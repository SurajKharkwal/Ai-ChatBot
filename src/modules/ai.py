
from gtts import gTTS
import os
import google.generativeai as genai
import tempfile
import pygame
import time

class AI:
    def __init__(self):
        genai.configure(api_key="AIzaSyBwzOtsCqcxorIsyitmgpyPce76T8NshTg")
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
        """
        Convert text to speech and play it using pygame.
        """
        temp_path = None
        try:
            # Define a custom temporary directory
            temp_dir = os.path.join(os.getcwd(), "temp_audio")
            os.makedirs(temp_dir, exist_ok=True)  # Create the directory if it doesn't exist

            # Create a temporary file in the custom directory
            temp_path = os.path.join(temp_dir, "speech.mp3")
            tts = gTTS(text)
            tts.save(temp_path)  # Save the speech as an MP3 file

            # Load and play the audio with pygame
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            # Wait for the audio playback to finish
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            # Stop and unload the mixer to release the file
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

        except Exception as e:
            print(f"An error occurred while speaking: {e}")
        finally:
            # Clean up the temporary file
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == "__main__":
    assistant = AI()
    assistant.speak("Today news")
