// Main script for the quiz application
document.addEventListener('DOMContentLoaded', () => {
    // State variables
    let allQuestions = [];
    let currentQuestions = [];
    let userAnswers = [];
    let currentQuestionIndex = 0;
    let reviewQuestionIndex = 0;
    let examType = 'practice';
    let timer;
    let timeLeft = 0;
    let totalTime = 0;
    let examSeed = '';
    let activeSeed = '';
    let startTime = 0;
    let isQuizActive = false;
    let hasShown50PercentModal = false; // <-- Bug fix state variable

    // Add these constants at the top of the file, after the state variables
    const MAX_HISTORY_ROWS = 20;
    const MAX_HISTORY_DAYS = 7;
    const DEBOUNCE_DELAY = 300; // milliseconds

    // Pagination variables
    let currentPage = 1;
    const rowsPerPage = 3;

    // DOM Elements
    const setupSection = document.getElementById('setup-section');
    const quizSection = document.getElementById('quiz-section');
    const resultsSection = document.getElementById('results-section');
    const reviewSection = document.getElementById('review-section');
    const startExamBtn = document.getElementById('start-exam');
    const domainSelect = document.getElementById('domain-select');
    const questionCountSelect = document.getElementById('question-count');
    const examTypeSelect = document.getElementById('exam-type');
    const seedInput = document.getElementById('seed-input');
    const questionContainer = document.getElementById('question-container');
    const reviewContainer = document.getElementById('review-container');
    const prevQuestionBtn = document.getElementById('prev-question');
    const nextQuestionBtn = document.getElementById('next-question');
    const submitExamBtn = document.getElementById('submit-exam');
    const timerDisplay = document.getElementById('timer');
    const scoreDisplay = document.getElementById('score');
    const percentageDisplay = document.getElementById('percentage');
    const timeTakenDisplay = document.getElementById('time-taken');
    const restartExamBtn = document.getElementById('restart-exam');
    const reviewExamBtn = document.getElementById('review-exam');
    const historyTableBody = document.getElementById('history-table-body');
    const downloadCsvBtn = document.getElementById('download-csv');
    const downloadJsonBtn = document.getElementById('download-json');
    const resetHistoryBtn = document.getElementById('reset-history');
    const supportIcon = document.getElementById('support-icon');
    const supportModal = document.getElementById('support-modal');
    const skipSupportBtn = document.getElementById('skip-support');
    const progressIndicator = document.getElementById('progress-indicator');
    const reviewProgressIndicator = document.getElementById('review-progress-indicator');
    const resetModal = document.getElementById('reset-modal');
    const confirmResetBtn = document.getElementById('confirm-reset-btn');
    const cancelResetBtn = document.getElementById('cancel-reset-btn');
    const loaderOverlay = document.getElementById('loader-overlay');
    const prevReviewBtn = document.getElementById('prev-review-question');
    const nextReviewBtn = document.getElementById('next-review-question');
    const backToResultsBtn = document.getElementById('back-to-results');
    
    // --- INITIAL SETUP ---
    
    function loadQuestions() {
        if (typeof window.quizQuestions !== 'undefined') {
            allQuestions = window.quizQuestions;
        } else {
            console.error("Questions data could not be loaded. Make sure 'questions.js' is in the same directory.");
            allQuestions = [];
            alert("Error: questions.js could not be loaded. Please check the console for details.");
        }
        populateDomains();
        updateQuestionCountOptions(); // Initial population
    }

    function populateDomains() {
        const domains = [...new Set(allQuestions.map(q => q.domain))];
        domains.sort().forEach(domain => {
            const option = document.createElement('option');
            option.value = domain;
            option.textContent = domain;
            domainSelect.appendChild(option);
        });
    }

    function updateQuestionCountOptions() {
        const domainSelect = document.getElementById('domain-select');
        const questionCountSelect = document.getElementById('question-count');
        const selectedDomain = domainSelect.value;
        
        // Clear existing options
        questionCountSelect.innerHTML = '';
        
        // Get total questions for selected domain
        let totalQuestions = 0;
        if (selectedDomain === 'all') {
            totalQuestions = window.quizQuestions.length;
            
            // For "All Domains", show 10, 30, and 90 questions
            const allDomainOptions = [10, 30, 90];
            allDomainOptions.forEach(count => {
                if (count <= totalQuestions) {
                    const option = document.createElement('option');
                    option.value = count;
                    option.textContent = count;
                    questionCountSelect.appendChild(option);
                }
            });
        } else {
            totalQuestions = window.quizQuestions.filter(q => q.domain === selectedDomain).length;
            
            // For individual domains, show 10 and total questions
            if (totalQuestions >= 10) {
                const option = document.createElement('option');
                option.value = 10;
                option.textContent = '10';
                questionCountSelect.appendChild(option);
            }
            
            const option = document.createElement('option');
            option.value = totalQuestions;
            option.textContent = totalQuestions;
            questionCountSelect.appendChild(option);
        }
    }


    // --- SEED-BASED PRNG ---
    function xmur3(str) {
        for(var i = 0, h = 1779033703 ^ str.length; i < str.length; i++) {
            h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
            h = h << 13 | h >>> 19;
        }
        return function() {
            h = Math.imul(h ^ h >>> 16, 2246822507);
            h = Math.imul(h ^ h >>> 13, 3266489909);
            return (h ^= h >>> 16) >>> 0;
        }
    }
    
    function mulberry32(a) {
        return function() {
            var t = a += 0x6D2B79F5;
            t = Math.imul(t ^ t >>> 15, t | 1);
            t ^= t + Math.imul(t ^ t >>> 7, t | 61);
            return ((t ^ t >>> 14) >>> 0) / 4294967296;
        }
    }

    function shuffleArray(array, seed) {
        const seedFunc = xmur3(seed);
        const rand = mulberry32(seedFunc());
        let currentIndex = array.length, randomIndex;
        while (currentIndex != 0) {
            randomIndex = Math.floor(rand() * currentIndex);
            currentIndex--;
            [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
        }
        return array;
    }

    function generateSeed() {
        return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    }

    // --- EXAM LOGIC ---

    function beginExam() {
        loaderOverlay.classList.remove('hidden');
        
        setTimeout(() => {
            let numQuestions;
            let questionsForQuiz;
            let selectedDomain;

            if (activeSeed) {
                examSeed = activeSeed;
                const history = JSON.parse(localStorage.getItem('quizHistory')) || [];
                const seedRecord = history.find(r => r.seed === activeSeed);
                selectedDomain = seedRecord.domain;
                questionsForQuiz = selectedDomain === 'all' 
                    ? allQuestions
                    : allQuestions.filter(q => q.domain === selectedDomain);
                numQuestions = seedRecord.questionCount;
            } else {
                examSeed = generateSeed();
                selectedDomain = domainSelect.value;
                questionsForQuiz = selectedDomain === 'all' 
                    ? allQuestions 
                    : allQuestions.filter(q => q.domain === selectedDomain);
                numQuestions = parseInt(questionCountSelect.value);
            }

            examType = examTypeSelect.value;
            
            const shuffledQuestions = shuffleArray([...questionsForQuiz], examSeed);
            currentQuestions = shuffledQuestions.slice(0, numQuestions);
            
            userAnswers = new Array(currentQuestions.length).fill(null);
            currentQuestionIndex = 0;
            isQuizActive = true;
            hasShown50PercentModal = false;
            
            // Reset timer-related variables
            if (timer) {
                clearInterval(timer);
                timer = null;
            }
            timeLeft = 0;
            totalTime = 0;
            startTime = 0;
            
            setupSection.classList.add('hidden');
            resultsSection.classList.add('hidden');
            reviewSection.classList.add('hidden');
            quizSection.classList.remove('hidden');
            supportIcon.classList.add('hidden');

            if (examType === 'exam') {
                timeLeft = numQuestions * 60; // 1 minute per question
                totalTime = timeLeft;
            }
            
            startTimer();
            displayQuestion();
            loaderOverlay.classList.add('hidden');
        }, 500);
    }
    
    function displayQuestion() {
        if (currentQuestionIndex >= currentQuestions.length) return;
        const question = currentQuestions[currentQuestionIndex];
        let optionsHtml = '';
        
        question.options.forEach((option, index) => {
            const isSelected = userAnswers[currentQuestionIndex] === option;
            optionsHtml += `
                <div class="quiz-option p-4 border rounded-lg cursor-pointer mb-3 ${isSelected ? 'selected' : 'bg-gray-50'}" data-option-index="${index}">
                    <span class="font-bold mr-2">${index + 1}.</span> ${option}
                </div>
            `;
        });
        
        questionContainer.innerHTML = `
            <h3 class="text-2xl font-semibold mb-4">${currentQuestionIndex + 1}. ${question.question}</h3>
            <div id="options-container">${optionsHtml}</div>
        `;
        
        updateQuizNavigation();
        updateProgress();

        document.querySelectorAll('.quiz-option').forEach(el => {
            el.addEventListener('click', (e) => handleOptionSelect(e.currentTarget));
        });
    }

    function handleOptionSelect(selectedElement) {
        const selectedIndex = parseInt(selectedElement.dataset.optionIndex);
        const selectedOption = currentQuestions[currentQuestionIndex].options[selectedIndex];
        userAnswers[currentQuestionIndex] = selectedOption;
        displayQuestion();
    }

    function updateProgress() {
        const progress = currentQuestionIndex + 1;
        const total = currentQuestions.length;
        progressIndicator.textContent = `Question ${progress} of ${total}`;
        
        // Only show the 50% modal once per quiz
        if (progress >= Math.ceil(total / 2) && !hasShown50PercentModal) {
            showSupportModal(false);
            hasShown50PercentModal = true;
        }
    }

    function updateQuizNavigation() {
        prevQuestionBtn.disabled = currentQuestionIndex === 0;
        prevQuestionBtn.classList.toggle('opacity-50', prevQuestionBtn.disabled);
        nextQuestionBtn.textContent = userAnswers[currentQuestionIndex] === null ? 'Skip' : 'Next';
        
        if (currentQuestionIndex === currentQuestions.length - 1) {
            nextQuestionBtn.classList.add('hidden');
            submitExamBtn.classList.remove('hidden');
        } else {
            nextQuestionBtn.classList.remove('hidden');
            submitExamBtn.classList.add('hidden');
        }
    }
    
    function startTimer() {
        // Clear any existing timer
        if (timer) {
            clearInterval(timer);
        }
        
        timerDisplay.classList.remove('hidden');
        
        if (examType === 'exam') {
            timeLeft = totalTime;
            timer = setInterval(() => {
                timeLeft--;
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                timerDisplay.textContent = `Time Left: ${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    submitExam();
                }
            }, 1000);
        } else {
            // Practice mode timer
            startTime = Date.now();
            timer = setInterval(() => {
                const elapsedSeconds = Math.floor((Date.now() - startTime) / 1000);
                const hours = Math.floor(elapsedSeconds / 3600);
                const minutes = Math.floor((elapsedSeconds % 3600) / 60);
                const seconds = elapsedSeconds % 60;
                
                let timeString = 'Practice Mode - Elapsed: ';
                if (hours > 0) {
                    timeString += `${hours}:`;
                }
                timeString += `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
                
                timerDisplay.textContent = timeString;
            }, 1000);
        }
    }

    function submitExam() {
        if (timer) {
            clearInterval(timer);
            timer = null;
        }
        
        isQuizActive = false;
        let score = 0;
        currentQuestions.forEach((q, index) => {
            const correctAnswers = Array.isArray(q.answer) ? q.answer : [q.answer];
            if (correctAnswers.includes(userAnswers[index])) {
                score++;
            }
        });

        const percentage = currentQuestions.length > 0 ? ((score / currentQuestions.length) * 100) : 0;
        let timeTakenInSeconds;

        if (examType === 'exam') {
            timeTakenInSeconds = totalTime - timeLeft;
        } else {
            timeTakenInSeconds = startTime > 0 ? Math.floor((Date.now() - startTime) / 1000) : 0;
        }
        
        scoreDisplay.textContent = `${score} / ${currentQuestions.length}`;
        percentageDisplay.textContent = `${percentage.toFixed(2)}%`;
        timeTakenDisplay.textContent = formatTime(timeTakenInSeconds);
        
        saveHistory(score, percentage, timeTakenInSeconds);

        quizSection.classList.add('hidden');
        resultsSection.classList.remove('hidden');
        supportIcon.classList.remove('hidden');
        
        if (percentage >= 80) {
            triggerCelebration();
        }
        
        showSupportModal(false);
    }

    // --- REVIEW & CELEBRATION LOGIC ---
    function triggerCelebration() {
        const duration = 5 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        const interval = setInterval(function() {
            const timeLeft = animationEnd - Date.now();

            if (timeLeft <= 0) {
                return clearInterval(interval);
            }

            const particleCount = 50 * (timeLeft / duration);
            confetti({ ...defaults, particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } });
            confetti({ ...defaults, particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } });
        }, 250);
    }

    function startReview() {
        reviewQuestionIndex = 0;
        resultsSection.classList.add('hidden');
        reviewSection.classList.remove('hidden');
        displayReviewQuestion();
    }
    
    function displayReviewQuestion() {
        const question = currentQuestions[reviewQuestionIndex];
        const userAnswer = userAnswers[reviewQuestionIndex];
        const correctAnswers = Array.isArray(question.answer) ? question.answer : [question.answer];
        let optionsHtml = '';
        
        question.options.forEach(option => {
            let classes = 'quiz-option p-4 border rounded-lg mb-3';
            const isCorrect = correctAnswers.includes(option);
            const isUserChoice = userAnswer === option;
            
            if(isCorrect) {
                classes += ' correct-answer';
            }
            if(isUserChoice && !isCorrect) {
                classes += ' incorrect-answer';
            }
            if(isUserChoice) {
                classes += ' user-selected';
            }

            optionsHtml += `<div class="${classes}">${option}</div>`;
        });

        reviewContainer.innerHTML = `
            <h3 class="text-2xl font-semibold mb-4">${reviewQuestionIndex + 1}. ${question.question}</h3>
            <div id="review-options-container">${optionsHtml}</div>
            <div class="explanation-box">
                <h4 class="font-bold text-lg mb-2">Explanation:</h4>
                <p>${question.explanation || 'No explanation available.'}</p>
            </div>
        `;
        updateReviewNavigation();
    }

    function updateReviewNavigation() {
        reviewProgressIndicator.textContent = `Question ${reviewQuestionIndex + 1} of ${currentQuestions.length}`;
        prevReviewBtn.disabled = reviewQuestionIndex === 0;
        prevReviewBtn.classList.toggle('opacity-50', prevReviewBtn.disabled);
        nextReviewBtn.disabled = reviewQuestionIndex === currentQuestions.length - 1;
        nextReviewBtn.classList.toggle('opacity-50', nextReviewBtn.disabled);
    }

    // --- UTILITIES & HISTORY ---

    function formatTime(totalSeconds) {
        if (isNaN(totalSeconds) || totalSeconds < 0) return '00:00:00';
        const hours = Math.floor(totalSeconds / 3600).toString().padStart(2, '0');
        const minutes = Math.floor((totalSeconds % 3600) / 60).toString().padStart(2, '0');
        const seconds = (totalSeconds % 60).toString().padStart(2, '0');
        return `${hours}:${minutes}:${seconds}`;
    }

    function saveHistory(score, percentage, timeInSeconds) {
        try {
            const history = safeLocalStorageGet('quizHistory', []);
            const now = new Date();
            
            // Get the current domain and question count
            const currentDomain = domainSelect.value;
            const currentQuestionCount = currentQuestions.length;
            
            // Validate domain exists
            const domains = [...new Set(allQuestions.map(q => q.domain))];
            if (!domains.includes(currentDomain) && currentDomain !== 'all') {
                console.error('Invalid domain:', currentDomain);
                return;
            }
            
            // Validate question count
            const availableQuestions = currentDomain === 'all' 
                ? allQuestions 
                : allQuestions.filter(q => q.domain === currentDomain);
            
            if (currentQuestionCount > availableQuestions.length) {
                console.error('Invalid question count:', currentQuestionCount);
                return;
            }

            const newRecord = {
                seed: examSeed,
                date: now.toLocaleDateString(),
                time: now.toLocaleTimeString(),
                timestamp: now.getTime(), // Add timestamp for age-based filtering
                score: `${score} / ${currentQuestionCount}`,
                percentage: `${percentage.toFixed(2)}%`,
                timeTaken: formatTime(timeInSeconds),
                examType: examType.charAt(0).toUpperCase() + examType.slice(1),
                domain: currentDomain,
                questionCount: currentQuestionCount
            };

            // If using an active seed, update the existing record instead of adding a new one
            if (activeSeed) {
                const existingIndex = history.findIndex(r => r.seed === activeSeed);
                if (existingIndex !== -1) {
                    history[existingIndex] = newRecord;
                } else {
                    history.unshift(newRecord);
                }
            } else {
                history.unshift(newRecord);
            }

            // Clean up old records
            const cleanedHistory = cleanupHistory(history);
            safeLocalStorageSet('quizHistory', cleanedHistory);
            currentPage = 1; // Reset to first page when new record is added
            updateHistoryTable();
        } catch (error) {
            console.error('Error saving history:', error);
            alert('There was an error saving your exam history. Please try again.');
        }
    }

    function cleanupHistory(history) {
        const now = Date.now();
        const maxAge = MAX_HISTORY_DAYS * 24 * 60 * 60 * 1000; // Convert days to milliseconds
        
        // Filter out records older than MAX_HISTORY_DAYS
        let cleanedHistory = history.filter(record => {
            const recordDate = new Date(record.timestamp);
            return (now - recordDate.getTime()) <= maxAge;
        });
        
        // Limit to MAX_HISTORY_ROWS
        if (cleanedHistory.length > MAX_HISTORY_ROWS) {
            cleanedHistory = cleanedHistory.slice(0, MAX_HISTORY_ROWS);
        }
        
        return cleanedHistory;
    }

    function loadHistory() {
        const history = JSON.parse(localStorage.getItem('quizHistory')) || [];
        const cleanedHistory = cleanupHistory(history);
        
        // Update localStorage with cleaned history if any records were removed
        if (cleanedHistory.length !== history.length) {
            localStorage.setItem('quizHistory', JSON.stringify(cleanedHistory));
        }
        
        historyTableBody.innerHTML = '';
        if (cleanedHistory.length === 0) {
            historyTableBody.innerHTML = '<tr><td colspan="6" class="text-center py-4">No exam history found.</td></tr>';
        } else {
            cleanedHistory.forEach(record => {
                const row = `
                    <tr>
                        <td class="py-2 px-4 border-b font-mono text-xs">${record.seed}</td>
                        <td class="py-2 px-4 border-b">${record.date} ${record.time}</td>
                        <td class="py-2 px-4 border-b">${record.examType || 'N/A'}</td>
                        <td class="py-2 px-4 border-b">${record.score}</td>
                        <td class="py-2 px-4 border-b">${record.percentage}</td>
                        <td class="py-2 px-4 border-b">${record.timeTaken}</td>
                    </tr>`;
                historyTableBody.innerHTML += row;
            });
        }
        
        // Add information about history limits
        const infoRow = `
            <tr class="bg-gray-50">
                <td colspan="6" class="py-2 px-4 text-sm text-gray-600">
                    <i class="fas fa-info-circle mr-1"></i>
                    History is limited to ${MAX_HISTORY_ROWS} records and ${MAX_HISTORY_DAYS} days retention.
                </td>
            </tr>`;
        historyTableBody.innerHTML += infoRow;
    }
    
    function downloadData(data, filename, type) {
        try {
            let processedData;
            if (type === 'text/csv') {
                // Properly escape CSV data
                const escapeCSV = (str) => {
                    if (typeof str !== 'string') return str;
                    // Escape quotes by doubling them and wrap in quotes if contains special characters
                    const needsQuotes = /[",\n\r]/.test(str);
                    const escaped = str.replace(/"/g, '""');
                    return needsQuotes ? `"${escaped}"` : escaped;
                };

                const history = JSON.parse(data);
                const headers = Object.keys(history[0]).filter(key => key !== 'timestamp').join(',');
                const rows = history.map(record => {
                    const values = Object.entries(record)
                        .filter(([key]) => key !== 'timestamp')
                        .map(([_, value]) => escapeCSV(value));
                    return values.join(',');
                });
                processedData = `${headers}\n${rows.join('\n')}`;
            } else {
                processedData = data;
            }

            const blob = new Blob([processedData], { type });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error downloading data:', error);
            alert('There was an error downloading the history. Please try again.');
        }
    }
    
    function showSupportModal(startAfter = true) {
        supportModal.classList.remove('hidden');
        if (startAfter) {
            skipSupportBtn.textContent = 'Skip to Exam';
            skipSupportBtn.onclick = () => {
                supportModal.classList.add('hidden');
                beginExam();
            };
        } else {
                skipSupportBtn.textContent = 'Close';
                skipSupportBtn.onclick = () => supportModal.classList.add('hidden');
        }
    }

    function handleSeedInput() {
        const seedValue = seedInput.value.trim();
        const history = JSON.parse(localStorage.getItem('quizHistory')) || [];
        const seedRecord = history.find(r => r.seed === seedValue);

        if (seedValue === '') {
            resetSeedState();
            return;
        }

        if (seedRecord) {
            // Validate if the domain still exists in current question bank
            const domains = [...new Set(allQuestions.map(q => q.domain))];
            if (!domains.includes(seedRecord.domain)) {
                seedInput.classList.add('border-red-500', 'ring-red-500');
                seedInput.setCustomValidity('This seed references a domain that no longer exists.');
                return;
            }

            // Validate if the question count is still valid
            const availableQuestions = seedRecord.domain === 'all' 
                ? allQuestions 
                : allQuestions.filter(q => q.domain === seedRecord.domain);
            
            if (seedRecord.questionCount > availableQuestions.length) {
                seedInput.classList.add('border-red-500', 'ring-red-500');
                seedInput.setCustomValidity(`This seed references ${seedRecord.questionCount} questions, but only ${availableQuestions.length} are available.`);
                return;
            }

            // If all validations pass, set the seed
            activeSeed = seedValue;
            domainSelect.value = seedRecord.domain;
            updateQuestionCountOptions();
            questionCountSelect.value = seedRecord.questionCount;
            
            domainSelect.disabled = true;
            questionCountSelect.disabled = true;
            seedInput.classList.add('border-green-500', 'ring-green-500');
            seedInput.classList.remove('border-red-500', 'ring-red-500');
            seedInput.setCustomValidity('');
        } else {
            resetSeedState();
            seedInput.classList.add('border-red-500', 'ring-red-500');
            seedInput.setCustomValidity('Invalid seed. Please enter a valid seed from your history.');
        }
    }
    
    function resetSeedState() {
        activeSeed = '';
        domainSelect.disabled = false;
        questionCountSelect.disabled = false;
        seedInput.value = '';
        seedInput.classList.remove('border-green-500', 'ring-green-500', 'border-red-500', 'ring-red-500');
        seedInput.setCustomValidity('');
    }
    
    // --- EVENT LISTENERS ---
    domainSelect.addEventListener('change', updateQuestionCountOptions);
    seedInput.addEventListener('input', handleSeedInput);
    startExamBtn.addEventListener('click', () => { showSupportModal(); });
    restartExamBtn.addEventListener('click', () => {
        resultsSection.classList.add('hidden');
        setupSection.classList.remove('hidden');
        resetSeedState();
    });

    // Quiz Navigation
    nextQuestionBtn.addEventListener('click', () => {
        if (currentQuestionIndex < currentQuestions.length - 1) {
            currentQuestionIndex++;
            displayQuestion();
        }
    });
    prevQuestionBtn.addEventListener('click', () => {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            displayQuestion();
        }
    });
    submitExamBtn.addEventListener('click', submitExam);

    // Review Navigation
    reviewExamBtn.addEventListener('click', startReview);
    nextReviewBtn.addEventListener('click', () => {
        if (reviewQuestionIndex < currentQuestions.length - 1) {
            reviewQuestionIndex++;
            displayReviewQuestion();
        }
    });
    prevReviewBtn.addEventListener('click', () => {
        if (reviewQuestionIndex > 0) {
            reviewQuestionIndex--;
            displayReviewQuestion();
        }
    });
    backToResultsBtn.addEventListener('click', () => {
        reviewSection.classList.add('hidden');
        resultsSection.classList.remove('hidden');
    });
    
    // History Listeners
    resetHistoryBtn.addEventListener('click', () => { resetModal.classList.remove('hidden'); });
    cancelResetBtn.addEventListener('click', () => { resetModal.classList.add('hidden'); });
    confirmResetBtn.addEventListener('click', () => {
        localStorage.removeItem('quizHistory');
        loadHistory();
        resetModal.classList.add('hidden');
    });
    downloadJsonBtn.addEventListener('click', () => {
        const history = localStorage.getItem('quizHistory') || '[]';
        downloadData(history, 'quiz_history.json', 'application/json');
    });
    downloadCsvBtn.addEventListener('click', () => {
        const history = JSON.parse(localStorage.getItem('quizHistory')) || [];
        if (history.length === 0) return;
        const headers = Object.keys(history[0]).join(',');
        const rows = history.map(record => `"${Object.values(record).join('","')}"`).join('\n');
        downloadData(`${headers}\n${rows}`, 'quiz_history.csv', 'text/csv');
    });

    // Keyboard and Window Listeners
    window.addEventListener('beforeunload', (e) => {
        if (isQuizActive) {
            e.preventDefault();
            e.returnValue = '';
        }
    });
    document.addEventListener('keydown', (e) => {
        if (!isQuizActive) return;
        if (e.key === 'ArrowRight') nextQuestionBtn.click();
        if (e.key === 'ArrowLeft') prevQuestionBtn.click();
        if(['1','2','3','4'].includes(e.key)) {
            const optionElement = document.querySelector(`.quiz-option[data-option-index="${parseInt(e.key) - 1}"]`);
            if(optionElement) handleOptionSelect(optionElement);
        }
    });

    // --- INITIALIZATION ---
    loadQuestions();
    loadHistory();

    // Add these utility functions at the top of the file, after the constants
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    function safeGetElement(id) {
        const element = document.getElementById(id);
        if (!element) {
            console.error(`Element with id '${id}' not found`);
            return null;
        }
        return element;
    }

    function safeLocalStorageGet(key, defaultValue = []) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (error) {
            console.error(`Error reading from localStorage (${key}):`, error);
            return defaultValue;
        }
    }

    function safeLocalStorageSet(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (error) {
            console.error(`Error writing to localStorage (${key}):`, error);
            return false;
        }
    }

    // Function to update history table with pagination
    function updateHistoryTable() {
        const historyTableBody = document.getElementById('history-table-body');
        const history = safeLocalStorageGet('quizHistory', []);
        const cleanedHistory = cleanupHistory(history);
        
        // Calculate pagination
        const totalRows = cleanedHistory.length;
        const totalPages = Math.ceil(totalRows / rowsPerPage);
        const start = (currentPage - 1) * rowsPerPage;
        const end = Math.min(start + rowsPerPage, totalRows);
        
        // Update pagination info
        document.getElementById('history-start').textContent = totalRows === 0 ? 0 : start + 1;
        document.getElementById('history-end').textContent = end;
        document.getElementById('history-total').textContent = totalRows;
        
        // Update pagination buttons
        document.getElementById('prev-page').disabled = currentPage === 1;
        document.getElementById('next-page').disabled = currentPage === totalPages || totalPages === 0;
        
        // Clear existing rows
        historyTableBody.innerHTML = '';
        
        if (cleanedHistory.length === 0) {
            historyTableBody.innerHTML = '<tr><td colspan="6" class="text-center py-4">No exam history found.</td></tr>';
        } else {
            // Add rows for current page
            for (let i = start; i < end; i++) {
                const record = cleanedHistory[i];
                const row = document.createElement('tr');
                row.className = 'hover:bg-gray-50';
                row.innerHTML = `
                    <td class="py-2 px-3 border-b text-sm font-mono">${record.seed}</td>
                    <td class="py-2 px-3 border-b text-sm">${record.date} ${record.time}</td>
                    <td class="py-2 px-3 border-b text-sm">${record.examType || 'N/A'}</td>
                    <td class="py-2 px-3 border-b text-sm">${record.score}</td>
                    <td class="py-2 px-3 border-b text-sm">${record.percentage}%</td>
                    <td class="py-2 px-3 border-b text-sm">${record.timeTaken}</td>
                `;
                historyTableBody.appendChild(row);
            }
        }
        
        // Add information about history limits
        const infoRow = document.createElement('tr');
        infoRow.className = 'bg-gray-50';
        infoRow.innerHTML = `
            <td colspan="6" class="py-2 px-3 text-sm text-gray-600">
                <i class="fas fa-info-circle mr-1"></i>
                History is limited to ${MAX_HISTORY_ROWS} records and ${MAX_HISTORY_DAYS} days retention.
            </td>
        `;
        historyTableBody.appendChild(infoRow);
    }

    // Add event listeners for pagination
    document.getElementById('prev-page').addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            updateHistoryTable();
        }
    });

    document.getElementById('next-page').addEventListener('click', () => {
        const history = safeLocalStorageGet('quizHistory', []);
        const totalPages = Math.ceil(history.length / rowsPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            updateHistoryTable();
        }
    });

    // Update the existing saveHistory function to reset pagination
    function saveHistory(score, percentage, timeInSeconds) {
        try {
            const history = safeLocalStorageGet('quizHistory', []);
            const now = new Date();
            
            // Get the current domain and question count
            const currentDomain = domainSelect.value;
            const currentQuestionCount = currentQuestions.length;
            
            // Validate domain exists
            const domains = [...new Set(allQuestions.map(q => q.domain))];
            if (!domains.includes(currentDomain) && currentDomain !== 'all') {
                console.error('Invalid domain:', currentDomain);
                return;
            }
            
            // Validate question count
            const availableQuestions = currentDomain === 'all' 
                ? allQuestions 
                : allQuestions.filter(q => q.domain === currentDomain);
            
            if (currentQuestionCount > availableQuestions.length) {
                console.error('Invalid question count:', currentQuestionCount);
                return;
            }

            const newRecord = {
                seed: examSeed,
                date: now.toLocaleDateString(),
                time: now.toLocaleTimeString(),
                timestamp: now.getTime(), // Add timestamp for age-based filtering
                score: `${score} / ${currentQuestionCount}`,
                percentage: `${percentage.toFixed(2)}%`,
                timeTaken: formatTime(timeInSeconds),
                examType: examType.charAt(0).toUpperCase() + examType.slice(1),
                domain: currentDomain,
                questionCount: currentQuestionCount
            };

            // If using an active seed, update the existing record instead of adding a new one
            if (activeSeed) {
                const existingIndex = history.findIndex(r => r.seed === activeSeed);
                if (existingIndex !== -1) {
                    history[existingIndex] = newRecord;
                } else {
                    history.unshift(newRecord);
                }
            } else {
                history.unshift(newRecord);
            }

            // Clean up old records
            const cleanedHistory = cleanupHistory(history);
            safeLocalStorageSet('quizHistory', cleanedHistory);
            currentPage = 1; // Reset to first page when new record is added
            updateHistoryTable();
        } catch (error) {
            console.error('Error saving history:', error);
            alert('There was an error saving your exam history. Please try again.');
        }
    }

    // Update the existing resetHistory function
    function resetHistory() {
        localStorage.removeItem('quizHistory');
        currentPage = 1;
        updateHistoryTable();
    }

    // Update event listeners to use debounced functions
    const debouncedHandleSeedInput = debounce(handleSeedInput, DEBOUNCE_DELAY);
    if (seedInput) {
        seedInput.addEventListener('input', debouncedHandleSeedInput);
    }
});