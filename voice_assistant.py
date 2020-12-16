import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your Alexa, what can i do for you')
engine.runAndWait()


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        listener.Pause_threshold = 1
        audio = listener.listen(source)

    try:
        print("Recongnizing...")
        query = listener.recognize_google(audio, language='en-in')
        if 'alexa' in query:
            query = query.replace('alexa', '')
            print(query)

    except Exception as e:
        print('Please say it again.')
        talk('Please say it again.')
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == "__main__":
    while True:
        query = take_command().lower()
        print(query)
        if 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 10)
            print(info)
            talk(info)
        elif 'date' in query:
            talk('sorry, I have a headache')
        elif 'are you single' in query:
            talk('I am in a relationship with wifi')
        elif 'joke' in query:
            talk(pyjokes.get_joke())
        elif 'email to name' in query:
            try:
                talk("What should I say?")
                content = take_command()
                to = "email id which you have to send email "
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry my friend. I am not able to send this email")