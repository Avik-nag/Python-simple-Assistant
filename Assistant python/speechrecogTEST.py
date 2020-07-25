import speech_recognition as sr
import sounddevice as sd
#import scipy.io.wavfile
import wavio
import simpleaudio
from gtts import gTTS 
import os
#import webbrowser
from playsound import playsound
#from googlesearch import search

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

print("Started recording")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait() 
print("Stop recording")
wavio.write("outputtest.wav", myrecording, fs ,sampwidth=2)
print("output file written to disk")
r = sr.Recognizer()
output = sr.AudioFile("D:\VS_Code workspace\p1\outputtest.wav")
with output as source:
    try:
        audio = r.record(source)
        command=(r.recognize_google(audio))
        print(r.recognize_google(audio))
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError: 
        print("Could not request results from Google")

with open('c.txt' , 'w') as mycommand:  #writing the command to c.txt file
    mycommand.write(command)
mycommand.close
        
with open('c.txt' , 'r') as mycommand:     #reading the file and storing to string = line
    line=mycommand.readline()
    line.lower()
mycommand.close
#playsound("D:\VS_Code workspace\p1\outputtest.wav")
#commands dictionary
mycommands ={}  #{"play songs":[0,1,3,4,5] , "open Google":9 , "what is":8}
mycommands[1]=[("play songs","play music")]
mycommands[2]=[7,8,9,0]
if line in mycommands.values():
    print('true')
else:
    print('false')

    