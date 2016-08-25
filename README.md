# Dobby
Chatbot with additional functionality (originally for xmpp)

## TTS

Dobby can currently use two TTS (Text-to-Speech)

- [Epos](#epos)
- [Google](#google)
- [Festival](#festival)

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

### Google

### Festival

- Ubuntu: sudo apt install festival-czech

## Availible commands

- jidlo: Decide which time is the bast for eating
- ip: Show your IP addresses
- date: Show today's date
- _default_: Answer from cleverbot

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
