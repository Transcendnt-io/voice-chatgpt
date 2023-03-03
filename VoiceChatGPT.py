import openai

import os
import speech_recognition as sr
import pyttsx3

openai.api_key = "API_KEY"

# Set up text-to-speech engine
engine = pyttsx3.init()
messages = []

system_msg = input("Start")
messages.append({"role": "system", "content": system_msg})
# Create a function to transcribe speech and call OpenAI API
engine.setProperty('voice', 'english-US')
engine.say('What the fuck do you need now?')
engine.runAndWait()
def process_speech():
    while input != "quit()":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now!")
            audio = r.listen(source)
        message = r.recognize_google(audio, language='en-US')
        
        messages.append({"role": "user", "content": message})
        response =  openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
            )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})    
        print("\n" + reply + "\n")
        # Speak the response aloud
        engine.setProperty('voice', 'english-US')
        engine.say(reply)
        engine.runAndWait()
# Call the function to start listening for speech
while True:
    process_speech()

