#!/usr/bin/env bash
# Creates epydoc HTML and text for our module.
epydoc eat.py
epydoc --text eat.py > README.txt
