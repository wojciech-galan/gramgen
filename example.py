#! /usr/bin/python
# -*- coding: utf-8 -*-

""" This file is a part of an library named gramgen
    If you have any questions and/or comments, don't hesitate to 
    contact me by email wojciech.galan@gmail.com
    
    Copyright (C) 2016  Wojciech Gałan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>"""

import os
from gramgen.ProdParser import prodParser, readProductions
from gramgen.RegularGenerativeGrammar import RegularAutomate
from gramgen.GenerativeGrammar import Automate
from gramgen.common import Node

if __name__ == '__main__':
    r_parser = prodParser('RegularProduction')
    sentence_productions_path = os.path.join(os.path.dirname(__file__), 'example_productions', 'sentence')
    ra = RegularAutomate(*[r_parser(line) for line in readProductions('#', sentence_productions_path)])
    sentences, how_much = ra([Node('START')], level=4, toString=' ')
    print sentences
    print how_much
    print '---------------------------------------'
    sentences, _ = ra([Node('START')], level=4, toString=False)
    print sentences
    print '---------------------------------------'
    parser = prodParser('Production')
    sentence_productions_details_path = os.path.join(os.path.dirname(__file__), 'example_productions', 'sentence_details')
    a = Automate(*[parser(line) for line in readProductions('#', sentence_productions_details_path)])
    sentences, ile = a(sentences[0], level=4, toString=' ', accept_nonterminals=False)
    print sentences
