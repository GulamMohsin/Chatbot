import os
import webbrowser
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from openai import OpenAI

client = OpenAI(api_key="your-actual-key-here")

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": "Hello Chintu!"}
#     ]
# )

# print(response.choices[0].message["content"])

WAKE_WORD = "chintu"   # Wake word

# Speak function
def speak(text):
    print("Chintu:", text)
    tts = gTTS(text=text, lang="en")
    tts.save("chintu_voice.mp3")
    playsound("chintu_voice.mp3")
    os.remove("chintu_voice.mp3")

# Listen function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    # Convert to wav for Whisper
    with open("audio.wav", "wb") as f:
        f.write(audio.get_wav_data())

    # Whisper transcription  
    with open("audio.wav", "rb") as f:
        result = client.audio.transcriptions.create(
            file=f,
            model="gpt-4o-transcribe"
        )

    text = result.text.lower()
    print("You said:", text)
    return text

# GPT reply function
def ask_gpt(query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message["content"]

# CHINTU command handler
def process_command(cmd):
    if "google" in cmd:
        speak("Opening Google sir")
        webbrowser.open("https://google.com")

    elif "youtube" in cmd:
        speak("Opening YouTube sir")
        webbrowser.open("https://youtube.com")

    elif "notepad" in cmd:
        speak("Opening Notepad sir")
        os.system("notepad")

    elif "time" in cmd:
        time = datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "date" in cmd:
        date = datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "play music" in cmd:
        speak("Playing music sir")
        os.startfile("C:\\Users\\Public\\Music")

    else:
        # GPT answer
        reply = ask_gpt(cmd)
        speak(reply)

# MAIN — Wake Word + Assistant Loop
def main():
    speak("Chintu is online. Say my name when you need me.")
    while True:
        try:
            text = listen()

            # Wake word
            if WAKE_WORD in text:
                speak("Yes sir, how can I help?")
                cmd = listen()
                process_command(cmd)

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I didn't get that sir.")

main()