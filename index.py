import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)

 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour <12):
        speak(f"good morning " )

    elif(hour>=12 and hour<18):
        speak(f"good afternoon")

    else:
        speak(f"good evening")

    speak("i am your voice assistent . How may I help you ?")

def SendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('khushi12kumai34@gmail.com','Khushi12@#')
        server.sendmail('khushi12kumai34@gmail.com',to,content)
        server.close()

def takeCommand():
    # it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said : {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


   





if __name__ =="__main__":
    speak("Hello vikash ")
    wishme()
    while True:
        query = takeCommand().lower()
        #logic for task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'gana bajao' in query:
            music_dir = 'C:\\Users\\vikas\\Music\\Playlists\\music\\Hindi'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[3]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().time()
            speak(f"sir , the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codepath = "C:\\Users\\vikas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "Vvikashpuran@gmail.com"
                SendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                # print(e)
                speak(" sorry! sending unsuccessful")

            
