let isRecording = false;
let mediaRecorder;
let audioChunks = [];
const recordButton = document.getElementById('recordButton');
const statusElement = document.getElementById('status');
const responseElement = document.getElementById('response');

recordButton.addEventListener('click', async () => {
    if (!isRecording) {
        isRecording = true;
        recordButton.innerText = 'Stop Recording';
        await startRecording();
    } else {
        isRecording = false;
        recordButton.innerText = 'Start Recording';
        await stopRecording();
    }
});

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.addEventListener('dataavailable', (event) => {
        audioChunks.push(event.data);
    });
    mediaRecorder.start();
    statusElement.textContent = 'Recording...';
}

function stopRecording() {
    return new Promise(resolve => {
        mediaRecorder.addEventListener('stop', async () => {
            statusElement.textContent = 'Recording stopped.';
            const audioBlob = new Blob(audioChunks);
            audioChunks = [];
            const formData = new FormData();
            formData.append('audio', audioBlob);

            const response = await fetch('/transcribe', {
                method: 'POST',
                body: formData,
            });

            const { transcription, answer } = await response.json();

            responseElement.textContent = 'Server response: ' + transcription;
            speak(answer);
            resolve();
        });

        mediaRecorder.stop();
    });
}


function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}

