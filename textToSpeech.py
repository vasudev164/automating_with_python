import pyperclip
import pyttsx3

text = ' '.join(pyperclip.paste().split('\r\n'))
#print(pyperclip.paste())
#print(pyperclip.paste().split('\r'))

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 2.0)
engine.say(text)
engine.runAndWait()
