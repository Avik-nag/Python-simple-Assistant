from gtts import gTTS 
import os  
mytext = 'Hey, what\'s your name?'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("test.mp3") 
os.system("test.mp3") 