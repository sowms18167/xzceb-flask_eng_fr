from machinetranslation import translator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text= translator.english_to_french(textToTranslate) # function from the translator
    return french_text # from the translator

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text= translator.french_to_english(textToTranslate) # function from the translator
    return english_text # from the translator

@app.route("/")
def renderIndexPage():
    return render_template('index.html') # my kod

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
