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
