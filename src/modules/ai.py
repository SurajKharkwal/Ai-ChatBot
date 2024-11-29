
from gtts import gTTS
import os
import google.generativeai as genai
import tempfile
import pygame
import time

class AI:
    def __init__(self):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        pygame.init()
        pygame.mixer.init()

    def speak(self, query):
        try:
            print("Generating response...")
            for chunk in self.model.generate_content(query, stream=True):
                text = chunk.text
                print(text, end="", flush=True) 
                self.speak_text(text)
        except Exception as e:
            print(f"An error occurred: {e}")

    def speak_text(self, text):
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_file:
            tts = gTTS(text)
            tts.save(temp_file.name)  # Save speech to a temporary file
            
            pygame.mixer.music.load(temp_file.name)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

if __name__ == "__main__":
    assistant = AI()
    assistant.speak("Today news")
