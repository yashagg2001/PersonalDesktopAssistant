import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
webbrowser.register('google-chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
chrome_browser=webbrowser.get('google-chrome')
import os
import smtplib
import pywhatkit
import requests
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")   

    elif hour>=18 and hour<21:
        speak("Good Evening sir")  
    else:
        speak("Hello sir")

    speak("I am Robo, your personal assistant. How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...") 
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break        

        elif 'open youtube' in query:
            speak('opening youtube')
            chrome_browser.open("youtube.com")
            break

        elif 'open google' in query:
            speak('opening google')
            chrome_browser.open("google.com")
            break

        elif 'open downloads' in query:
            downloads_dir = 'C:\\Users\\yashg\\Downloads'
            speak("opening downloads")
            os.startfile(downloads_dir)
            break

        elif 'on youtube' in query:
            x=len(query)
            query = query.replace("on youtube", "")
            query =query.replace("play","")
            speak(f'playing {query} on youtube')
            pywhatkit.playonyt(f"{query}")
            print("Playing...")
            break

        elif 'search' in query:
            query = query.replace("search", "")
            speak(f'searching {query} on google')
            pywhatkit.search(f"{query}")
            print("Searching...")
            break
        
        elif 'open music' in query or 'start music' in query or 'play music' in query or 'gana sunao' in query:
            music_dir='C:\\Users\\yashg\\Desktop\\Music\\aankhon me teri'
            songs = os.listdir(music_dir)   
            speak('playing aankhon me teri')
            os.startfile(os.path.join(music_dir, songs[0]))
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            break

        elif 'open code' in query:
            codePath = "C:\\Users\\yashg\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('opening visual studio code')
            os.startfile(codePath)
            break

        elif 'send email to yash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashkiemail@gmail.com" 
                speak('sending email...')   
                sendEmail(to, content)
                speak("Email has been sent!")
                break

            except Exception as e:
                print(e)
                speak("Sorry sir, I am unable to send the email")    
        
        elif "weather" in query or "temperature" in query or "humidity" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in degree celsius is " + str("%.2f"%(current_temperature-273.15)) + "\n humidity in percentage is " +str(current_humidiy) +"\n description  " +str(weather_description))
                print(" Temperature in degree celsius = " + str("%.2f"%(current_temperature-273.15)) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " + str(weather_description))
                break

            else:
                speak(" sorry, city not found ")
                break
        
        elif 'news' in query:
            news = webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India, Happy reading')
            break

        elif 'ask' in query or 'question' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now ?')
            print('I can answer to computational and geographical questions and what question do you want to ask now ?')
            question=takeCommand()
            app_id="2L22GX-L9JP4PTPPE"
            client = wolframalpha.Client('2L22GX-L9JP4PTPPE')
            res = client.query(question)
            answer = next(res.results).text
            print(f'Answer to your question is {answer}')
            speak(f'Answer to your question is {answer}')
            

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Robo, your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google,predict time,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
            break


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Yash Aggarwal")
            print("I was built by Yash Aggarwal")
            break

        elif "your father" in query or "your owner" in query or "your boss" in query or "your creator" in query:
            speak("Mr. Yash Aggarwal created me. He is currently persuing his B.Tech from IIT Mandi. He is very much interested in latest and new technologies. ")
            break
        
        elif 'thank you robo' in query or 'thank you' in query:
            speak('No problem sir, I am always there to help you')
            break

        elif 'exit' in query or 'stop' in query or 'quit' in query or 'nothing' in query or 'bye' in query:
            speak('Okay sir...take care')
            break
        elif 'none' in query:
            continue

        else:
            print("sorry, I couldn't understand. Try again") 
            speak("sorry, I couldn't understand. Try again") 
