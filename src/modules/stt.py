import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()

    def listener(self, timeout=5):
        try:
            print("Listening...")

            # Check and list available microphones
            mic_list = sr.Microphone.list_microphone_names()
            print("Available microphones:")
            for i, mic_name in enumerate(mic_list):
                print(f"{i}: {mic_name}")

            # Ensure the correct device_index is used (adjust if needed)
            device_index = 0  # Change to the correct index based on your setup
            print(f"Using microphone at index {device_index}: {mic_list[device_index]}")

            # Use the selected microphone
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

