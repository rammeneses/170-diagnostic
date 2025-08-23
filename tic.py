# Raphael Andrei M. Meneses
# 2022-13211
# GH-2L
# NOTE: I can't find the statement on the Responsible Use of AI in the Course Guide

import os
from ctypes import windll

# Clear Terminal taken from:
# https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

