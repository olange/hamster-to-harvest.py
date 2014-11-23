#!/usr/bin/env python
# -*- coding: utf_8 -*-

import ConfigParser
import codecs

def read( config_filename='hamster-migrate.cfg'):
  cfg = ConfigParser.RawConfigParser()
  cfg.read( config_filename)
  return cfg

def write( cfg, config_filename='hamster-migrate.cfg'):
  with codecs.open( config_filename, encoding='utf-8', mode='wb') as cfg_file:
    cfg.write( cfg_file)
