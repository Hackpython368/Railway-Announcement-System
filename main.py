import pyttsx3
import os
import playsound

def textTospeech(*text):
    engine = pyttsx3.init()
    engine.setProperty("rate",105)
    engine.setProperty("voice",0)
    engine.say(text[0])
    engine.runAndWait()

    print(text)

if __name__=="__main__":
    textTospeech("platform")