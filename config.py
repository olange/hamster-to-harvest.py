#!/usr/bin/python
# -*- coding: utf_8 -*-

import ConfigParser

def read( config_filename='hamster-migrate.cfg'):
  cfg = ConfigParser.RawConfigParser()
  cfg.read( config_filename)
  return cfg
