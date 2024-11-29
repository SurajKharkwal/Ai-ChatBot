import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()

    def listener(self, timeout=1):
        """Listen to the microphone and recognize speech."""
        with sr.Microphone(device_index=11) as source:
            print("Listening...")
            self.r.adjust_for_ambient_noise(source)

            try:
                audio = self.r.listen(source, timeout=timeout)
                text = self.r.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand the audio"
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"
            except Exception as e:
                return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    speech_to_text = SpeechToText()
    recognized_text = speech_to_text.listener(timeout=3)
    print(f"Recognized text: {recognized_text}")

