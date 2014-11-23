#!/usr/bin/env python
# -*- coding: utf_8 -*-

import ConfigParser
import codecs
import logging

logger = logging.getLogger( __name__)

def read( config_filename="hamster-migrate.cfg"):
  logger.info( u"Reading configuration from {0}".format( config_filename))
  cfg = ConfigParser.RawConfigParser()
  cfg.read( config_filename)
  return cfg

def write( cfg, config_filename="hamster-migrate.cfg"):
  logger.info( u"Writing configuration to {0}".format( config_filename))
  with codecs.open( config_filename, encoding="utf-8", mode="wb") as cfg_file:
    cfg.write( cfg_file)
