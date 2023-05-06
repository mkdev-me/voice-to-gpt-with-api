import torch
import openai
import pyaudio
import wave
import time
import openai
import audioop
import os
import subprocess
import requests
from gtts import gTTS

openai.api_key = os.environ.get("OPENAI_API_KEY")
messages = [{"role": "system", "content": "You are a helpful assistant."}]


def transcribe_audio(file):
    file_root, _ = os.path.splitext(file)
    output_file = file_root + ".mp3"
    command = ['ffmpeg', '-i', file, output_file]
    subprocess.run(command, check=True)
    audio_file= open(output_file, "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)

    print(transcript)
    return transcript


def text_to_speech(text, output_file, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)

def ask_gpt(prompt, max_tokens=4000):
    prompt = f"Conversación con un asistente AI:\n{prompt}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}], 
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.2,
    )

    # Extraer la respuesta del modelo
    assistant_message = response.choices[0].message['content']

    # Agregar la respuesta del asistente a la lista de mensajes
    messages.append({"role": "assistant", "content": assistant_message})

    print(assistant_message)

    return assistant_message
