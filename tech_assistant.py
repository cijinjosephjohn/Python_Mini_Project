import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime

l = sr.Recognizer()
eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice',voices[1].id)


def talk(text):
    print(text)
    eng.say(text)
    eng.runAndWait()

def alexa_talking():
    try:
        with sr.Microphone() as source:
            print("listening......")
            audio = l.listen(source)
            cmd = l.recognize_google(audio)
            cmd =cmd.lower()
            print(cmd)
    except:
        pass
    return cmd

if __name__=="__main__":
    command = alexa_talking()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I : %M : %S %p')
        print(time)
        talk('current time is '+time)
    elif 'schedule' in command:
        talk("you haven't scheduled any meeting")
        talk("Do you want to schedule any")
        ans=alexa_talking()
        if 'yes' in ans:
            talk("You're not fomated to that end")
        elif 'no' in ans:
            talk("Thank you have a wonderful day")
        else:
            talk("Sorry I didn't get you")
    else:
        talk("I'm not updated to that extend")
        talk("wish I will provide better experience next time")
        
