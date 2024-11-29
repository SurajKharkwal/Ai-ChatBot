
import yt_dlp
import pygame
import os

class SimpleMusicPlayer:
    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()

    def search_and_play(self, song_name):
        """
        Search for the song on YouTube and play it.
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'default_search': 'ytsearch',
            'outtmpl': 'temp_audio.%(ext)s',  # Temporary filename
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            video = info_dict['entries'][0]
            print(f"Now playing: {video['title']}")

            # Load and play the song
            pygame.mixer.music.load('temp_audio.mp3')
            pygame.mixer.music.play()

            # Wait until the song finishes playing
            while pygame.mixer.music.get_busy():  # Check if music is still playing
                pygame.time.Clock().tick(10)  # Wait and check every 100ms

            # Clean up by removing the temporary file after it's done playing
            os.remove('temp_audio.mp3')

    def run(self, song_command):
        """
        Play the song based on the user's command.
        """
        if song_command.lower() != "stop music":
            self.search_and_play(song_command)
