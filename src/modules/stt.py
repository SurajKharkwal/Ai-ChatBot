import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()
    def audioDevice (self):
        """List all available audio input devices."""
        devices = sr.Microphone.list_microphone_names()
        if devices:
            print("Available audio devices:")
            for index, name in enumerate(devices):
                print(f"{index}: {name}")
        else:
            print("No audio devices found.")

    def listener(self,device_index=4, timeout=5):
        try:
            print("Listening...")
            with sr.Microphone(device_index=device_index) as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source, timeout=timeout)
                return self.r.recognize_google(audio)

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return ""
        except AssertionError as e:
            print(f"Microphone assertion error: {e}")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

