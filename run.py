# -*- encoding: utf-8 -*-

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from flask import Flask, request
import chatbot



# Instantiates a client
client = speech.SpeechClient()


config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='vi')



app = Flask(__name__)


@app.route('/get_stt', methods = ['POST'])
def get_content():
    audio_content = request.files['file']
    audio = types.RecognitionAudio(content=audio_content.read())
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    questions = []
    for result in response.results:
        questions.append(unicode(result.alternatives[0].transcript))
    return chatbot.get_response(u'\n'.join(questions))



if __name__ == '__main__':
    app.run('0.0.0.0', port=11119)