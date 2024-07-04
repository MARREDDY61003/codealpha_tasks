import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def process_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]  # Remove stopwords
    return tokens

import requests

def get_weather(city):
    api_key = "your_api_key"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] == "404":
        return "City not found."
    else:
        weather = data["main"]
        temperature = weather["temp"]
        return f"The temperature in {city} is {temperature - 273.15:.2f}°C"

def main():
    while True:
        text = recognize_speech()
        if text:
            processed_text = process_text(text)
            if "weather" in processed_text:
                city = " ".join(processed_text[processed_text.index("weather") + 1:])
                weather_info = get_weather(city)
                speak(weather_info)
            elif "exit" in processed_text or "quit" in processed_text:
                speak("Goodbye!")
                break
            else:
                speak("I can help with weather information. Ask me about the weather in a specific city.")

if __name__ == "__main__":
    main()
