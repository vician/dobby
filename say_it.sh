#!/bin/bash

which say-epos 1>/dev/null 2>/dev/null
if [ $? -ne 0 ]; then
	echo "ERROR: Epos not found!"
	exit 1
fi

# prekonvertuju utf8 na iso-8859-2 a dam to na vstup say-epos
say=`echo "$1" | iconv -f utf-8 -t iso-8859-2 | say-epos - -w test.wav`
# orezu dlouhe mezery za teckou
sox test.wav test2.wav silence -l 1 0.1 1% -1 0.6 1%
# prehraji a smazu souboru
mplayer test2.wav && rm test.wav test2.wav
