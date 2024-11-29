from modules.stt import SpeechToText
from modules.ai import AI

speech_to_text = SpeechToText()
ai = AI()

ai.speak_text("AI is initialized.")

while True:
    text = speech_to_text.listener(timeout=3)
    print(f"Recognized text: {text}")
    
    if text == "" or text == "Google Speech Recognition could not understand the audio":
        continue
    if "goodbye" in text.lower():
        ai.speak_text("Goodbye!")
        break
    else:
        print("Promt",text)
        ai.speak(text) 

