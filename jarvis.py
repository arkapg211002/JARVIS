#Arkapratim Ghosh
#Techno Main Saltlake
#8-10-2021
#https://www.linkedin.com/in/arkapratimghosh10sep2021/

import pyttsx3#module
import speech_recognition as sr#module installed for taking command
import datetime#time module
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

engine=pyttsx3.init('sapi5')#speak api from microsoft
voices=engine.getProperty('voices')
#print(voices[0].id)#list of voices present
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)#function to set speaking
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour<=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("sir i am jarvis. please tell me how i may help u")

def command():
    '''take command from user through microphone and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)#587 is the server port
    server.ehlo()
    server.starttls()
    server.login('your email  id@gmail.com','your email password')
    server.sendmail('your email id@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    #speak("Hello i am jarvis. how may i help u?")
    wishme()
    while True:
      query=command().lower()
      #logic for executing tasks based  on query
      if 'wikipedia' in query:
          speak("searching wikipedia...")
          query=query.replace("wikipedia", "")
          results=wikipedia.summary(query, sentences=2)
          speak("according to wikipedia")
          print(results)
          speak(results)
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'open google' in query:
          webbrowser.open("google.com")
      elif 'open codechef' in query:
          webbrowser.open("codechef.com")

      elif 'open spotify' in query:
          webbrowser.open("https://open.spotify.com/")
      elif 'open codeforces' in query:
          webbrowser.open("codeforces.com")
      elif 'open stack overflow' in query:
          webbrowser.open("stackoverflow.com")
      elif 'open github' in query:
          webbrowser.open("https://education.github.com/pack/gallery")
      elif 'open hackerearth' in query:
          webbrowser.open("https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/")



      elif 'play music' in query:
          music_dir='D:\\OneDrive\\Desktop\\New folder'
          songs=os.listdir(music_dir)
          print(songs)
          #random.randrange(1,1000,1)
          os.startfile(os.path.join(music_dir,songs[0]))
      elif ' time' in query:
          strtime=datetime.datetime.now().strftime("%H:%M:%S")
          print(strtime)
          speak(f"Sir the time is {strtime}\n")
      elif 'open code' in query:
          codepath="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)


      elif 'open pycharm' in query:
          codepy="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
          os.startfile(codepy)
      elif 'open java' in query:
          codej="D:\\IdeaIntelliJ\\IntelliJ IDEA Community Edition 2021.2.2\\bin\\idea64.exe"
          os.startfile(codej)
      elif 'open powershell' in query:
          codeq="%SystemRoot%\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe"
          os.startfile(codeq)
      elif 'open cmd' in query:
          codec="%windir%\\system32\\cmd.exe"
          os.startfile(codec)

      elif 'quit' in query:
          speak("Bye sir")
          exit()
      elif 'send email' in query:
          try:
              speak("what should i say")
              content=command()
              to="receiver email id@gmail.com"
              sendEmail(to,content)
              speak("email has been sent")
          except Exception as e:
              print(e)
              speak("sorry sir this email can not be send")





