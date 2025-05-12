<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from langdetect import detect
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Load grammar rules
def load_grammar_rules():
    try:
        with open('data/grammar_rules.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default grammar rules if file doesn't exist
        return {
            'en-es': {
                'title': 'English to Spanish Grammar Tips',
                'tip': 'In Spanish, adjectives typically come after the noun they modify.',
                'examples': [
                    {'source': 'The red car', 'target': 'El coche rojo'},
                    {'source': 'A beautiful house', 'target': 'Una casa hermosa'}
                ]
            },
            'es-en': {
                'title': 'Spanish to English Grammar Tips',
                'tip': 'In English, adjectives typically come before the noun they modify.',
                'examples': [
                    {'source': 'El coche rojo', 'target': 'The red car'},
                    {'source': 'Una casa hermosa', 'target': 'A beautiful house'}
                ]
            }
        }

# Load daily vocabulary
def load_daily_vocabulary():
    try:
        with open('data/daily_vocabulary.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default vocabulary if file doesn't exist
        return {
            'en': {
                'word': 'Serendipity',
                'definition': 'The occurrence of events by chance in a happy or beneficial way.',
                'example': 'Finding this book was pure serendipity.'
            },
            'es': {
                'word': 'Serendipia',
                'definition': 'Hallazgo afortunado e inesperado que se produce cuando se está buscando otra cosa distinta.',
                'example': 'Encontrar este libro fue pura serendipia.'
            }
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        text = request.form.get('text', '')
        source_language = request.form.get('sourceLanguage', 'auto')
        target_language = request.form.get('targetLanguage', 'en')

        # Auto-detect language if source is set to auto
        if source_language == 'auto':
            source_language = detect(text)

        # Perform translation
        translator = GoogleTranslator(source=source_language, target=target_language)
        translation = translator.translate(text)

        # Get grammar tips
        grammar_rules = load_grammar_rules()
        grammar_tips = grammar_rules.get(f'{source_language}-{target_language}', {})

        # Prepare word breakdown
        words = text.split()
        translated_words = translation.split()
        word_breakdown = list(zip(words, translated_words))

        return jsonify({
            'translation': translation,
            'source_language': source_language,
            'target_language': target_language,
            'grammar_tips': grammar_tips,
            'word_breakdown': word_breakdown
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/grammar-tips')
def get_grammar_tips():
    source = request.args.get('source', 'en')
    target = request.args.get('target', 'es')
    
    grammar_rules = load_grammar_rules()
    tips = grammar_rules.get(f'{source}-{target}', {})
    
    if not tips:
        return jsonify({
            'title': 'Grammar Tips',
            'tip': 'Grammar tips not available for this language pair.',
            'examples': []
        })
    
    return jsonify(tips)

@app.route('/daily-vocabulary')
def get_daily_vocabulary():
    vocabulary = load_daily_vocabulary()
    language = request.args.get('language', 'en')
    
    return jsonify(vocabulary.get(language, vocabulary['en']))

@app.route('/practice-text')
def get_practice_text():
    # This would typically come from a database of practice texts
    practice_texts = {
        'en': [
            'The quick brown fox jumps over the lazy dog.',
            'She sells seashells by the seashore.',
            'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
        ],
        'es': [
            'El rápido zorro marrón salta sobre el perro perezoso.',
            'Ella vende conchas marinas junto al mar.',
            '¿Cuánta madera podría roer un roedor si un roedor pudiera roer madera?'
        ]
    }
    
    language = request.args.get('language', 'en')
    texts = practice_texts.get(language, practice_texts['en'])
    
    return jsonify({
        'text': texts[0]  # In a real app, this would be randomized
    })

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Create grammar rules file if it doesn't exist
    if not os.path.exists('data/grammar_rules.json'):
        with open('data/grammar_rules.json', 'w', encoding='utf-8') as f:
            json.dump(load_grammar_rules(), f, ensure_ascii=False, indent=2)
    
    # Create daily vocabulary file if it doesn't exist
    if not os.path.exists('data/daily_vocabulary.json'):
        with open('data/daily_vocabulary.json', 'w', encoding='utf-8') as f:
            json.dump(load_daily_vocabulary(), f, ensure_ascii=False, indent=2)
    
    app.run(debug=True)
=======
from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()  # Get JSON data from the frontend
        text_to_translate = data.get('text')
        target_language = data.get('language')

        if not text_to_translate or not target_language:
            return jsonify({'error': 'Invalid input data.'}), 400

        # Perform translation
        translated_text = GoogleTranslator(target=target_language).translate(text_to_translate)

        return jsonify({'translated_text': translated_text})  # Return JSON response

    except Exception as e:
        return jsonify({'error': f"Translation failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 2f497e4c414f441f646a81876144b59be31ca5fa
