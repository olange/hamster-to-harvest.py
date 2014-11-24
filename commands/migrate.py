# -*- coding: utf_8 -*-

from __future__ import print_function
import logging

logger = logging.getLogger( __name__)

def dump_fact( fact):
  print( u"Fact {id} / {start_time} / {delta} / {tags} {category} / {description}".format( **fact))

def list_facts( storage, date_start, date_end, search_terms):
  logger.info( "Retrieving facts '{0}' from {1} to {2}".format( search_terms, date_start, date_end))
  facts = storage.get_facts( date_start, date_end, search_terms)
  if not facts:
    print( "No matching facts.")
  else:
    for fact in facts:
      dump_fact( fact)
