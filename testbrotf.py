
from gtts import gTTS
import os
name = str(input())
mytext = str(input())
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(name + ".mp3")
os.system("mpg321 welcome.mp3")