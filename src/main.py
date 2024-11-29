
from modules.ai import AI
from modules.player import SimpleMusicPlayer
from modules.stt import SpeechToText

speech_to_text = SpeechToText()
ai = AI()
player = SimpleMusicPlayer()

speech_to_text.audioDevice()

ai.speak_text("AI is initialized.")

while True:
    print("Listening for commands...")
    text = speech_to_text.listener(timeout=3)
    print(f"Recognized text: {text}")
    
    if text == "" or text == "Google Speech Recognition could not understand the audio":
        continue

    command = text.lower()

    if "goodbye" in command:
        ai.speak_text("Goodbye!")
        break

    elif "play" in command:
        # Extract song name after the command "play"
        song_name = command.replace("play", "").strip()
        if song_name:  # Ensure there is a song name
            player.run(song_name)
        else:
            ai.speak_text("Please provide a song name.")
    else:
        print(f"Generating ...{text}")
        ai.speak(text)  # Repeat the recognized text

