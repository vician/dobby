# Dobby
Chatbot with additional functionality (originally for xmpp)

## Availible commands

See `$ help`

### Write new module

- See `reactions/example.py`
- Preapre your module as `reactions/yourmodule.py`
- Content has to be as in `reactions/example.py` with your changes
- Do not forget to:
	- rename *class name*
	- write help
	- specify aliasses (the first is used as section in dobby.ini file)
	- specify attributes
	- do not use `__init__()` but use `init()` instead of it
	- inicialize attributes in `init()`
	- write your behaviour in `do()`
	- use `self.ini.get()` for all attributes
- Include your module to Dobbby `from reactions.yourmodule import Yourmodule`
- Add loading to `__init__` of `Dobby`: `self.load_reaction(Yourmodule())`

## TTS

Dobby can currently use two TTS (Text-to-Speech)

- [Espeak](#espeak)
- [Epos](#epos)
- [Google](#google)
- [Festival](#festival)

### Espeak

Install `python3-espeak` package.

### Epos

Official webpage: http://epos.ufe.cz/

Installation:
- Download epos from http://epos.ufe.cz/
- Unpack
- Build

```
wget "http://epos.ufe.cz/download/ep2-4-85.tgz"
tar xvf ep2-4-85.tgz
cd epos-2.4.85/src
./configure
make
```

#### Requirements

- Ubuntu: `sudo apt install libpulse-dev`

### Writing new TTS

- See `tts/example.py`
- Preapre your tts as `tts/yourtts.py`
- Content has to be as in `tts/example.py` with your changes
- Do not forget to:
	- rename *class name*
	- do not use `__init__()` or `init()` but use `tts_init()` instead of them
	- write your behaviour in `tts_say()`
	- use `helpers.language` for getting language code or name (see `tts/gtts.py`)
	- use `helpers.mplayer` if you need some media player


### Google

### Festival

- Ubuntu: sudo apt install festival-czech

## SST

### sr

- Ubuntu ```
sudo apt install portaudio19-dev
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio
sudo python3 setup.py install
pip3 install SpeechRecognition
```

## Example running
```
./dobby.py 
Hi, I'm your house-elf Dobby. How can I help you?
$ Hi, Dobby
Nobody ever says Harry.
$ How are you?
Fine and you?
$ date
Today is 2016-08-25
$ jidlo
OK, takze jidlo bude presne v 13:54
```
