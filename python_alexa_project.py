# pip install pyttsx3
# pip install pipwin
# pip install pyaudio
# pip install pywhatkit
# pip install wikipedia
# pip install weather629
# pip install pyjokes
# import datetime 




#importing required library:-
#=============================


import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import weather629
from datetime import datetime
import pyjokes 



# function for alexa female voice:-
#===================================


def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(answer)
    engine.runAndWait()


#function for processing question:-
#====================================

    
def processQuestion(question):
    if 'what are you doing' in question:
        print("i am waiting for your question")
        talk('i am waiting for your question')
        return True
    elif 'how are you' in question:
        print("i am good , how can i help you...")
        talk('i am good , how can i help you...')
        return True
    elif 'play' in question:
        question = question.replace('play','')
        pywhatkit.playonyt(question)
        return True
    elif 'who is' in question:
        question = question.replace('who is', '')
        print(wikipedia.summary(question,1))
        talk(wikipedia.summary(question,1))
        return True
    elif 'time' in question:
        time =datetime.today().time().strftime('%I:%M:%P')
        print(time)
        talk(time)
        return True
    elif 'joke' in question:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        retrun True
    elif 'love you' in question:
        print("niku inko pani ledha yentra... yepudu adhena")
        talk('niku inko pani ledha yentra... yepudu adhena')
        return True
    elif 'what is weather now' in question:
        weather = weather-reporter -q delhi -d 3
        talk(weather)
        return True
    elif "byee" in question:
        talk("bye byee .. see you soon")
        return False
    else:
        print("i can't process your request...")
        return True
    


# function for geting question and microphone as source
#======================================================
        
def getQuestion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if 'Alexa' in question:
                question = question.replace('Alexa','')
                print(question)
                return question   
            else:
                print('you are not talking with me , please carion with you friend')
                return "notwithme"
        except sr.UnknownValueError:
            print("sorry, i can't get  you")



# while loop for iterating question continuosly:
#================================================

canAskQuestion = True
while canAskQuestion:
    question = getQuestion()
    if question=="notwithme":
        talk("ok carrion with your friend")
        canAskQuestion = False
    else:
        canAskQuestion = processQuestion(question)
