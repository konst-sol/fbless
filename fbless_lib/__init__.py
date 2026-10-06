#!/usr/bin/env python3
# -*- mode: python; coding: utf-8; -*-
# (c) Con Radchenko mailto:lankier@gmail.com

import sys
import locale
import contextlib
from io import StringIO
import curses

from fbless_lib.main import MainWindow

def main():
    locale.setlocale(locale.LC_ALL, '')

    log_buffer = StringIO()
    with contextlib.redirect_stdout(log_buffer):
        try:
            MainWindow().main_loop()
        finally:
            try:
                curses.endwin()
            except:
                pass

    value = log_buffer.getvalue()
    if value:
        print(value)

if __name__ == '__main__':
    main()
