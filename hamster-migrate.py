#!/usr/bin/python
# -*- coding: utf_8 -*-

import sys, logging, datetime
import hamster.db
import cli

logging.basicConfig( level=logging.INFO)
logger = logging.getLogger( __name__)
storage = hamster.db.Storage( database_dir="./data")

def dump_fact( fact):
  print "{id} / {start_time} - {end_time} / {date} {delta} / {tags}".format( **fact)

def list_facts( date_start, date_end, search_terms):
  logger.info( "Looking for facts '{query}' from {date_start} to {date_end}".format( query=search_terms, date_start=date_start, date_end=date_end))
  facts = storage.get_facts( date_start, date_end, search_terms)
  if not facts:
    print "No matching facts."
  else:
    for fact in facts:
      dump_fact( fact)

def main( argv):
  args = vars( cli.parser.parse_args( argv))
  logger.info( args)
  list_facts( args['from'], args['to'], args['search'])

if __name__ == '__main__':
  main( sys.argv[1:])
