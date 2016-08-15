#! /usr/bin/python
# -*- coding: utf-8 -*-

    # This file is a part of an library named gramgen
    # If you have any questions and/or comments, don't hesitate to
    # contact me by email wojciech.galan@gmail.com
    #
    # Copyright (C) 2016  Wojciech Gałan
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>


# produkcje stosujemy tylko na końcu

from common import *


class RegularAutomate(BaseAutomate):

    def __init__(self, *productions):
        """

        :param productions: - obiekty typu RegularProduction
        :return:
        """
        super(RegularAutomate, self).__init__(*productions)

    def __call__(self, start, level=2, toString=False):
        ret_val = []
        _produce(start, self.productions, self.terminals, level, ret_val)
        if toString:
            return '\n'.join(toString.join(str(e) for e in element) for element in ret_val), len(ret_val)
        return ret_val, len(ret_val)


class RegularProduction(BaseProduction):

    def __init__(self, pre, post):
        super(RegularProduction, self).__init__(pre, post)

    def __call__(self, input_):
        return listReplaceLastElement(input_, self.pre, self.post)


def _produce(start, productions, terminals, length, res=[]):
    """
    funkcja uruchaniająca rekurencyjnie produkcje na ostalnim elemencie listy 'start'
    :param start: lista node'ów, na której wywołujemy produkcje
    :param productions: lista produkcji
    :param terminals: lista terminali
    :param length: max długość zdania
    :param res: akumulator wyników
    :return: nie zwraca nic. Lista otrzymanych zdań znajduje się w res
    """
    if len(start)<=length:
        productions_of_interest = [p for p in productions if p.pre == start[-1]]
        for prod_of_interest in productions_of_interest:
            result = prod_of_interest(start)
            #print result
            if result not in res and len(result) <= length and result[-1] in terminals:
                res.append(result)
            else:
                _produce(result, productions, terminals, length, res)


if __name__ == '__main__':
    pass