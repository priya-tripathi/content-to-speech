import speech_recognition as sr 
from gtts import *
import os

voice=""


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:               # use the default microphone as the audio source
            audio = r.listen(source)
            text=r.recognize_google(audio)
            print(text)
            if text=='stop':
                break
            text=r.recognize_google(audio)
            voice=voice+str(text)

        except:
            print("Say something")

hr = gTTS(text=voice, lang='en-in', slow=False)
hr.save("1.mp3")