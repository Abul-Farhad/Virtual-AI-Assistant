import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import time
import subprocess
import wolframalpha
import json
import requests
import pywhatkit
#->> Setting up the speech engine:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


#->> runAndWait:
def speak(text):
    engine.say(text)
    engine.runAndWait()


#->> Initiating function to greet the user:
def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print('Good Morning sensei')
        speak('Good Morning sensei')

    elif hour >= 12 and hour < 18:
        print('Good Afternoon sensei')
        speak('Good Afternoon sensei')

    else:
        print('Good Evening sensei')
        speak('Good Evening sensei')



#->> Setting up command function for my AI:
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language = 'en-in')
            print(f'user said:{statement}\n')
        except Exception as e:
            speak('Pardon me, please say that again')
            return 'None'
        return statement
print('Loading your personal AI assistant Genos')
speak('Loading your personal AI assistant Genos')
wishme()

#->> The Main Function:
if __name__ =='__main__':
    while True:
        speak('Tell me how can I help you now?')
        statement = takeCommand().lower()
        if statement == 0:
            continue
        if 'good bye' in statement or 'ok bye' in statement or 'stop' in statement:
            speak('Your personal assistant Genos is shutting downm Good bye')
            break

        #Skill -> 1(Fetching data from Wikipedia)
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace('wikipedia','')
            results = wikipedia.summary(statement,sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        #Skill->2(Accessing the Web Browsers — Google chrome , G-Mail and YouTube)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab('http://www.youtube.com')
            speak('youtube is open now')
            time.sleep(5)

        elif "play" in statement:
            statement.replace('play','')
            print('playing'+statement)
            speak('playing'+statement)
            pywhatkit.playonyt(statement)


        #Skill 3 -Predicting time:
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {strTime}')

        #Skill 4 -To fetch latest news:
        elif 'news' in statement:
            news = webbrowser.open_new_tab('http://www.bbc.com/bengali')
            speak('here are some headlilnes from the BBC news Bangla,Happy reading')
            time.sleep(6)

        #Skill 6-Searching data from web:
        elif 'search' in statement:
            statement = statement.replace('search','')
            webbrowser.open_new_tab(statement)
            speak('here what I found')
            time.sleep(5)

        #Skill 7- Setting your AI assistant to answer geographical and computational questions:
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what do you want to ask now')
            question = takeCommand()
            app_id = 'X226A2-TLVKLERGA8'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        #Skill 8- Extra features:
        elif 'who are you' in statement or "what's is your name" in statement or 'what can you do' in statement:
            speak("I am Genos, your personal assistant. I am your first creation of your virtual AI assistant project. I am programmed to minor tasks like opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,predict weather In different cities, get top headline news from BBC Bangla and you can ask me computational or geographical questions too!")

        elif 'who created you' in statement or 'who made you' in statement:
            speak('I was built by Sakib')
            print('I was built by Sakib')

        elif "what's your name" in statement:
            speak('My name is Genos. Your personal assistant and disciple. Sensei.')

        elif "my wife's name" in statement:
            speak("Your wife's name is Emu. You love her more than your life. Sensei")
            print("Your wife's name is Emu. You love her more than your life. Sensei")


        #Skill 9- To forecast weather:
        elif 'weather' in statement:
            api_key = '2acec86c6f2cfaed27620465814524ec'
            base_url = 'http://api.openweathermap.org/data/2.5/weather?'
            speak('what is the city name')
            city_name = takeCommand()
            complete_url = base_url+'appid='+api_key+'&q='+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x['cod'] != '404':
                y = x['main']
                current_temperature = y['temp']
                current_humidity = y['humidity']
                z = x['weather']
                weather_descripton = z[0]['description']
                speak('Temperature in kelvin unit is '+str(current_temperature)+'\nhumidity in percentage is '+str(current_humidity)+'\ndescription '+str(weather_descripton))
                print('Temperature in kelvin unit is '+str(current_temperature)+'\nhumidity in percentage is '+str(current_humidity)+'\ndescription '+str(weather_descripton))


        #Skill 10- To log off your PC:
        elif 'log off' in statement or 'sign out' in statement or 'ok bye' in statement or 'bye bye' in statement or 'goodbye' in statement or 'shut down' in statement:
            speak('Ok, your pc will log off in 10 second. make sure you exit from all applications. goodbye sensei. Take care')
            subprocess.call(['shutdown','/1'])
            break

time.sleep(3)



