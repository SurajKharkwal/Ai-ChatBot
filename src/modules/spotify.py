import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyPlayer:
    def __init__(self):
        # Initialize Spotify API client
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.environ["CLIENT_ID"],
            client_secret=os.environ["CLIENT_SECRET"],
            redirect_uri=os.environ["REDIRECT_URI"],
            scope="user-modify-playback-state user-read-playback-state user-read-currently-playing"
        ))

    def play_song(self, song_name=None):
        try:
            if song_name:
                results = self.sp.search(q=song_name, type='track', limit=1)
                if results and 'tracks' in results and results['tracks']['items']:
                    track_uri = results['tracks']['items'][0]['uri']
                    self.sp.start_playback(uris=[track_uri])
                    print(f"Playing {song_name}.")
                else:
                    print(f"No track found for {song_name}.")
            else:
                self.sp.start_playback()
                print("Resuming playback.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error playing song: {e}")
        except TypeError as e:
            print(f"Unexpected error: {e}")

    def pause_song(self):
        """Pause the current song."""
        try:
            self.sp.pause_playback()
            print("Playback paused.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error pausing playback: {e}")

    def next_song(self):
        """Skip to the next track."""
        try:
            self.sp.next_track()
            print("Skipped to the next track.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error skipping to the next track: {e}")

    def previous_song(self):
        """Go back to the previous track."""
        try:
            self.sp.previous_track()
            print("Skipped to the previous track.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Error skipping to the previous track: {e}")

