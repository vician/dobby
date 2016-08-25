#!/usr/bin/python
# -*- coding: utf-8 -*-
# Youtoobe player
# Author: Jan Lipovský <janlipovsky@gmail.com>

import subprocess
import logging
import sys


class PyMixer(object):
    """
    Wrapping class for using linux amixer to set volume
    """
    amixer = 'amixer'
    logger = None

    def __init__(self):
        self.logger = logging.getLogger("PyMixer")

    def set_volume(self, value):

        if value < 0:
            self.logger.info("Norm value to: 0")
            value = 0

        volume = int((65536/100) * int(value))
        subprocess.call(["sudo", "-u", "dobby", "amixer", "set", "Master", "{}".format(volume)])
        return "Volume set for: {}% - {}".format(value, volume)

    def get_volume(self):
        temp = subprocess.check_output(["sudo", "-u", "dobby", "amixer", "get", "Master"], universal_newlines=True)

        pos = temp.find('[')
        volume = temp[pos+1:pos+4]

        if volume[2] == '%':
            volume = volume[:2]

        return volume


if __name__ == "__main__":
    m = PyMixer()
    print(m.set_volume(110))
