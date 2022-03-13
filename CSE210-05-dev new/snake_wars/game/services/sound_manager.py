# An optional class. We may or may not use it. Would be a "fun addition," if we have the time.
# import distro # TODO: To be used in future games... :)
from platform import system, release, version
from types import TracebackType
from log21 import Levels

from shared_data import SharedData

class SoundManager():
    # Play sounds, imports sounds, etc. on multiple OSes.

    # Initialize the class:
    def __init__(self):
        print(f"Current OS: {system} {release} (v{version})")
        self._data = SharedData()
        self.sound_playing = self._data.sound_playing
    
    # Play a sound:
    def play_sound(self, path: str):
        if system() == "Windows":
            import winsound
            winsound.PlaySound(path, winsound.SND_ASYNC)
            self.sound_playing = True
            self._data.log_utils.log_msg(f"Played sound '{path.split(self._data.path_sep)[len(path.split(self._data.path_sep))-1]}'.", Levels.DEBUG)
        elif system() == "Linux":
            pass # TODO: #1 Do linux related sound things here...