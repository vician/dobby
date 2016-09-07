#!/usr/bin/env python3

import syslog
from jabberbot import JabberBot, botcmd


class MUCJabberBot(JabberBot):

    ''' Add features in JabberBot to allow it to handle specific
    characteristics of multiple users chatroom (MUC). '''


    def __init__(self, *args, **kwargs):
        ''' Initialize variables. '''

        # answer only direct messages or not?
        self.only_direct = kwargs.get('only_direct', False)
        try:
            del kwargs['only_direct']
        except KeyError:
            pass

        # initialize jabberbot
        super(MUCJabberBot, self).__init__(*args, **kwargs)

        # create a regex to check if a message is a direct message
        user, domain = str(self.jid).split('@')
        self.direct_message_re = re.compile('^%s(@%s)?[^\w]? ' \
                % (user, domain))

    def callback_message(self, conn, mess):
        ''' Changes the behaviour of the JabberBot in order to allow
        it to answer direct messages. This is used often when it is
        connected in MUCs (multiple users chatroom). '''

        message = mess.getBody()
        if not message:
            return

        if self.direct_message_re.match(message):
            mess.setBody(' '.join(message.split(' ', 1)[1:]))
            return super(MUCJabberBot, self).callback_message(conn, mess)
        elif not self.only_direct:
            return super(MUCJabberBot, self).callback_message(conn, mess)

class Dobby(MUCJabberBot):

    __RETCODE_SHUTDOWN = 0
    __RETCODE_UPDATE = 2

    talker = None
    say_all = False

    def __init__(self, *args, **kwargs):
        MUCJabberBot.__init__(self, *args, **kwargs)

        self.talker = Talker()
        self.yt = Ytplayer()
        self.__wp = Webpages()
        self.__cb = Cleverbot()
        self.__cp = CatchPhrases()
        self.__return_code = self.__RETCODE_SHUTDOWN
        self.say_all = False
        self.mixer = PyMixer()

        regexp = re.compile('[^:]*: ')
        self.__rm_name = lambda msg: regexp.sub('', msg, 1)

    def shutdown(self):
        MUCJabberBot.shutdown(self)
        return self.__return_code

    def say_and_send(self, mess, text):
        self.send_simple_reply(mess, text)
        if self.say_all:
            self.talker.addAndSayMessage(text)

    @botcmd
    def date(self, mess, args):
        """Dobby says what date it is."""
        reply = datetime.now().strftime('%Y-%m-%d')
        self.say_and_send(mess, reply)

    @botcmd
    def say_all(self, mess, args):
        """ say_all start/stop Dobby will read all his messages"""

        if args.strip() == "stop":
            self.say_all = False
            self.say_and_send(mess, "Už mlčím!")
        else:
            self.say_all = True
            self.say_and_send(mess, "Od teď vám budu zprávy i číst!")


    @botcmd
    def say(self, mess, args):
        """Dobby says text using EPOS."""
        if len(args) <= 0:
            self.talker.addAndSayMessage("Nemám co říct.")
        else:
            self.talker.addAndSayMessage(args)

    @botcmd
    def say_google(self, mess, args):
        """Set google voice and language"""
        self.talker.useGoogle()
        if len(args) > 0:      
                self.talker.setGoogleLanguage(args)
                self.say_and_send(mess, "Google TTS je nastaven na jazyk: "+args)
        else:
            self.say_and_send(mess, "Google TTS je nastaven na jazyk: "+self.talker.googleLang)

    @botcmd
    def say_epos(self, mess, args):
        """Set epos voice"""
        self.talker.useEpos()
        self.say_and_send(mess, "Epos TTS je nastaven")

    @botcmd
    def show_ip(self, mess, args):
        """Shows Dobby IP addresses"""
        ifaces = ni.interfaces()
        ret = "My IPs are:"
        for iface in ifaces:
            ni.ifaddresses(iface)
            ip = ni.ifaddresses(iface)[2][0]['addr']
            ret += "\n{}: {}".format(str(iface), str(ip))

        self.say_and_send(mess, ret)

    @botcmd
    def yt(self, mess, args):
        """yt <URL> Playes Youtube URL"""
        ret = self.yt.play_youtube(args)
        self.say_and_send(mess, ret)

    @botcmd
    def yt_stop(self, mess, args):
        """STOP youtube player"""
        ret = self.yt.stop_youtube()
        self.say_and_send(mess, ret)


    @botcmd
    def volume(self, mess, args):
        """set or get volume"""

        volume = args.strip()
        if len(volume) > 0:
            self.mixer.set_volume(volume)

        volume = self.mixer.get_volume()
        self.say_and_send(mess, "Volume is set to {}%".format(volume))

    @botcmd
    def google(self, mess, args):
        """Dobby googles for answers."""

        search = pygoogle(log_level=logging.INFO, query=args, pages=1, hl='cs').search()

        reply = 'Tak jsem vygooglil tohle: \n'
        count = 0
        for res in search:
            count = count + 1
            reply = reply + str(count) + ": " + res + ' - ' + search[res] + '\n'
            if count > 2:
                break

        self.say_and_send(mess, reply)

    @botcmd
    def jidlo(self, mess, args):
        """Dobby says at what time my masters eat today."""
        tmp = random.randint(0, 11)

        if(tmp <= 7):
            cas = lunchTime.getLunchTimeNow(59)
            if(cas == False):
                reply = 'ERROR: getLunchTimeFromNow'
            else:
                reply = "OK, takze jidlo bude presne v "+cas

        if(tmp == 8):
            reply = 'Vsechno bude, neboj!'
        if(tmp == 9):
            reply = 'Bezte si zrat kdy chcete!'
        if(tmp == 10):
            reply = 'Jidlo, jidlo? Makat se bude!'
        if(tmp == 11):
            reply = 'Diky, zatim nemam hlad.'

        self.say_and_send(mess, reply)

    def unknown_command(self, mess, cmd, args):
        """
        Handle unknown commands.
        """
        msg = cmd if not args else cmd + ' ' + args
        if msg.lower().find(self._username.lower()) >= 0 and mess.attrs['from'].resource != self._username:
            self.say_and_send(mess, mess.attrs['from'].resource + ': ' + self.__cb.ask(self.__rm_name(msg)))

if __name__ == '__main__':
    # if the first command line parameter is "test", connect to the test room
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        pass
    else:
        pass

    mucbot = Dobby(
        username, password, only_direct=False, command_prefix=nickname.lower()+': ',
        server="jabber.cyan-networks.com", debug=False)
    mucbot.muc_join_room(chatroom, nickname, password='dobby')
    sys.exit(mucbot.serve_forever())
