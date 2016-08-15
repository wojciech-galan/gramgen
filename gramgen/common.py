#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wgalan'


class Base(object):

    def __init__(self):
        super(Base, self).__init__()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class Node(Base):

    def __init__(self, content):
        super(Node, self).__init__()
        self.content = content

    def __repr__(self):
        return "Node('%s')" %self.content

    def __str__(self):
        return self.content


class BaseProduction(Base):

    def __init__(self, pre, post):
        super(BaseProduction, self).__init__()
        self.pre = pre
        self.post = post

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, str(self.pre), str(self.post))


class BaseAutomate(Base):

    def __init__(self, *productions):
        super(BaseAutomate, self).__init__()
        assert all(isinstance(p, BaseProduction) for p in productions)
        self.productions = productions
        self.terminals = detectTerminals(productions)


def listReplaceLastElement(in_list, from_, to_):
    """
    Zmienia ostatni element listy z from_ na element(y) zawarte w liście to_
    :param in_list:
    :param from_:
    :param to_:
    :return:
    """
    assert type(in_list) is list
    assert type(to_) is list
    if in_list[-1] == from_:
        out = in_list[:-1]
        out.extend(to_)
        return out
    else:
        return in_list

def listReplaceElement(in_list, from_, to_):
    """
    Zmienia element listy in_list z from_ na element(y) zawarte w liście to_
    :param in_list:
    :param from_:
    :param to_:
    :return:
    """
    assert type(in_list) is list
    assert type(to_) is list
    if from_ in in_list:
        out = in_list[:]
        ind = in_list.index(from_)
        out[ind] = to_[0]
        for element in to_[1:]:
            out.insert(ind, element)
            ind += 1
        return out
    else:
        return in_list


def detectTerminals(productions):
    probably_nonterminals = []
    pres = []
    ret_val = []
    for p in  productions:
        probably_nonterminals.extend(p.post)
        pres.append(p.pre)
    for probably_nonterminal in set(probably_nonterminals):
        if probably_nonterminal not in pres:
            ret_val.append(probably_nonterminal)
    return ret_val


if __name__ == '__main__':
    pass