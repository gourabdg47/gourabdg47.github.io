// Main script for the quiz application
document.addEventListener('DOMContentLoaded', () => {
    // --- STATE VARIABLES ---
    let allQuestions = [];
    let currentQuestions = [];
    let userAnswers = [];
    let currentQuestionIndex = 0;
    let reviewQuestionIndex = 0;
    let examType = 'practice';
    let currentExamDomain = 'all'; // FIX: State for the current exam's domain
    let timer;
    let timeLeft = 0;
    let totalTime = 0;
    let examSeed = '';
    let activeSeed = '';
    let startTime = 0;
    let isQuizActive = false;
    let hasShown50PercentModal = false;

    // --- CONSTANTS ---
    const MAX_HISTORY_ROWS = 20;
    const MAX_HISTORY_DAYS = 7;
    const DEBOUNCE_DELAY = 300; // milliseconds

    // --- DOM ELEMENTS ---
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
    const analyticsSection = document.getElementById('analytics-section');
    const toggleAnalyticsBtn = document.getElementById('toggle-analytics-btn');


    // --- UTILITY FUNCTIONS ---
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

    // --- INITIAL SETUP ---
    function loadQuestions() {
        if (typeof window.quizQuestions !== 'undefined' && window.quizQuestions.length > 0) {
            allQuestions = window.quizQuestions;
        } else {
            console.error("Questions data could not be loaded or is empty.");
            // Changed alert to a console error as per guidelines
            console.error("Error: Questions could not be loaded. Please check the console for details.");
            allQuestions = [];
        }
        populateDomains();
        updateQuestionCountOptions();
    }

    function populateDomains() {
        const domains = [...new Set(allQuestions.map(q => q.domain))].sort();
        domainSelect.innerHTML = '<option value="all">All Domains</option>';
        domains.forEach(domain => {
            const count = allQuestions.filter(q => q.domain === domain).length;
            if (count >= 10) {
                const option = document.createElement('option');
                option.value = domain;
                option.textContent = domain;
                domainSelect.appendChild(option);
            }
        });
    }

    function updateQuestionCountOptions() {
        const selectedDomain = domainSelect.value;
        const questionsForDomain = selectedDomain === 'all' 
            ? allQuestions 
            : allQuestions.filter(q => q.domain === selectedDomain);
        
        const totalQuestions = questionsForDomain.length;
        questionCountSelect.innerHTML = '';
        
        // Add options based on available questions
        if (totalQuestions >= 10) {
            // Always add 10 if we have at least 10 questions
            const option10 = document.createElement('option');
            option10.value = 10;
            option10.textContent = '10 Questions';
            questionCountSelect.appendChild(option10);
            
            if (totalQuestions >= 30) {
                // Add 30 if we have at least 30 questions
                const option30 = document.createElement('option');
                option30.value = 30;
                option30.textContent = '30 Questions';
                questionCountSelect.appendChild(option30);
                
                if (totalQuestions >= 90) {
                    // Add 90 if we have at least 90 questions
                    const option90 = document.createElement('option');
                    option90.value = 90;
                    option90.textContent = '90 Questions';
                    questionCountSelect.appendChild(option90);
                }
            }
            
            // Add the maximum value option
            const maxOption = document.createElement('option');
            maxOption.value = totalQuestions;
            
            // If we have more than 90 questions, show it as "All"
            if (totalQuestions > 90) {
                maxOption.textContent = `All (${totalQuestions})`;
            } else {
                maxOption.textContent = `${totalQuestions} Questions`;
            }
            questionCountSelect.appendChild(maxOption);
        } else {
            // If we have less than 10 questions, just show the total
            const option = document.createElement('option');
            option.value = totalQuestions;
            option.textContent = `${totalQuestions} Questions`;
            questionCountSelect.appendChild(option);
        }
        
        questionCountSelect.classList.remove('hidden');
        
        // If in exam mode, ensure 90 questions is selected
        if (examTypeSelect.value === 'exam') {
            questionCountSelect.value = '90';
        }
    }

    // --- SEED-BASED PRNG ---
    function xmur3(str) {
        let h = 1779033703 ^ str.length;
        for (let i = 0; i < str.length; i++) {
            h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
            h = h << 13 | h >>> 19;
        }
        return function () {
            h = Math.imul(h ^ h >>> 16, 2246822507);
            h = Math.imul(h ^ h >>> 13, 3266489909);
            return (h ^= h >>> 16) >>> 0;
        }
    }

    function mulberry32(a) {
        return function () {
            let t = a += 0x6D2B79F5;
            t = Math.imul(t ^ t >>> 15, t | 1);
            t ^= t + Math.imul(t ^ t >>> 7, t | 61);
            return ((t ^ t >>> 14) >>> 0) / 4294967296;
        }
    }

    function shuffleArray(array, seed) {
        const seedFunc = xmur3(seed);
        const rand = mulberry32(seedFunc());
        let currentIndex = array.length;
        while (currentIndex !== 0) {
            const randomIndex = Math.floor(rand() * currentIndex);
            currentIndex--;
            [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
        }
        return array;
    }

    function generateSeed() {
        return Math.random().toString(36).substring(2, 10) + Math.random().toString(36).substring(2, 10);
    }

    // --- EXAM LOGIC ---
    function beginExam() {
        loaderOverlay.classList.remove('hidden');

        setTimeout(() => {
            let numQuestions, questionsForQuiz, selectedDomain;

            if (activeSeed) {
                examSeed = activeSeed;
                const history = safeLocalStorageGet('quizHistory');
                const seedRecord = history.find(r => r.seed === activeSeed);
                selectedDomain = seedRecord.domain;
                numQuestions = seedRecord.questionCount;
            } else {
                examSeed = generateSeed();
                selectedDomain = domainSelect.value;
                numQuestions = parseInt(questionCountSelect.value);
            }

            questionsForQuiz = selectedDomain === 'all'
                ? allQuestions
                : allQuestions.filter(q => q.domain === selectedDomain);

            currentQuestions = shuffleArray([...questionsForQuiz], examSeed).slice(0, numQuestions);
            examType = examTypeSelect.value;
            currentExamDomain = selectedDomain; // FIX: Set domain state at the start

            userAnswers = new Array(currentQuestions.length).fill(null);
            currentQuestionIndex = 0;
            isQuizActive = true;
            hasShown50PercentModal = false;

            if (timer) clearInterval(timer);
            // --- MODIFICATION START ---
            if (examType === 'exam') {
                totalTime = 5400; // 90 minutes for exam mode (90 * 60 seconds)
                timeLeft = 5400;
            } else {
                totalTime = currentQuestions.length * 60; // Original logic for practice mode
                timeLeft = totalTime; // Original logic for practice mode
            }
            // --- MODIFICATION END ---

            setupSection.classList.add('hidden');
            resultsSection.classList.add('hidden');
            reviewSection.classList.add('hidden');
            quizSection.classList.remove('hidden');
            supportIcon.classList.add('hidden');

            startTimer();
            displayQuestion();
            loaderOverlay.classList.add('hidden');
        }, 500);
    }

    function displayQuestion() {
        if (currentQuestionIndex >= currentQuestions.length) return;
        const question = currentQuestions[currentQuestionIndex];
        const isMultiAnswer = Array.isArray(question.answer);
        const selectedAnswers = userAnswers[currentQuestionIndex] || (isMultiAnswer ? [] : null);

        const optionsHtml = question.options.map((option, index) => {
            const isSelected = isMultiAnswer ? selectedAnswers.includes(option) : selectedAnswers === option;
            return `
                <button class="quiz-option text-left p-4 border rounded-lg mb-3 w-full transition-colors ${isSelected ? 'selected bg-blue-100 border-blue-500' : 'bg-gray-50 hover:bg-blue-50'}" data-option-index="${index}">
                    <span class="font-bold mr-2">${String.fromCharCode(65 + index)}.</span> ${option}
                </button>
            `;
        }).join('');

        questionContainer.innerHTML = `
            <h3 class="text-xl md:text-2xl font-semibold mb-4">${question.question}</h3>
            ${isMultiAnswer ? `<div class='mb-3 text-sm font-medium text-blue-700 p-2 bg-blue-50 rounded-md'>Select ${question.answer.length} answer(s)</div>` : ''}
            <div id="options-container">${optionsHtml}</div>
        `;
        
        updateQuizNavigation();
        updateProgress();
    }

    function handleOptionSelect(selectedElement) {
        const selectedIndex = parseInt(selectedElement.dataset.optionIndex);
        const question = currentQuestions[currentQuestionIndex];
        const option = question.options[selectedIndex];
        
        if (Array.isArray(question.answer)) {
            let currentSelections = userAnswers[currentQuestionIndex] || [];
            if (currentSelections.includes(option)) {
                userAnswers[currentQuestionIndex] = currentSelections.filter(ans => ans !== option);
            } else if (currentSelections.length < question.answer.length) {
                userAnswers[currentQuestionIndex] = [...currentSelections, option];
            }
        } else {
            userAnswers[currentQuestionIndex] = option;
        }
        displayQuestion();
    }
    
    function updateProgress() {
        const progress = currentQuestionIndex + 1;
        const total = currentQuestions.length;
        progressIndicator.textContent = `Question ${progress} of ${total}`;
        
        if (progress >= Math.ceil(total / 2) && !hasShown50PercentModal) {
            showSupportModal(false);
            hasShown50PercentModal = true;
        }
    }

    function updateQuizNavigation() {
        prevQuestionBtn.disabled = currentQuestionIndex === 0;
        prevQuestionBtn.classList.toggle('opacity-50', prevQuestionBtn.disabled);
        nextQuestionBtn.classList.toggle('hidden', currentQuestionIndex === currentQuestions.length - 1);
        submitExamBtn.classList.toggle('hidden', currentQuestionIndex !== currentQuestions.length - 1);
    }

    function startTimer() {
        if (timer) clearInterval(timer);
        timerDisplay.classList.remove('hidden');
        
        if (examType === 'exam') {
            timer = setInterval(() => {
                timeLeft--;
                timerDisplay.textContent = `Time Left: ${formatTime(timeLeft, false)}`;
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    submitExam();
                }
            }, 1000);
        } else {
            startTime = Date.now();
            timer = setInterval(() => {
                const elapsedSeconds = Math.floor((Date.now() - startTime) / 1000);
                timerDisplay.textContent = `Elapsed: ${formatTime(elapsedSeconds, false)}`;
            }, 1000);
        }
    }

    function submitExam() {
        if (timer) clearInterval(timer);
        isQuizActive = false;
        
        let score = 0;
        currentQuestions.forEach((q, index) => {
            const correct = Array.isArray(q.answer) ? q.answer.slice().sort() : [q.answer];
            let userAns = userAnswers[index];
            userAns = Array.isArray(userAns) ? userAns.slice().sort() : (userAns ? [userAns] : []);
            
            if (userAns.length === correct.length && userAns.every((val, i) => val === correct[i])) {
                score++;
            }
        });

        const percentage = currentQuestions.length > 0 ? (score / currentQuestions.length) * 100 : 0;
        // Calculation of time taken is correct based on exam type and initial totalTime.
        const timeTakenInSeconds = examType === 'exam' ? totalTime - timeLeft : Math.floor((Date.now() - startTime) / 1000);
        
        scoreDisplay.textContent = `${score} / ${currentQuestions.length}`;
        percentageDisplay.textContent = `${percentage.toFixed(2)}%`;
        timeTakenDisplay.textContent = formatTime(timeTakenInSeconds, true);
        
        saveHistory(score, percentage, timeTakenInSeconds);

        quizSection.classList.add('hidden');
        resultsSection.classList.remove('hidden');
        supportIcon.classList.remove('hidden');
        
        if (percentage >= 80) triggerCelebration();
        
        // Show support modal after a short delay (reduced to 30ms)
        setTimeout(() => {
            showSupportModal(false);
        }, 350);
    }

    // --- REVIEW & CELEBRATION ---
    function triggerCelebration() {
        if (typeof confetti !== 'function') return;
        const end = Date.now() + (3 * 1000);
        (function frame() {
            confetti({ particleCount: 2, angle: 60, spread: 55, origin: { x: 0 } });
            confetti({ particleCount: 2, angle: 120, spread: 55, origin: { x: 1 } });
            if (Date.now() < end) requestAnimationFrame(frame);
        }());
    }

    function startReview() {
        reviewQuestionIndex = 0;
        resultsSection.classList.add('hidden');
        reviewSection.classList.remove('hidden');
        displayReviewQuestion();
    }
    
    function displayReviewQuestion() {
        const question = currentQuestions[reviewQuestionIndex];
        const userAnswer = userAnswers[reviewQuestionIndex] || [];
        const correctAnswers = Array.isArray(question.answer) ? question.answer : [question.answer];
        
        const optionsHtml = question.options.map(option => {
            const isCorrect = correctAnswers.includes(option);
            const isUserChoice = Array.isArray(userAnswer) ? userAnswer.includes(option) : userAnswer === option;
            let classes = 'p-4 border rounded-lg mb-3';
            if (isCorrect) classes += ' bg-green-100 border-green-500';
            else if (isUserChoice) classes += ' bg-red-100 border-red-500';
            else classes += ' bg-gray-50';
            return `<div class="${classes}">${option}</div>`;
        }).join('');

        reviewContainer.innerHTML = `
            <h3 class="text-xl md:text-2xl font-semibold mb-4">${reviewQuestionIndex + 1}. ${question.question}</h3>
            <div class="mb-4">${optionsHtml}</div>
            <div class="mt-6 p-4 bg-gray-100 rounded-lg border border-gray-200">
                <h4 class="font-bold text-lg mb-2 text-gray-800">Explanation:</h4>
                <p class="text-gray-700">${question.explanation || 'No explanation available.'}</p>
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

    // --- HISTORY & DATA HANDLING ---
    function formatTime(totalSeconds, showHours = true) {
        if (isNaN(totalSeconds) || totalSeconds < 0) return showHours ? '00:00:00' : '00:00';
        const hours = Math.floor(totalSeconds / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        const seconds = totalSeconds % 60;
        const paddedMinutes = String(minutes).padStart(2, '0');
        const paddedSeconds = String(seconds).padStart(2, '0');
        if (showHours) {
            return `${String(hours).padStart(2, '0')}:${paddedMinutes}:${paddedSeconds}`;
        }
        return `${paddedMinutes}:${paddedSeconds}`;
    }

    function saveHistory(score, percentage, timeInSeconds) {
        const history = safeLocalStorageGet('quizHistory');
        const now = new Date();
        const newRecord = {
            seed: examSeed,
            date: now.toLocaleDateString(),
            time: now.toLocaleTimeString(),
            timestamp: now.getTime(),
            score: `${score} / ${currentQuestions.length}`,
            percentage: `${percentage.toFixed(2)}%`,
            timeTaken: formatTime(timeInSeconds, true),
            examType: examType.charAt(0).toUpperCase() + examType.slice(1),
            domain: currentExamDomain, // FIX: Use the state variable
            questionCount: currentQuestions.length
        };

        const existingIndex = activeSeed ? history.findIndex(r => r.seed === activeSeed) : -1;
        if (existingIndex !== -1) {
            history[existingIndex] = newRecord;
        } else {
            history.unshift(newRecord);
        }

        const cleanedHistory = cleanupHistory(history);
        safeLocalStorageSet('quizHistory', cleanedHistory);
        loadHistory();
    }

    // OPTIMIZATION: Reusable function to clean history based on age and count
    function cleanupHistory(history) {
        const now = Date.now();
        const maxAge = MAX_HISTORY_DAYS * 24 * 60 * 60 * 1000;
        let cleaned = history.filter(record => (now - (record.timestamp || 0)) <= maxAge);
        return cleaned.slice(0, MAX_HISTORY_ROWS);
    }

    // Load Chart.js if not already loaded
    function ensureChartJsLoaded(callback) {
        if (window.Chart) {
            callback();
            return;
        }
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
        script.onload = callback;
        document.head.appendChild(script);
    }

    let scoreChart = null;
    function renderScoreGraph(history) {
        ensureChartJsLoaded(() => {
            const ctx = document.getElementById('score-graph').getContext('2d');
            // Filter for Exam Mode only
            const examHistory = history.filter(r => r.examType === 'Exam');
            const labels = examHistory.map((r, i) => r.date + ' ' + r.time);
            const scores = examHistory.map(r => parseFloat(r.percentage.replace('%', '')));
            // Target line
            const targetData = Array(scores.length).fill(80);

            if (scoreChart) {
                scoreChart.data.labels = labels;
                scoreChart.data.datasets[0].data = scores;
                scoreChart.data.datasets[1].data = targetData;
                scoreChart.update();
                return;
            }

            scoreChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Your Score (%)',
                            data: scores,
                            borderColor: '#4A90E2',
                            backgroundColor: 'rgba(74,144,226,0.1)',
                            fill: true,
                            tension: 0.3,
                            pointRadius: 4,
                            pointBackgroundColor: '#4A90E2',
                        },
                        {
                            label: 'Target (80%)',
                            data: targetData,
                            borderColor: '#FFA500',
                            borderDash: [8, 4],
                            fill: false,
                            pointRadius: 0,
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: true },
                        tooltip: { enabled: true }
                    },
                    scales: {
                        y: {
                            min: 0,
                            max: 100,
                            title: { display: true, text: 'Score (%)' },
                            grid: { color: '#e5e7eb' }
                        },
                        x: {
                            title: { display: false },
                            grid: { color: '#f3f4f6' }
                        }
                    }
                }
            });
        });
    }

    // Update loadHistory to calculate averages
    function loadHistory() {
        const history = safeLocalStorageGet('quizHistory');
        const cleanedHistory = cleanupHistory(history);
        if (cleanedHistory.length !== history.length) {
            safeLocalStorageSet('quizHistory', cleanedHistory);
        }

        historyTableBody.innerHTML = '';
        if (cleanedHistory.length === 0) {
            historyTableBody.innerHTML = '<tr><td colspan="6" class="text-center py-4 text-gray-500">No exam history found.</td></tr>';
            // Update analytics panel to zero
            updateHistoryAnalytics(0, 0, 0, 0, 0, 0);
            renderScoreGraph([]);
            return;
        }

        cleanedHistory.forEach(record => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td class="py-2 px-4 border-b text-left font-mono text-xs text-gray-600">${record.seed}</td>
                <td class="py-2 px-4 border-b text-left">${record.date} ${record.time}</td>
                <td class="py-2 px-4 border-b text-left">${record.examType || 'N/A'}</td>
                <td class="py-2 px-4 border-b text-left">${record.score}</td>
                <td class="py-2 px-4 border-b text-left font-bold">${record.percentage}</td>
                <td class="py-2 px-4 border-b text-left">${record.timeTaken}</td>
            `;
            historyTableBody.appendChild(row);
        });

        // Calculate analytics
        let totalExams = cleanedHistory.length;
        let totalPractice = cleanedHistory.filter(r => r.examType === 'Practice').length;
        let totalExam = cleanedHistory.filter(r => r.examType === 'Exam').length;
        // Calculate averages
        let avgPractice = 0, avgExam = 0, avgTotal = 0;
        if (cleanedHistory.length > 0) {
            avgTotal = cleanedHistory.reduce((sum, r) => sum + parseFloat(r.percentage.replace('%', '')), 0) / cleanedHistory.length;
        }
        // Only include practice records with more than 10 questions
        const practiceRecords = cleanedHistory.filter(r => r.examType === 'Practice' && r.questionCount > 10);
        if (practiceRecords.length > 0) {
            avgPractice = practiceRecords.reduce((sum, r) => sum + parseFloat(r.percentage.replace('%', '')), 0) / practiceRecords.length;
        }
        const examRecords = cleanedHistory.filter(r => r.examType === 'Exam');
        if (examRecords.length > 0) {
            avgExam = examRecords.reduce((sum, r) => sum + parseFloat(r.percentage.replace('%', '')), 0) / examRecords.length;
        }
        updateHistoryAnalytics(totalExams, totalPractice, totalExam, avgPractice, avgExam, avgTotal);
        renderScoreGraph(cleanedHistory);
    }

    function updateHistoryAnalytics(total, practice, exam, avgPractice = 0, avgExam = 0, avgTotal = 0) {
        const totalEl = document.getElementById('total-exams');
        const practiceEl = document.getElementById('total-practice');
        const examEl = document.getElementById('total-exam');
        const avgTotalEl = document.getElementById('avg-total');
        const avgPracticeEl = document.getElementById('avg-practice');
        const avgExamEl = document.getElementById('avg-exam');
        if (totalEl) totalEl.textContent = total;
        if (practiceEl) practiceEl.textContent = practice;
        if (examEl) examEl.textContent = exam;
        if (avgTotalEl) avgTotalEl.textContent = isNaN(avgTotal) ? '0%' : avgTotal.toFixed(1) + '%';
        if (avgPracticeEl) avgPracticeEl.textContent = isNaN(avgPractice) ? '0%' : avgPractice.toFixed(1) + '%';
        if (avgExamEl) avgExamEl.textContent = isNaN(avgExam) ? '0%' : avgExam.toFixed(1) + '%';
    }

    function downloadData(data, filename, type) {
        try {
            const history = JSON.parse(data);
            if (history.length === 0) {
                // Changed alert to console error as per guidelines
                console.error("No history to download.");
                return;
            }
            let processedData;

            if (type === 'text/csv') {
                const escapeCSV = (str) => {
                    if (str === null || str === undefined) return '';
                    str = String(str);
                    if (/[",\n\r]/.test(str)) {
                        return `"${str.replace(/"/g, '""')}"`;
                    }
                    return str;
                };

                const headers = Object.keys(history[0]).filter(key => key !== 'timestamp').join(',');
                const rows = history.map(record => {
                    return Object.keys(history[0])
                        .filter(key => key !== 'timestamp')
                        .map(key => escapeCSV(record[key]))
                        .join(',');
                });
                processedData = `${headers}\n${rows.join('\n')}`;
            } else {
                processedData = JSON.stringify(history, null, 2);
            }

            const blob = new Blob([processedData], {
                type
            });
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
            // Changed alert to console error as per guidelines
            console.error('There was an error preparing the download. Please try again.');
        }
    }

    function showSupportModal(startAfter = true) {
        supportModal.classList.remove('hidden');
        skipSupportBtn.textContent = startAfter ? 'Skip to Exam' : 'Close';
        skipSupportBtn.onclick = () => {
            supportModal.classList.add('hidden');
            if (startAfter) beginExam();
        };
    }

    // FIX & UX Improvement: Better seed validation and user feedback
    function handleSeedInput() {
        const seedValue = seedInput.value.trim();
        seedInput.setCustomValidity(''); // Clear previous custom errors

        if (!seedValue) {
            resetSeedState();
            return;
        }

        const history = safeLocalStorageGet('quizHistory');
        const seedRecord = history.find(r => r.seed === seedValue);

        if (!seedRecord) {
            resetSeedState(false);
            seedInput.classList.add('border-red-500');
            seedInput.setCustomValidity('Seed not found in your exam history.');
            return;
        }

        // Validate if the domain and question count are still valid
        const availableQuestions = seedRecord.domain === 'all'
            ? allQuestions
            : allQuestions.filter(q => q.domain === seedRecord.domain);
        
        if (availableQuestions.length < seedRecord.questionCount) {
             resetSeedState(false);
             seedInput.classList.add('border-red-500');
             seedInput.setCustomValidity(`This seed requires ${seedRecord.questionCount} questions for the '${seedRecord.domain}' domain, but only ${availableQuestions.length} are now available.`);
             return;
        }

        // If valid, set the state
        activeSeed = seedValue;
        domainSelect.value = seedRecord.domain;
        updateQuestionCountOptions();
        questionCountSelect.value = seedRecord.questionCount;
        domainSelect.disabled = true;
        questionCountSelect.disabled = true;
        seedInput.classList.add('border-green-500');
        seedInput.classList.remove('border-red-500');
    }

    function resetSeedState(clearInput = true) {
        activeSeed = '';
        domainSelect.disabled = false;
        questionCountSelect.disabled = false;
        if (clearInput) seedInput.value = '';
        seedInput.classList.remove('border-green-500', 'border-red-500');
        seedInput.setCustomValidity('');
    }

    // --- EVENT LISTENERS ---
    domainSelect.addEventListener('change', updateQuestionCountOptions);
    seedInput.addEventListener('input', debounce(handleSeedInput, DEBOUNCE_DELAY));
    startExamBtn.addEventListener('click', () => showSupportModal(true));
    restartExamBtn.addEventListener('click', () => {
        resultsSection.classList.add('hidden');
        setupSection.classList.remove('hidden');
        resetSeedState();
    });

    prevQuestionBtn.addEventListener('click', () => {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            displayQuestion();
        }
    });
    nextQuestionBtn.addEventListener('click', () => {
        if (currentQuestionIndex < currentQuestions.length - 1) {
            currentQuestionIndex++;
            displayQuestion();
        }
    });
    submitExamBtn.addEventListener('click', submitExam);
    questionContainer.addEventListener('click', (e) => {
        const optionButton = e.target.closest('.quiz-option');
        if (optionButton) handleOptionSelect(optionButton);
    });

    reviewExamBtn.addEventListener('click', startReview);
    prevReviewBtn.addEventListener('click', () => {
        if (reviewQuestionIndex > 0) reviewQuestionIndex--;
        displayReviewQuestion();
    });
    nextReviewBtn.addEventListener('click', () => {
        if (reviewQuestionIndex < currentQuestions.length - 1) reviewQuestionIndex++;
        displayReviewQuestion();
    });
    backToResultsBtn.addEventListener('click', () => {
        reviewSection.classList.add('hidden');
        resultsSection.classList.remove('hidden');
    });

    resetHistoryBtn.addEventListener('click', () => resetModal.classList.remove('hidden'));
    cancelResetBtn.addEventListener('click', () => resetModal.classList.add('hidden'));
    confirmResetBtn.addEventListener('click', () => {
        localStorage.removeItem('quizHistory');
        loadHistory();
        resetModal.classList.add('hidden');
    });
    downloadJsonBtn.addEventListener('click', () => downloadData(localStorage.getItem('quizHistory') || '[]', 'quiz_history.json', 'application/json'));
    downloadCsvBtn.addEventListener('click', () => downloadData(localStorage.getItem('quizHistory') || '[]', 'quiz_history.csv', 'text/csv'));

    // UX Improvement: More specific warning message
    window.addEventListener('beforeunload', (e) => {
        if (isQuizActive) {
            const confirmationMessage = 'Are you sure you want to leave? Your exam progress will be lost.';
            e.returnValue = confirmationMessage;
            return confirmationMessage;
        }
    });
    document.addEventListener('keydown', (e) => {
        if (!isQuizActive) return;
        if (e.key === 'ArrowRight' && !nextQuestionBtn.disabled) nextQuestionBtn.click();
        if (e.key === 'ArrowLeft' && !prevQuestionBtn.disabled) prevQuestionBtn.click();
    });

    // Add this after the existing event listeners
    examTypeSelect.addEventListener('change', () => {
        if (examTypeSelect.value === 'exam') {
            // Set domain to "All Domains" and disable it
            domainSelect.value = 'all';
            domainSelect.disabled = true;
            
            // Set questions to 90 and disable it
            questionCountSelect.value = '90';
            questionCountSelect.disabled = true;
            
            // Update the question count options
            updateQuestionCountOptions();
        } else {
            // Enable both dropdowns in practice mode
            domainSelect.disabled = false;
            questionCountSelect.disabled = false;
            
            // Update the question count options
            updateQuestionCountOptions();
        }
    });

    // --- ANALYTICS TOGGLE ---
    if (toggleAnalyticsBtn && analyticsSection) {
        toggleAnalyticsBtn.addEventListener('click', () => {
            if (analyticsSection.style.display === 'none') {
                analyticsSection.style.display = '';
                toggleAnalyticsBtn.textContent = 'Hide Analytics';
            } else {
                analyticsSection.style.display = 'none';
                toggleAnalyticsBtn.textContent = 'Show Analytics';
            }
        });
    }

    // --- INITIALIZATION ---
    loadQuestions();
    loadHistory();
});
