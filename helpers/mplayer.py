import subprocess
import threading

class Mplayer():

    playThread = None

    def __init__(self):
        pass

    def thread(self,audio_file):
        if len(audio_file) > 0:
            args = [ "mplayer", "-really-quiet", audio_file]
            subprocess.Popen(args)

    def play(self,audio_file):
        if len(audio_file) > 0:
            if threading.active_count() <= 1:
                self.playThread = threading.Thrread(target=self.thread)
                self.playThread.start()

    def stop(self):
        if self.playThread is not None:
            subprocess.call(["killall", "mplayer"])
            self.playThread.join()
            self.playThread = None
