import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
        
    speak("I am mani. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Wikipedia Search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I could not find any information on that.")
                
        
        # Open YouTube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        # Open Google
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        # Open Stack Overflow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'open facebook'in query:
            webbrowser.open("facebook.com")
            
        elif 'open linkedin'in query:
            webbrowser.open("linkedin.com")
            
        elif 'open nakuri'in query:
            webbrowser.open("nakuri.com")
            
        
        
        # Tell the time
        elif 'my name is' in query:
            name = query.replace('my name is', "").strip()
            speak(f"Hi {name}, nice to meet you!")
        
        elif 'i am' in query:
            name = query.replace('i am', "").strip()
            speak(f"Hi {name}, nice to meet you!")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'send whatsapp message' in query:
            try:
                speak("Please tell me the phone number with country code.")
                phone_number = takeCommand().replace(" ", "").strip()
                speak("What is the message?")
                message = takeCommand()
                
                # Schedule the message to be sent 2 minutes from now
                now = datetime.datetime.now()
                hour = now.hour
                minute = now.minute + 2  # Sends message in 2 minutes
                
               
            except Exception as e:
                speak("I am sorry, I couldn't send the message.")
        
        
        # Exit the loop
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day!")
            break
