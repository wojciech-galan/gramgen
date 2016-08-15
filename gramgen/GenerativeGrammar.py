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


import pdb
from common import *

# jest to moduł, który dostaje już zdanie o określonej strukturze, wykonuje tylko punktowe podstawienia

class Production(BaseProduction):

    def __init__(self, pre, post):
        super(Production, self).__init__(pre, post)

    def __call__(self, input_):
        #return input.replace(self.pre, self.post)
        return listReplaceElement(input_, self.pre, self.post)


class Automate(BaseAutomate):

    def __init__(self, *productions):
        assert all(type(production) is Production for production in productions)
        super(Automate, self).__init__(*productions)

    def __call__(self, start, level=2, toString=False, accept_nonterminals=True):
        ret_val = []
        _produce(start, self.productions, self.terminals, level, ret_val, accept_nonterminals)
        # ret_val = [sentence for sentence in ret_val if all(node not in self.nonterminals for node in sentence)]# TODO temp solution - eliminacja nieterminali. powinno to być robione inaczej
        if toString:
            return '\n'.join(toString.join(str(e) for e in element) for element in ret_val), len(ret_val)
        return ret_val, len(ret_val)

    def produce(self, sentences, level=2, toString=False, accept_nonterminals=True):
        """
        Wywołuje produkcje na już istniejących zdaniach
        :param sentences:
        :param level:
        :return:
        """
        if accept_nonterminals:
            result = sentences[:]
        else:
            result=[]
        non_terminals = [prod.pre for prod in self.productions]
        for sentence in sentences:
            res = []
            terminals = self.terminals[:]
            terminals.extend([node for node in sentence if node not in non_terminals])
            _produce(sentence, self.productions, terminals, level, res, accept_nonterminals)
            result.extend(res)
        if toString:
            return '\n'.join(toString.join(str(e) for e in element) for element in result), len(result)
        return result, len(result)


def _produce(start, productions, terminals, length, res=[], accept_nonterminals=True):
    if len(start)<=length:
        productions_of_interest = [p for p in productions if p.pre in start]
        for prod_of_interest in productions_of_interest:
            # result - zdanie utworzone na podstawie zdania start i produkcji prod_of_interest
            result = prod_of_interest(start)
            # TODO do refaktoryzacji!
            if result not in res and len(result) <= length:
                if accept_nonterminals:
                    if any(r not in terminals for r in result):
                        _produce(result, productions, terminals, length, res, accept_nonterminals)
                    res.append(result)
                else:
                    if all(r in terminals for r in result):
                        res.append(result)
                    else:
                        _produce(result, productions, terminals, length, res, accept_nonterminals)
            else:
                _produce(result, productions, terminals, length, res, accept_nonterminals)


if __name__ == '__main__':
    pass