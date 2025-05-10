document.addEventListener('DOMContentLoaded', () => {
    const cardForm = document.getElementById('cardForm');
    const generatedLinkInput = document.getElementById('generatedLink');
    const shareLinkSection = document.getElementById('share-link-section');
    const copyLinkButton = document.getElementById('copyLinkButton');
    const previewLink = document.getElementById('previewLink');
    const templateOptions = document.querySelectorAll('.template-option');
    const selectedTemplateInput = document.getElementById('selectedTemplate');

    // Template selection logic
    templateOptions.forEach(option => {
        option.addEventListener('click', () => {
            templateOptions.forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            selectedTemplateInput.value = option.dataset.template;
        });
    });
    // Select default template visually
    document.querySelector(`.template-option[data-template="${selectedTemplateInput.value}"]`).classList.add('selected');


    cardForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const recipientName = document.getElementById('recipientName').value;
        const message = document.getElementById('message').value;
        const senderName = document.getElementById('senderName').value;
        const template = selectedTemplateInput.value;

        // Construct the URL for card.html
        // For local development, this will be a file path. For a deployed app, it'll be an HTTP URL.
        const baseUrl = window.location.origin + window.location.pathname.replace('index.html', '');
        const cardUrl = new URL(`${baseUrl}card.html`);

        cardUrl.searchParams.append('to', recipientName);
        cardUrl.searchParams.append('msg', message);
        cardUrl.searchParams.append('from', senderName);
        cardUrl.searchParams.append('template', template);

        generatedLinkInput.value = cardUrl.toString();
        previewLink.href = cardUrl.toString();
        shareLinkSection.style.display = 'block';

        // Scroll to the link section smoothly
        shareLinkSection.scrollIntoView({ behavior: 'smooth' });
    });

    copyLinkButton.addEventListener('click', () => {
        generatedLinkInput.select();
        generatedLinkInput.setSelectionRange(0, 99999); // For mobile devices

        try {
            document.execCommand('copy');
            copyLinkButton.textContent = 'Copied!';
            setTimeout(() => {
                copyLinkButton.textContent = 'Copy';
            }, 2000);
        } catch (err) {
            alert('Oops, unable to copy. Please copy manually.');
        }
    });
});