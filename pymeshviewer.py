#!/usr/bin/env python
# coding: utf-8
#from tkinterview import load, main
from win32view import load, main

import sys

if __name__ == '__main__':
    if len(sys.argv)>1:
        load(sys.argv[1])
    main(600, 600)

