from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['language']
        if text_to_translate and target_language:
            try:
                translated_text = GoogleTranslator(target=target_language).translate(text_to_translate)
            except Exception as e:
                translated_text = "Error: Unable to translate. Please try again."
                print(f"Error: {e}")
    return render_template('index.html', translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
