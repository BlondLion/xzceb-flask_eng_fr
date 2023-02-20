from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_transl = translator.english_to_french(textToTranslate)
    return french_transl

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    eng_transl = translator.french_to_english(textToTranslate)
    return eng_transl

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
