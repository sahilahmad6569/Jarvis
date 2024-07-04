import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai
import os
import datetime
import wikipedia
import requests

# Configure API keys and check if they are set
def configure_api_keys():
    """Ensures that the API keys are set correctly in the environment variables."""
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    if not weather_api_key:
        raise ValueError("WEATHER_API_KEY environment variable not set")
    
    return gemini_api_key, weather_api_key

gemini_api_key, weather_api_key = configure_api_keys()

# Configure Generative AI
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for better clarity
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Select a clear English voice
voices = engine.getProperty('voices')
for voice in voices:
    if 'english' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Initialize the speech recognizer
r = sr.Recognizer()

def speak(text: str):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_weather():
    """Fetches current weather information."""
    city = "Varanasi"  # Change this to your city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {city} is {main} with {description}. The temperature is {temp} degrees Celsius."
    else:
        return "Unable to fetch weather information."

def process_command(command: str):
    """Processes the given command and performs the corresponding action."""
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com/in/sahil-ahmad-tech")
    elif "open my website" in command:
        webbrowser.open("https://sahilahmad.netlify.app")
    elif "open github" in command:
        webbrowser.open("https://github.com/sahilahmad6569")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "favourite song" in command:
        webbrowser.open("https://www.youtube.com/watch?v=2RubMkkAltE")
    elif "college website" in command:
        webbrowser.open("https://sms.iul.ac.in/Student/index.aspx")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")
    elif "weather" in command:
        weather_info = get_weather()
        speak(weather_info)
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    # elif "take note" in command:
    #     note = command.replace("take note", "").strip()
    #     with open("notes.txt", "a") as file:
    #         file.write(note + "\n")
    #     speak("Note taken.")
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown now")
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("reboot")
    elif "log out" in command:
        speak("Logging out.")
        os.system("logout")
    else:
        try:
            prompt = f"You are a voice assistant. Respond to the command: {command}. Please provide a brief and relevant response using spellings in a way so that when it is pronounced by text to speech, it's understandable."
            response = model.generate_content(prompt)
            response_text = response.text.strip()
            print(response_text)
            speak(response_text)
        except Exception as e:
            print("Error in generating response:", e)
            speak("I'm sorry, I couldn't process that command.")

def listen_for_wake_word():
    """Listens for the wake word 'Jarvis'."""
    print("Listening for wake word...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Reduce background noise
        while True:
            try:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
                active_word = r.recognize_google(audio).lower()
                if active_word == "jarvis":
                    speak("Yes?")
                    return  # Wake word detected, exit the loop
            except sr.UnknownValueError:
                print("Jarvis could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print("Error occurred:", e)

def listen_for_command():
    """Listens for a voice command after the wake word has been detected."""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening for command...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            command = r.recognize_google(audio)
            process_command(command)
        except sr.UnknownValueError:
            print("Jarvis could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print("Error occurred:", e)

def main():
    """Main function to initialize and run the voice assistant."""
    speak("Initializing Jarvis...")
    while True:
        listen_for_wake_word()
        listen_for_command()

if __name__ == "__main__":
    main()
