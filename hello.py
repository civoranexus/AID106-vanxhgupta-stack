import speech_recognition as sr
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for rural user input...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language='en-IN') # Supports regional codes like hi-IN
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        speak("I am sorry, I couldn't understand that. Could you repeat?")
        return "None"

if __name__ == "__main__":
    speak("Welcome to Voice Aid. How can I help you today?")
    while True:
        user_input = listen()
        
        if "hello" in user_input:
            speak("Hello! I am your assistant designed for rural connectivity.")
        
        elif "exit" in user_input or "stop" in user_input:
            speak("Goodbye!")
            break