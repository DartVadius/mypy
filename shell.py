#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import readline
from pprint import pprint

from flask import *
from app import *
from wtforms import Form, BooleanField, StringField, validators

os.environ['PYTHONINSPECT'] = 'True'
