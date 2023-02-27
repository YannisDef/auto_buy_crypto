#!/usr/bin/env python3
#
# PERSONNAL PROJECT, 2023
# Trade bot with Bitcoin
# File description:
# Ichimoku function
#

import sys

ERROR = 84


def tenkanSen(dataHigh: list, dataLow: list, idx: int = 9):
    """
    Middle between the highest value and the lowest value over the last 9 periods observed.

    Args:
        data (list): list of values

    Returns:
        float: average between the highest and lowest value
    """
    if len(dataHigh) < idx:
        print(f'tenkanSen: No many data {len(dataHigh)}', file=sys.stderr)
        return ERROR
    return (max(dataHigh[:idx]) + min(dataLow[:idx])) / 2


def kijunSen(dataHigh: list, dataLow: list, idx: int = 26):
    """
    Middle between the highest value and the lowest value over the last 26 periods observed.

    Args:
        data (list): list of values
        idx (int, optional): number of previous candles to analyze. Defaults to 26.

    Returns:
        float: average of maximum and minimum
    """
    if len(dataHigh) < idx:
        print(f"kijunSen: No many data {len(dataHigh)}", file=sys.stderr)
        return ERROR
    return (max(dataHigh[:idx]) + min(dataLow[:idx])) / 2


def chikoSpan(dataClose: list, idx: int = 26):
    """
    Corresponds to the last closing price projected 26 periods back

    Args:
        dataClose (list): list of values
        idx (int, optional): number of previous candles to analyze. Defaults to 26.

    Returns:
        float: last closing price
    """
    if len(dataClose) < idx:
        print('chikoSpan: No many data', file=sys.stderr)
        return ERROR
    return dataClose[-idx]


def senkoSpanA(dataHigh: list, dataLow: list):
    """
    First frontier of the cloud. (SSA)
    This is the middle of the Tenkan and the Kijun projected 26 periods forward.

    Args:
        data (list): list of values

    Returns:
        float: average
    """
    if len(dataHigh) < 26:
        print('senkoSpanA: No many data', file=sys.stderr)
        return ERROR
    return (tenkanSen(dataHigh, dataLow) + kijunSen(dataHigh, dataLow)) / 2


def senkoSpanB(dataHigh: list, dataLow: list):
    """
    Second frontier of the cloud. (SSB)
    This is the midpoint of the 52-period high and low, projected 26 periods forward.
    The SSB is a “stronger” line than the SSA in the sense that its period is larger.
    In other words, it is more difficult to cross and can act as support/resistance.

    Args:
        data (list): list of values

    Returns:
        float: average
    """
    if len(dataHigh) < 52:
        print('senkoSpanB: No many data', file=sys.stderr)
        return ERROR
    return tenkanSen(dataHigh, dataLow, 52)
