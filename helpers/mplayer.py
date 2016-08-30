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

    def play(self,audio_file,threading="1"):
        if len(audio_file) > 0:
            self.audio_file = audio_file
            if threading == "1":
                if threading.active_count() <= 1:
                    self.stop() # Should be disabled for youtube?
                    self.playThread = threading.Thread(target=self.thread)
                    self.playThread.start()
            else:
                self.stop()
                self.thread()

    def stop(self):
        if self.playThread is not None:
            subprocess.call(["killall", "mplayer"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            self.playThread.join()
            self.playThread = None
