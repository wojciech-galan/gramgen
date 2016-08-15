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

from common import Node
from RegularGenerativeGrammar import RegularProduction
from GenerativeGrammar import Production


def prodParser(prod_type, delimiter='|', sub_delimiter=' '):
    def ret(text):
        assert text.count(delimiter) == 1
        pre, post = text.split(delimiter)
        assert pre
        # pre should contain only one element
        assert not pre.count(delimiter)
        eval_str = "%s(%r, %r)"%(prod_type, Node(pre), [Node('%s'%x) for x in post.split(sub_delimiter)])
        # print eval_str
        return eval(eval_str)
    return ret

def readProductions(mark_ignore='#', *paths):
    """
    Czyta pliki, zwraca tekst składający się z ninii, które nie zaczynają się od mark_ignore
    :param path: ścieżka do pliku
    :param mark_ignore: marker, który mówi, że nalezy zignorować daną linię
    :return: linie tekstu, które powinny być brane pod uwagę
    """
    ret_list = []
    for path in paths:
        ret_list.extend([line.strip() for line in open(path) if line.strip() and not line.startswith(mark_ignore)])
    return ret_list


if __name__ == '__main__':
    pass