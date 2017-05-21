# coding=utf-8

import operator as op


def generate_site_name(name):
    words = name.replace('-', ' ').replace('_', ' ').split()
    return ' '.join(map(str.title, words))


def generate_site_brand(name):
    words = name.replace('-', ' ').replace('_', ' ').split()
    return str.upper('SYS ' + ''.join(map(op.itemgetter(0), words)))
