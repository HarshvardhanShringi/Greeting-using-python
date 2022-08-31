import pyttsx3 as pyt
import datetime
import subprocess as sbps
engine=pyt.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# SPEAK FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# TIME FUNCTION
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


# WISHING BASED ON TIME
def hour():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir")
    if hour >= 12 and hour < 18:
        speak("good afternoon sir")
    if hour >= 18 and hour < 24:
        speak("good evening sir")
# OPENING AN APP
def open():
    a=input("Application name :")
    if(a=="Notepad"):
        sbps.Popen('C:\\WINDOWS\\system32\\notepad')
    if(a=="Word"):
        sbps.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD')
    if(a=="Ppt"):
        sbps.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT')
    if(a=="Xl"):
        sbps.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEl')
    if(a=="Chrome"):
        sbps.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome')
    if(a=="n"):
        exit()

hour()
open()
