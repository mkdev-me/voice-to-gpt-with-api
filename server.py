import os
import base64
import tempfile
from audio_processing import transcribe_audio, ask_gpt, text_to_speech
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import tempfile
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
from werkzeug.utils import secure_filename
app = Flask(__name__, static_folder="static", static_url_path="/")

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = {'wav'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return upload()
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Call the process_audio function
        response_text = process_audio()

        return jsonify({'result': response_text})



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if request.method == 'POST':
        audio_file = request.files.get('audio')
        if audio_file is not None:
            # Crea un archivo temporal para guardar el audio recibido
            with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp:
                audio_file.save(temp.name)
                temp.flush()

                # Transcribe el archivo de audio
                transcription = transcribe_audio(temp.name)

                # Elimina el archivo temporal
                os.unlink(temp.name)

                # Consulta a GPT con la transcripción
                answer = ask_gpt(transcription)

                # Convierte la respuesta del asistente a audio
                output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'response.mp3')
                text_to_speech(answer, output_file)

                # Devuelve la respuesta del GPT y los datos de audio en base64
                with open(output_file, "rb") as f:
                    audio_data = base64.b64encode(f.read()).decode('utf-8')
                
                return jsonify({'transcription': transcription, 'answer': answer, 'audio_data': audio_data})

        return jsonify({'error': 'No audio file received'})

if __name__ == '__main__':
    app.run(debug=True)

