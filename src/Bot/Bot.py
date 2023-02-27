#!/usr/bin/env python3
#
# PERSONNAL PROJECT, 2023
# Trade bot with Bitcoin
# File description:
# Follow pep 8 rules
#

from sys import stderr
from Mathematic.ichimoku import chikoSpan, kijunSen, tenkanSen, senkoSpanA, senkoSpanB

class Bot:
    """
        A bot that can receive data in the form of a candle and make purchase or resale decisions
    """
    def __init__(self, conf) -> None:
        self.conf = conf
        self.nbBuy = 0
        self.nbSell = 0
        self.wallet = {
            'BTC': self.conf['Trade']['Wallet']['crypto_to_buy'],
            'USDT': self.conf['Trade']['Wallet']['crypto_for_buy']
        }

    def action(self, data):
        """ Decide if he buy, sell or nothing

        Args:
            data: candle

        Returns:
            _type_: data of Ichimoku, -1 if it's too early
        """
        USDT_BUY = self.percent(self.conf['Trade']['percent_to_buy'], self.wallet['USDT'])

        if len(data['Open']) < 52:
            value = round((len(data['Open']) * 100 / 52))
            print('-' * value, '.' * round((100 - value)), sep='')
            return -1, -1, -1, -1, -1

        ssa, ssb = senkoSpanA(data['High'], data['Low']), senkoSpanB(data['High'], data['Low'])
        tenkan = tenkanSen(data['High'], data['Low'])
        kinjun = kijunSen(data['High'], data['Low'])
        chiko = chikoSpan(data['Close'])
        down_limit = min(ssa, ssb)
        up_limit = max(ssa, ssb)

        self.print_value(data, ssa, ssb, tenkan, kinjun, chiko, up_limit, down_limit)

        if data['Close'][-1] > up_limit and tenkan > kinjun and chiko > data['Close'][-1] and self.wallet['USDT'] > self.conf['Trade']['stop_to_buy']:
            self.buy(USDT_BUY, data['Close'][-1])
            self.nbBuy += 1
        elif data['Close'][-1] < down_limit and tenkan < kinjun and chiko < data['Close'][-1]:
            if self.can_sell(self.wallet['BTC']):
                self.sell(self.wallet['BTC'], data['Close'][-1])
                self.nbSell += 1

        print(f'END OF THE TRADE - {self.nbBuy} buy / {self.nbSell} sell - {self.wallet["USDT"]} USDT / {self.wallet["BTC"]} BTC', flush=True)
        print("values", ssa, ssb, tenkan, kinjun, chiko)
        return ssa, ssb, tenkan, kinjun, chiko

    def buy(self, sum_to_buy: float, price: float):
        """ buy some crypto

        Args:
            sum_to_buy (float): sum to buy
            price (float): last close candle
        """
        btc_bought = sum_to_buy / price
        print(f'---------> buy {btc_bought} BTC with {sum_to_buy} USDT', flush=True)
        self.wallet['USDT'] -= sum_to_buy
        self.wallet['BTC'] += btc_bought

    def can_sell(self, sum_to_sell: float) -> bool:
        """ To know if he can sell

        Args:
            sum_to_sell (float): sum he want to sell

        Returns:
            bool: True if he can, otherwise False
        """
        if sum_to_sell <= self.conf["Trade"]["sum_to_sell_min"]:
            print('[ERR] You can\'t sell because you don\'t have any', flush=True, file=stderr)
            return False
        return True

    def sell(self, sum_to_sell: float, actual_price):
        """ Sell crypto

        Args:
            sum_to_sell (float): sum to sell
            actual_price (_type_): last close of the crypto
        """
        print(f'---------> sell {sum_to_sell} BTC so win {self.wallet["BTC"] * actual_price} USDT', flush=True)
        self.wallet['USDT'] += self.wallet['BTC'] * actual_price
        self.wallet['BTC'] -= sum_to_sell

    def percent(self, percent: float, sum: float) -> float:
        return percent * sum / 100

    def print_value(self, data, ssa, ssb, tenkan, kinjun, chiko, up_limit, down_limit) -> float:
        """
            Print of debug
        """
        print('---- BUY ----')
        print('ssa', '>' if ssa > ssb else '<=', 'ssb', flush=True)
        print('data[\"Close\"][-1] > up_limit:', data['Close'][-1], up_limit, data['Close'][-1] > up_limit)
        print('tenkan > kinjun:', tenkan, kinjun, tenkan > kinjun)
        print('chiko > data[\"Close\"][-1]:', chiko, data['Close'][-1], chiko > data['Close'][-1])

        print('---- SELL ----')
        print('data[\"Close\"][-1] < down_limit:', data['Close'][-1], down_limit, data['Close'][-1] < down_limit)
        print('tenkan < kinjun:', tenkan, kinjun, tenkan < kinjun)
        print('chiko < data[\"Close\"][-1]:', chiko, data['Close'][-1], chiko < data['Close'][-1])

    def __str__(self):
        return 'Wallet:' + self.wallet
