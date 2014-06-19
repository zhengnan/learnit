#!/usr/bin/env python
# -*- coding: utf-8 -*-

'A test of with statement'

__author__="focus"

class Test(object):
    def __init__(self, text):
        self.text=text
    def __enter__(self):
        self.text="ccc"
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.text="mmm"

def test():
    with Test("cgcg") as demo:
        print demo.text
    print demo.text

if __name__=='__main__':
    test()
