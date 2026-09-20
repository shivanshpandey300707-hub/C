import importlib

sr = importlib.import_module("speech_recognition")
pyttsx3 = importlib.import_module("pyttsx3")
import datetime
import webbrowser
wikipedia = importlib.import_module("wikipedia")
import os
import builtins

# Voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    builtins.print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hello Shivansh. I am Jarvis. How can I help you?")

def run_jarvis():

    wish()

    while True:

        command = listen()

        if not command:
            continue

        # Time
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)

        # Date
        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        # Google
        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        # YouTube
        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        # GitHub
        elif "open github" in command:
            speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        # Search Google
        elif "search" in command:
            query = command.replace("search", "").strip()

            if query:
                speak("Searching for " + query)
                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    query.replace(" ", "+")
                )

        # Wikipedia
        elif "who is" in command or "what is" in command:
            try:
                topic = command.replace("who is", "").replace(
                    "what is", ""
                ).strip()

                speak("Searching Wikipedia.")

                result = wikipedia.summary(topic, sentences=2)

                speak(result)

            except Exception:
                speak("I couldn't find that information.")

        # Open Notepad
        elif "open notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad.exe")

        # Open Calculator
        elif "open calculator" in command:
            speak("Opening Calculator.")
            os.system("calc.exe")

        # Stop Jarvis
        elif "exit" in command or "stop" in command or "shutdown" in command:
            speak("Goodbye Shivansh.")
            break

        else:
            speak("I don't know that command yet.")


if __name__ == "__main__":
    run_jarvis()
