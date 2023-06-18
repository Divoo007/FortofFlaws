from gtts import gTTS
import os
from playsound import playsound

def texttospeech(answerr):
    language = 'en'
    myobj = gTTS(text=answerr, lang=language)
    myobj.save("somename.mp3")
    playsound('somename.mp3')

