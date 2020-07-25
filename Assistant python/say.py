from gtts import gTTS 
import os  
mytext = 'Say'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("say.mp3") 
os.system("say.mp3") 