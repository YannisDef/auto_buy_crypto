#!/usr/bin/env python3
#
# PERSONNAL PROJECT, 2023
# Trade bot with Bitcoin
# File description:
# Graphic for crypto
#

from matplotlib import pyplot as plt
import time


"""
    Graphic for crypto
"""
class Cryptograph:
    def __init__(self, conf) -> None:
        self.conf = conf
        self.candle_data = {
            'close': [0] * 52,
            'ssa': [0] * 52,
            'ssb': [0] * 52,
            'tenkan': [0] * 52,
            'kinjun': [0] * 52,
            'chiko': [0] * 52
        }
        self.size_max = self.conf['Cryptograph']['size_max']

        self.fig, self.ax = plt.subplots()
        self.close, = self.ax.plot(self.candle_data['close'], "g-", label='close')
        self.ssa, = self.ax.plot(self.candle_data['ssa'], "b-", label='ssa')
        self.ssb, = self.ax.plot(self.candle_data['ssb'], "k-", label='ssb')
        self.tenkan, = self.ax.plot(self.candle_data['tenkan'], "y-", label='tenkan')
        self.kinjun, = self.ax.plot(self.candle_data['kinjun'], "m-", label='kinjun')
        self.chiko, = self.ax.plot(self.candle_data['chiko'], "r-", label='chiko')
        self.ax.legend(handles=[self.close, self.ssa, self.ssb, self.tenkan, self.kinjun, self.chiko])

    def run(self):
        while True:
            if len(self.candle_data['close']) < 52:
                print("Not enough data", len(self.candle_data['close']))
                time.sleep(10)
                continue

            self.close.set_ydata(self.candle_data['close'])
            self.ssa.set_ydata(self.candle_data['ssa'])
            self.ssb.set_ydata(self.candle_data['ssb'])
            self.tenkan.set_ydata(self.candle_data['tenkan'])
            self.kinjun.set_ydata(self.candle_data['kinjun'])
            self.chiko.set_ydata(self.candle_data['chiko'])

            self.ax.relim()  # Recalculer les limites des axes
            self.ax.autoscale_view()  # Ajuster l'échelle des axes
            plt.draw()  # Dessiner le graphique
            plt.pause(1)  # Attendre une seconde

    def add(self, last_candle, ssa, ssb, tenkan, kinjun, chiko):
        """ add some data in every keys

        Args:
            last_candle (_type_): last candle registered
            ssa (_type_): ssa
            ssb (_type_): ssb
            tenkan (_type_): tenkan
            kinjun (_type_): kinjun
            chiko (_type_): chiko
        """
        self.candle_data['close'].append(float(last_candle[4]))
        self.candle_data['close'].pop(0)

        self.candle_data['ssa'].append(ssa)
        self.candle_data['ssa'].pop(0)

        self.candle_data['ssb'].append(ssb)
        self.candle_data['ssb'].pop(0)

        self.candle_data['tenkan'].append(tenkan)
        self.candle_data['tenkan'].pop(0)

        self.candle_data['kinjun'].append(kinjun)
        self.candle_data['kinjun'].pop(0)

        self.candle_data['chiko'].append(chiko)
        self.candle_data['chiko'].pop(0)
