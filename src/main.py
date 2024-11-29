
from modules.stt import SpeechToText
from modules.ai import AI
from modules.spotify import SpotifyPlayer

speech_to_text = SpeechToText()
ai = AI()
spotify = SpotifyPlayer()

ai.speak_text("AI is initialized.")

while True:
    text = speech_to_text.listener(timeout=3)
    print(f"Recognized text: {text}")
    
    if text == "" or text == "Google Speech Recognition could not understand the audio":
        continue

    command = text.lower()

    if "goodbye" in command:
        ai.speak_text("Goodbye!")
        break

    elif "play next song" in command or "next song" in command:
        ai.speak_text("Skipping to the next song.")
        spotify.next_song()

    elif "play previous song" in command or "previous song" in command:
        ai.speak_text("Going back to the previous song.")
        spotify.previous_song()

    elif "pause song" in command or "pause music" in command:
        ai.speak_text("Pausing the song.")
        spotify.pause_song()

    elif "play song" in command:
        song_name = command.replace("play song", "").strip()
        if song_name:
            ai.speak_text(f"Playing {song_name}.")
            spotify.play_song(song_name)
        else:
            ai.speak_text("Please specify the song name.")

    else:
        ai.speak(text)
