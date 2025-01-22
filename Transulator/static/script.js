document.getElementById('translatorForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const inputText = document.getElementById('inputText').value;
    const targetLanguage = document.getElementById('language').value;

    // Simulate translation (replace this with actual backend API calls)
    const mockTranslation = `Translated version of "${inputText}" to ${targetLanguage}`;

    // Show the result
    const resultSection = document.getElementById('resultSection');
    const translatedText = document.getElementById('translatedText');
    translatedText.textContent = mockTranslation;
    resultSection.classList.remove('hidden');
});

document.getElementById('copyButton').addEventListener('click', function () {
    const translatedText = document.getElementById('translatedText').textContent;

    navigator.clipboard.writeText(translatedText)
        .then(() => alert('Translation copied to clipboard!'))
        .catch(() => alert('Failed to copy. Please try again.'));
});