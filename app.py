from flask import Flask, render_template, request
from translate import Translator  # Ensure this package is installed, or use googletrans instead.

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        # Get the text and target language from the form
        original_text = request.form['text']
        target_language = request.form['language']
        
        try:
            # Initialize the translator and translate the text
            translator = Translator(to_lang=target_language)
            translated_text = translator.translate(original_text)
        except Exception as e:
            # Handle translation errors
            translated_text = f"Error: {str(e)}"

    # Render the HTML template with the translated text
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
