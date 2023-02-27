#!/usr/bin/env python3
#
# PERSONNAL PROJECT, 2023
# Trade bot with Bitcoin
# File description:
# Server to get crypto info
#

from sys import stderr
from requests import get
from time import sleep
from threading import Thread

from Cryptograph.Cryptograph import Cryptograph

data = {
    "Open time": [],
    'Open': [],
    "High": [],
    "Low": [],
    'Close': [],
    "Volume": [],
    "Close time": [],
    "Quote asset volume": [],
    "Number of trades": [],
    "Taker buy base asset volume": [],
    "Taker buy quote asset volume": [],
    "Ignore": []
}
keys = list(data.keys())


class Server:
    """
        Server who will send request to know the current price of the crypto, then send it to the bot, then print with the Cryptograph
    """
    def __init__(self, conf, bot) -> None:
        self.conf = conf
        self.url = f"https://api.binance.com/api/v1/klines?symbol={self.conf['Trade']['symbole']}&interval={self.conf['Trade']['interval']}"
        self.t1 = Thread(target=self.run)
        self.t1.start()
        self.graph = Cryptograph(self.conf)
        self.bot = bot

    def run(self):
        while True:
            reponse = get(self.url)
            if reponse.status_code == 200:
                last_candle = self.parse(reponse)
                ssa, ssb, tenkan, kinjun, chiko = self.bot.action(data)
                self.graph.add(last_candle, ssa, ssb, tenkan, kinjun, chiko)
            else:
                print('[ERR] Binance API failure', flush=True, file=stderr)
            sleep(self.conf['Trade']['time_between_request'])
        self.t1.join()

    def parse(self, info):
        donnees = info.json()
        last_candle = donnees[-1]
        for i, val in enumerate(last_candle):
            data[keys[i]].append(float(val))
        return last_candle
