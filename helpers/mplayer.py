import subprocess
import threading

class Mplayer():

    playThread = None
    audio_file = ""

    def __init__(self):
        pass

    def thread(self):
        if len(self.audio_file) > 0:
            args = [ "mplayer", self.audio_file]
            subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def play(self,audio_file):
        if len(audio_file) > 0:
            self.audio_file = audio_file
            if threading.active_count() <= 1:
                self.playThread = threading.Thread(target=self.thread)
                self.playThread.start()

    def stop(self):
        if self.playThread is not None:
            subprocess.call(["killall", "mplayer"])
            self.playThread.join()
            self.playThread = None
