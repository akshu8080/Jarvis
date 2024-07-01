import os
import subprocess
from urllib.request import urlopen
from googlesearch import search
import webbrowser
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import random
import smtplib
import pyjokes
import wolframalpha
import json
import winshell
import time

def listen_for_recipient_name():#for sending email
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        name = recognizer.recognize_google(audio,).lower()
        return name
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, I could not request results. Please check your internet connection.")
        return None


recipients={<key value pairs of email id's with associated name>}

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning..." )
    elif hour>=12 and hour<18:
        speak("good Afternoon..")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir, how may I help you")


def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','email password(rrvv uucc oopp)')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    #speak("akshay is good boy ")
    wishMe()
    while True:
     query = takeCommand().lower()
     #logic for executing task based on query
     if 'wikipedia' in query :
         speak('Searching Wikipedia....')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=3)# for how many sentences it reads 
         speak("According to Wikipedia")
         print(results)
         speak(results)
         
     elif 'open youtube' in query:
        print("Opening you tube.....")
        webbrowser.open("https://www.youtube.com")

     elif 'open google' in query:
        print("Opening Google.....")
        webbrowser.open("https://www.google.com")

     elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
        

     elif 'play music' in query:
        print("Playing music.....")
        music_dir = "C:\\Users\\hp\\Music\\favmusic"
        songs = os.listdir(music_dir)
        print(songs)
        mus=random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir,songs[mus]))

     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")

     elif 'open code' in query:
         codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

     elif 'open browser' in query:
          bwsrPath = "C:\\Users\\hp\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"           
          os.startfile(bwsrPath)

     elif 'open powerpoint' in query:
         powerPath =  "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
         os.startfile(powerPath)
     
     elif 'open word' in query:
        wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(wordPath)
         
     elif 'open amazon' in query:
          print("Opening Amazon......")
          webbrowser.open("http://www.amazon.com/gp/ubp/oneButton/config/redirectHome?tagbase=hpga1-ubpl&ref=aagateway-taskbar-hp")
     
     elif 'open zomato' in query:
          print("Opening Zomato......")
          webbrowser.open("http://www.zomato.com")

     elif 'open instagram' in query:
          print("Opening instagram......")
          webbrowser.open("http://www.instagram.com")
     
         
     elif 'open microsoft store' in query:
          
          command = "start ms-windows-store://"
          os.system(command)

     elif 'open sql workbench' in query:
        workPath =  "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
        os.startfile(workPath)

     elif 'open camera' in query:
           camCommand= "start microsoft.windows.camera:"
           os.system(camCommand)
     
     

     elif 'send email' in query:
        
        try:
               speak("whom to send ")
               to=listen_for_recipient_name()
               if to in recipients:
                   
                speak("what message you want to send")
                content=listen_for_recipient_name() 
                print("Prossecing....")
             
                sendEmail(recipients[to],content)
                speak(f"Email has been send to {to} on {recipients[to]}")
            
                 
        except Exception as e:
            print(e)
            speak("Sorry Sir, I am not able to send this email")


     elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
     elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

     elif "calculate" in query: 
        try:
            app_id =  "TL78HH-5H3UKGV6KP"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 
        except Exception as e:
            print(e)
        
     elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")
            query = query.replace("jarvis","")
            speak(f"Searching {query} Sir")          
            webbrowser.open(query) 


     elif 'news' in query:
      try: 
        jsonObj = urlopen("https://newsapi.org/v2/everything?q=tesla&from=2024-03-03&sortBy=publishedAt&apiKey=cabdf3dcdba1497cb3a809e4763809ad")
        data = json.load(jsonObj)
        i = 1
         
        speak('Here are some top news from the Times of India:')
        print('=============== TIMES OF INDIA ============' + '\n')
         
        for item in data['articles']:
            title = item.get('title', 'Unknown Title')
            description = item.get('description', 'No description available')
            
            if title is not None:
                print(str(i) + '. ' + title + '\n')
                speak(str(i) + '. ' + title + '\n')
            if description is not None:
                print(description + '\n')
            
            if i == 5:
                break
            i += 1

      except Exception as e:
            print(str(e))

     elif 'good job' in query:
         speak("Thank you Sir, its my pleasure")

     elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

     elif "where is" in query:
            query = query.replace("where is", "")
            query = query.replace("jarvis", "")

            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in / maps / place /" + location + "") 

     elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            file.write(note)
     elif "show notes" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read())
      
     elif "weather" in query:
      api_key = "eac5145ebddd1e1b681b457bdec35075"  
      base_url = "http://api.openweathermap.org/data/2.5/weather?"
      speak("Please provide the city name.")
      print("City name:")
      city_name = takeCommand()  # Assuming takeCommand() is a function that captures user input
      complete_url = f"{base_url}&appid={api_key}&q={city_name}"  # Construct complete URL

      response = requests.get(complete_url)
      if response.status_code == 200:
        data = response.json()
        if data.get("cod") != "404":  # Check if the city is found
            main_data = data["main"]
            current_temperature = main_data["temp"]
            current_pressure = main_data["pressure"]
            current_humidity = main_data["humidity"]
            weather_data = data["weather"]
            weather_description = weather_data[0]["description"]

            print(f"Temperature: {current_temperature} K")  # Temperature in Kelvin
            print(f"Pressure: {current_pressure} hPa")
            print(f"Humidity: {current_humidity}%")
            print(f"Weather Description: {weather_description}")
            speak(f"The temperature in {city_name} is {current_temperature} Kelvin with {weather_description}. Humidity is {current_humidity} percent.")
        else:
            print("City not found.")
            speak("City not found.")
      else:
        print("Error:", response.status_code)
        speak("Sorry, unable to fetch weather information at the moment.")
 
     elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
     elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
     elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
     
     
     elif "what is" in query or "who is" in query:
             
            # Use the same API key 
            # that we have generated earlier
            query=query.replace("jarvis","")
            client = wolframalpha.Client("TL78HH-5H3UKGV6KP")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
