⭐ Chintu – AI Voice Assistant (Python)

A fully functional voice assistant built using Python, OpenAI GPT-4o, Speech Recognition, and gTTS.
Chintu listens to your voice, responds with natural AI speech, opens apps, answers questions, and performs smart tasks.


🚀 Features

✔️ Wake-word activation — just say "Chintu"
✔️ Listens using Microphone
✔️ Converts voice → text using Whisper (gpt-4o-transcribe)
✔️ Speaks naturally using gTTS
✔️ Uses GPT-4o-mini to answer any question
✔️ Opens Google, YouTube, Notepad, Music folder
✔️ Tells time and date
✔️ Runs continuously just like JARVIS


🎧 How It Works

1. Chintu always listens for the word “chintu”

2. After hearing it, he replies:
"Yes sir, how can I help?"

3. He listens again for your command

4. Based on command, he:

Opens websites
Opens apps
Tells date/time
Plays music
Or sends your question to GPT-4o


📦 Installation

1️⃣ Clone the repository

git clone https://github.com/GulamMohsin/Chatbot.git
cd Chatbot

2️⃣ Install required libraries

pip install -r requirements.txt

3️⃣ Create .env file

OPENAI_API_KEY=your_api_key_here

4️⃣ Run the assistant

python chintu.py


🧠 Technologies Used

Python

OpenAI GPT-4o mini

Whisper Transcription

gTTS

SpeechRecognition

playsound

datetime

webbrowser

dotenv


🗂️ Project Structure

Chatbot/
│-- chintu.py
│-- requirements.txt
│-- README.md
│-- .env


🗣️ Wake Word

To activate Chintu, simply say:

➡️ “Chintu”

Example:

> “Chintu, open Google.”
> “Chintu, what time is it?”
> “Chintu, who is the president of India?”


👨‍💻 Author

Gulam Mohsin
Voice assistant created using Python + OpenAI API.
