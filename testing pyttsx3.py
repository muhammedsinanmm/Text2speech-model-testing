import pyttsx3
engine = pyttsx3.init()

engine.setProperty('volume',0.8)
engine.setProperty('rate',150)

voices = engine.getProperty('voices')

for v in voices:
    print(v.id)

engine.setProperty('voice', voices[2].id)  

engine.say("This is a different voice with custom speed and volume.")
engine.runAndWait()