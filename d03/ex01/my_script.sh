#!/bin/sh
pip -V
pip install --upgrade -t ./local_lib  git+https://github.com/jaraco/path --log ./log.log && python3 my_program.py