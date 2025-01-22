document.getElementById('translatorForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const inputText = document.getElementById('inputText').value;
    const targetLanguage = document.getElementById('language').value;

    try {
        // Send translation request to the Flask backend
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText, language: targetLanguage }),
        });

        const result = await response.json();

        if (response.ok) {
            // Display the translated text
            const translatedText = document.getElementById('translatedText');
            translatedText.textContent = result.translated_text;

            const resultSection = document.getElementById('resultSection');
            resultSection.classList.remove('hidden');
        } else {
            // Display error message
            alert(result.error || 'An unknown error occurred.');
        }
    } catch (error) {
        alert('Failed to connect to the translation service. Please check your network and try again.');
        console.error(error);
    }
});
