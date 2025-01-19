from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        original_text = request.form['text']
        target_language = request.form['language']
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(original_text)
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
