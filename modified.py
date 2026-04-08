# py -3.10 -m pip install gTTS pygame speechrecognition googletrans==4.0.0-rc1 pyaudio
import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator  #  # Google Translate API
from gtts import gTTS
import pygame
import os
import time

# Initialize text-to-speech engine
def speak(text, language="hi"):
    try:
        filename = "translated_voice.mp3"
        tts = gTTS(text=text, lang=language)
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait until playback finishes
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove(filename)

    except Exception as e:
        print("Error in speaking:", e)


# Speech-to-Text: Recognize spoken language (English)

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("???? Please speak now in English...")

        audio = recognizer.listen(source)



    try:

        print("???? Recognizing speech...")

        text = recognizer.recognize_google(audio, language="en-US")  # Use English for speech recognition

        print(f"✅ You said: {text}")

        return text

    except sr.UnknownValueError:

        print("❌ Could not understand the audio.")

    except sr.RequestError as e:

        print(f"❌ API Error: {e}")

    return ""



# Translate text using Google Translate API

def translate_text(text, target_language="hi"):
    translation = GoogleTranslator(source='auto', target=target_language).translate(text)
    print(f"Translated text: {translation}")
    return translation



# Display language options to the user

def display_language_options():

    print("???? Available translation languages: ")

    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Gujarati (gu)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")



    # User selects language

    choice = input("Please select the target language number (1-8): ")

    language_dict = {

        "1": "hi",

        "2": "ta",

        "3": "te",

        "4": "bn",

        "5": "mr",

        "6": "gu",

        "7": "ml",

        "8": "pa"

    }

    

    return language_dict.get(choice, "es")  # Default to Spanish if invalid input



# Main function to combine all steps

def main():

    # Step 1: Display language options and get user's choice

    target_language = display_language_options()

    

    # Step 2: Speech-to-Text (recognizing English speech)

    original_text = speech_to_text()

    

    if original_text:

        # Step 3: Translate to selected target language

        translated_text = translate_text(original_text, target_language=target_language)

        

        # Step 4: Text-to-Speech (Translate output and speak it)

        speak(translated_text, language=target_language)  # Speak the translation in English

        print("✅ Translation spoken out!")



if __name__ == "__main__":

    main()