# VOICE TO GPT WITH API


Voice-to-GPT is a web application that allows users to interact with an AI assistant using voice commands. The application records users' voice input, transcribes it, and sends the transcribed text to OpenAI's GPT-4 for processing. The AI assistant responds with an answer, which is then converted back to speech and played to the user. this version is faster than https://github.com/mkdev-me/voice-to-gpt because use whisper API instead of the free code. But it is not cheap



https://user-images.githubusercontent.com/13846927/228222749-6261031a-6a4e-449c-9f3d-92df19eff05b.mp4




## **functionalities:**

* Voice input: Users can speak their questions or commands directly into their microphone.
* Automatic speech recognition (ASR): The application transcribes users' voice input using Whisper ASR.
* AI assistant: The transcribed text is sent to OpenAI's GPT-4, which processes the input and generates an appropriate response.
* Text-to-speech (TTS): The AI assistant's response is converted back to speech and played to the user.
* Please follow the instructions in the "Installation" section to set up and run the application.

## Installation

remember to add the GPT API key in you env first

export  OPENAI_API_KEY=......


You only need to say what you want to ask the GPT API.

To compile the image you need to do 

 docker build -t audio-to-gpt .  

and to execute 

docker run -p 5001:5000 -e OPENAI_API_KEY=$OPENAI_API_KEY audio-to-gpt  

and after that open your browser in

https://127.0.0.1:5001

and enjoy


Remember that depends of your computer, lambda, cloud run, etc resources spead will be different


## Usage


1. Open the application in a web browser.
2. Click the "Record" button and speak your question or command into the microphone.
3. Click the "Stop" button when you're done speaking.
4. The application will transcribe your speech, send the text to GPT-4, and play the AI assistant's response.


## Dependencies

Flask

Flask-CORS

OpenAI

Whisper


## Contributing

If you'd like to contribute to this project, please submit a pull request with your proposed changes. Be sure to provide a clear description of the changes and any relevant information.

## License

This project is licensed under the MIT License. Please refer to the LICENSE file for more information.
