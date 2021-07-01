"""A video player class."""

from src.video import Video
from .video_library import VideoLibrary
from .video_playlist import Playlist
import random
is_playing = False
previous_video = None


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.now_playing = None
        self.is_paused = False
        self.is_playing = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        show_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        list = []
        for item in show_videos:
            title_vid = item.title
            id_vid = item.video_id
            tags_vid = item.tags
            if not tags_vid:
                tags_vid = ''
                list.append(f"\t{title_vid} ({id_vid}) [{tags_vid}] ")
            else:
                list.append(f"\t{title_vid} ({id_vid}) [{tags_vid[0]} {tags_vid[1]}] ")

        first = list.pop(0)
        list.insert(2, first)
        for item in list:
            print(item)

    def play_video(self, video_id):
        global is_playing
        global previous_video
        now_playing = self._video_library.get_video(video_id)
        if now_playing == None :
            print(f"Cannot play video: Video does not exist")
        else:
            if is_playing is True:
                print(f"Stoping video: {previous_video}")
                print(f"Playing video: {now_playing.title}")
                previous_video = now_playing.title
            else:
                print(f"Playing video: {now_playing.title}")
                is_playing = True
                previous_video = now_playing.title

    def stop_video(self):
        """Stops the current video."""
        global is_playing
        global previous_video
        global now_playing
        global is_paused
        """Displays video currently playing."""
        if is_playing:
            print("Stopping video: {now_playing.title}")
            is_playing = False
            previous_video = None
        else:
            print("Cannot stop video: No video is currently playing!")
            previous_video = None
            is_paused = False

    def play_random_video(self):
        global is_playing
        global is_paused
        global previous_video
        global now_playing

        now_playing = random.choice(self._video_library.get_all_videos())
        if is_playing:
            print(f"Stopping video: {previous_video}")
            print(f"Playing video: {now_playing.title}")
            is_playing = True
            is_paused = False
        else:
            print(f"Playing video: {now_playing.title}")
            is_playing = True
            is_paused = False
        previous_video = now_playing.title

    def pause_video(self):
        """Pauses the current video."""
        if self.is_paused and self.now_playing:
            print(f"Video already paused: {self.now_playing.title}")
        else:
            if self.is_playing and not self.is_paused:
                print(f"Pausing Video: {self.now_playing.title}")
                self.is_paused = True
            else:
                print("Cannot pause video: No video is currently playing!")

    def continue_video(self):
        """Resumes playing the current video."""  
        if not self.is_paused and self.now_playing:
            print("Cannot continue video: Video is not paused!")
        else:
            if self.is_paused:
                print(f"Continuing video: {self.now_playing.title}")
                self.is_paused = False
            else:
                print("Cannot continue video: No video is currently playing!")

    def show_playing(self):
        """Displays video currently playing."""

        if self.now_playing and not self.is_paused and self.is_playing:
            tags = " ".join(self.now_playing.tags)
            print(f"Currently playing: {self.now_playing.title} ({self.now_playing.video_id}) [{tags}]")
        else:
            if self.is_paused and self.now_playing:
                tags = " ".join(self.now_playing.tags)
                print(f"Currently playing: {self.now_playing.title} ({self.now_playing.video_id}) [{tags}] - PAUSED")
            else:
                print("No video is currently playing!")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
