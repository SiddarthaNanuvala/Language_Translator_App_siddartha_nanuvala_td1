<<<<<<< HEAD
// Initialize variables
let currentFlashcardIndex = 0;
let flashcards = [];
let speechRecognition = null;
let practiceTimer = null;
let practiceStartTime = null;
=======
document.getElementById('translatorForm').addEventListener('submit', async function (event) {
    event.preventDefault();
>>>>>>> 2f497e4c414f441f646a81876144b59be31ca5fa

// DOM Elements
const translatorForm = document.getElementById('translatorForm');
const sourceLanguage = document.getElementById('sourceLanguage');
const targetLanguage = document.getElementById('targetLanguage');
const inputText = document.getElementById('inputText');
const translatedText = document.getElementById('translatedText');
const resultSection = document.getElementById('resultSection');
const learningTools = document.getElementById('learningTools');
const practiceSection = document.getElementById('practiceSection');
const progressSection = document.getElementById('progressSection');
const historySection = document.getElementById('historySection');
const themeToggle = document.getElementById('themeToggle');

<<<<<<< HEAD
// Initialize theme
const currentTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', currentTheme);

// Theme toggle functionality
themeToggle.addEventListener('click', () => {
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
});

// Initialize speech recognition if supported
if ('webkitSpeechRecognition' in window) {
    speechRecognition = new webkitSpeechRecognition();
    speechRecognition.continuous = false;
    speechRecognition.interimResults = false;
}

// Handle form submission
translatorForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const text = inputText.value.trim();
    if (!text) {
        showError('Please enter text to translate');
        return;
    }

    try {
        showLoading();
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                text: text,
                sourceLanguage: sourceLanguage.value,
                targetLanguage: targetLanguage.value
            })
        });

        if (!response.ok) {
            throw new Error('Translation failed');
        }

        const data = await response.json();
        displayTranslation(data);
        updateLearningTools(data);
        saveToHistory(text, data.translation);
    } catch (error) {
        showError('Translation failed. Please try again.');
        console.error('Translation error:', error);
    } finally {
        hideLoading();
    }
});

// Display translation result
function displayTranslation(data) {
    resultSection.classList.remove('hidden');
    translatedText.textContent = data.translation;
    
    // Show word breakdown
    const wordBreakdown = document.getElementById('wordBreakdown');
    wordBreakdown.innerHTML = data.word_breakdown.map(([source, target]) => `
        <div class="word-item" onclick="speakWord('${target}')">
            ${source} → ${target}
        </div>
    `).join('');
}

// Update learning tools
function updateLearningTools(data) {
    // Update grammar tips
    const grammarTips = document.getElementById('grammarTips');
    if (data.grammar_tips) {
        grammarTips.innerHTML = `
            <h4>${data.grammar_tips.title || 'Grammar Tips'}</h4>
            <p>${data.grammar_tips.tip}</p>
            <div class="examples">
                ${data.grammar_tips.examples.map(example => `
                    <div class="example-item">
                        <p>${example.source} → ${example.target}</p>
                    </div>
                `).join('')}
            </div>
        `;
    }

    // Generate flashcards
    generateFlashcards(data.word_breakdown);
}

// Generate flashcards
function generateFlashcards(wordBreakdown) {
    flashcards = wordBreakdown.map(([source, target]) => ({
        front: source,
        back: target
    }));
    currentFlashcardIndex = 0;
    updateFlashcard();
}

// Update flashcard display
function updateFlashcard() {
    const flashcard = document.getElementById('flashcard');
    if (flashcards.length > 0) {
        const currentCard = flashcards[currentFlashcardIndex];
        flashcard.innerHTML = `
            <div class="flashcard-front">${currentCard.front}</div>
            <div class="flashcard-back">${currentCard.back}</div>
        `;
    }
}

// Flashcard navigation
function nextCard() {
    if (currentFlashcardIndex < flashcards.length - 1) {
        currentFlashcardIndex++;
        updateFlashcard();
    }
}

function prevCard() {
    if (currentFlashcardIndex > 0) {
        currentFlashcardIndex--;
        updateFlashcard();
    }
}

// Flip flashcard
function flipCard() {
    const flashcard = document.getElementById('flashcard');
    flashcard.classList.toggle('flipped');
}

// Speaking practice
function startSpeakingPractice() {
    if (!speechRecognition) {
        showError('Speech recognition is not supported in your browser');
        return;
    }

    const practiceText = document.getElementById('practiceText').textContent;
    speechRecognition.onresult = (event) => {
        const spoken = event.results[0][0].transcript;
        const accuracy = calculateAccuracy(spoken, practiceText);
        showFeedback(accuracy);
    };

    speechRecognition.start();
}

// Calculate accuracy between spoken and correct text
function calculateAccuracy(spoken, correct) {
    const spokenWords = spoken.toLowerCase().split(' ');
    const correctWords = correct.toLowerCase().split(' ');
    let matches = 0;

    spokenWords.forEach(word => {
        if (correctWords.includes(word)) matches++;
    });

    return (matches / correctWords.length) * 100;
}

// Show feedback
function showFeedback(accuracy) {
    const feedback = document.getElementById('feedback');
    feedback.innerHTML = `
        <div class="feedback-content">
            <h4>Accuracy: ${accuracy.toFixed(1)}%</h4>
            <p>${getFeedbackMessage(accuracy)}</p>
        </div>
    `;
}

// Get feedback message based on accuracy
function getFeedbackMessage(accuracy) {
    if (accuracy >= 90) return 'Excellent! Keep up the good work!';
    if (accuracy >= 70) return 'Good job! Practice makes perfect.';
    if (accuracy >= 50) return 'Not bad! Keep practicing.';
    return 'Keep trying! You can do better.';
}

// Save translation to history
function saveToHistory(source, target) {
    const history = JSON.parse(localStorage.getItem('translationHistory') || '[]');
    history.unshift({
        source,
        target,
        timestamp: new Date().toISOString()
    });
    
    // Keep only last 10 translations
    if (history.length > 10) history.pop();
    
    localStorage.setItem('translationHistory', JSON.stringify(history));
    updateHistoryDisplay();
}

// Update history display
function updateHistoryDisplay() {
    const history = JSON.parse(localStorage.getItem('translationHistory') || '[]');
    const historyList = document.getElementById('historyList');
    
    historyList.innerHTML = history.map(item => `
        <div class="history-item">
            <p class="source">${item.source}</p>
            <p class="target">${item.target}</p>
            <p class="timestamp">${new Date(item.timestamp).toLocaleString()}</p>
        </div>
    `).join('');
}

// Show loading state
function showLoading() {
    const loading = document.createElement('div');
    loading.id = 'loading';
    loading.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(loading);
}

// Hide loading state
function hideLoading() {
    const loading = document.getElementById('loading');
    if (loading) loading.remove();
}

// Show error message
function showError(message) {
    const error = document.createElement('div');
    error.className = 'error-message';
    error.textContent = message;
    document.body.appendChild(error);
    setTimeout(() => error.remove(), 3000);
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    updateHistoryDisplay();
    updateDailyVocabulary();
    updateProgressStats();
=======
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
>>>>>>> 2f497e4c414f441f646a81876144b59be31ca5fa
});
