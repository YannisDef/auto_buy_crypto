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
    Milieu entre la valeur du plus haut et la valeur du plus bas sur les 9 dernières périodes observées.

    Args:
        data (list): liste de valeur

    Returns:
        _type_: moyenne entre la valeur la plus haute et la plus basse
    """
    if len(dataHigh) < idx:
        print(f'tenkanSen: No many data {len(dataHigh)}', file=sys.stderr)
        return ERROR
    return (max(dataHigh[:idx]) + min(dataLow[:idx])) / 2


def kijunSen(dataHigh: list, dataLow: list, idx: int = 26):
    """
    Milieu entre la valeur du plus haut et la valeur du plus bas sur les 26 dernières périodes observées.

    Args:
        data (list): liste de valeur
        idx (int, optional): nb de bougies précédentes a analiser. Defaults to 26.

    Returns:
        _type_: moyenne du maximum et minimum
    """
    if len(dataHigh) < idx:
        print(f"kijunSen: No many data {len(dataHigh)}", file=sys.stderr)
        return ERROR
    return (max(dataHigh[:idx]) + min(dataLow[:idx])) / 2


def chikoSpan(dataClose: list, idx: int = 26):
    """
    Correspond au dernier prix de clôture projeté 26 périodes en arrière

    Args:
        dataClose (list): liste de valeur
        idx (int, optional): nb de bougies précédentes a analiser. Defaults to 26.

    Returns:
        _type_: dernier prix de cloture
    """
    if len(dataClose) < idx:
        print('chikoSpan: No many data', file=sys.stderr)
        return ERROR
    return dataClose[-idx]


def senkoSpanA(dataHigh: list, dataLow: list):
    """
    Première frontière du nuage. (SSA)
    Il s'agit du milieu de la Tenkan et de la Kijun projeté 26 périodes en avant.

    Args:
        data (list): liste de valeur

    Returns:
        _type_: moyenne
    """
    if len(dataHigh) < 26:
        print('senkoSpanA: No many data', file=sys.stderr)
        return ERROR
    return (tenkanSen(dataHigh, dataLow) + kijunSen(dataHigh, dataLow)) / 2


def senkoSpanB(dataHigh: list, dataLow: list):
    """
    Deuxième frontière du nuage. (SSB)
    Il s'agit du milieu du plus haut et du plus bas des 52 dernières périodes, projeté 26 périodes en avant.
    La SSB est une ligne « plus forte » que la SSA dans le sens où sa période est plus grande.
    En d'autres termes, elle est plus difficile à traverser et peut faire office de support/résistance.

    Args:
        data (list): liste de valeur

    Returns:
        _type_: moyenne
    """
    if len(dataHigh) < 52:
        print('senkoSpanB: No many data', file=sys.stderr)
        return ERROR
    return tenkanSen(dataHigh, dataLow, 52)
