from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

app = Flask(__name__)

# Cargar configuración
load_dotenv()
translatorRegion = os.getenv('TRANSLATOR_REGION')
translatorKey = os.getenv('TRANSLATOR_KEY')

# Crear el cliente de traducción
credential = TranslatorCredential(translatorKey, translatorRegion)
client = TextTranslationClient(credential)

# Ruta para servir el archivo HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        # Obtener texto e idioma de destino del cuerpo de la solicitud
        data = request.json
        input_text = data['text']
        target_language = data['target_language']

        # Crear el elemento de texto y traducir
        input_text_elements = [InputTextItem(text=input_text)]
        translation_response = client.translate(content=input_text_elements, to=[target_language])
        translation = translation_response[0] if translation_response else None

        if translation:
            source_language = translation.detected_language.language
            translated_text = translation.translations[0].text
            return jsonify({
                'source_language': source_language,
                'translated_text': translated_text
            })
        else:
            return jsonify({'error': 'Translation failed'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

if __name__ == '__main__':
    app.run(debug=True)
