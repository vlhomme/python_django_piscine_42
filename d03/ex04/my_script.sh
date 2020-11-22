#!/bin/bash

virtualenv django_venv
pip install -r django_venv/requirement.txt
source django_venv/bin/activate
