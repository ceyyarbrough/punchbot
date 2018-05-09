# punchbot.py
# Main code for bot

import cfg
import utils
import socket
import re
import time
import thread
from time import sleep


def main():
    # Networking
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    utils.chat(s, "What up party people!")

    thread.start_new_thread(utils.threadFillOpList, ())

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)
            print(response)

        if message.strip() == "!hey":
            utils.chat(s, "What's up dude")
        if message.strip() == "best":
            utils.chat(s, "PunchBot is the best")
        sleep(1)


if __name__ == "__main__" :
    main()