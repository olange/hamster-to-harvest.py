#!/usr/bin/python
# -*- coding: utf_8 -*-

import sys, logging, datetime
import hamster.db
import harvest.api
import cli, config

logging.basicConfig( level=logging.INFO)
logger = logging.getLogger( __name__)

def dump_fact( fact):
  print "{id} / {start_time} - {end_time} / {date} {delta} / {tags}".format( **fact)

def list_facts( storage, date_start, date_end, search_terms):
  logger.info( "Retrieving facts '{query}' from {date_start} to {date_end}".format( query=search_terms, date_start=date_start, date_end=date_end))
  facts = storage.get_facts( date_start, date_end, search_terms)
  if not facts:
    print "No matching facts."
  else:
    for fact in facts:
      dump_fact( fact)

def main( argv):
  args = vars( cli.parser.parse_args( argv))
  logger.info( args)

  cfg = config.read( 'hamster-migrate.cfg')
  hamster_db_dir = cfg.get( 'Hamster', 'database-dir')
  logger.info( "Reading Hamster time entries from {database_dir}".format( database_dir=hamster_db_dir))
  storage = hamster.db.Storage( database_dir=hamster_db_dir)

  list_facts( storage, args['from'], args['to'], args['search'])

  harvest_url = cfg.get( 'Harvest', 'url')
  harvest_email = cfg.get( 'Harvest', 'email')
  harvest_pwd = cfg.get( 'Harvest', 'password')
  logger.info( "Accessing Harvest timesheet at {harvest_url}".format( harvest_url=harvest_url))
  harvest = harvest.api.Harvest( harvest_url, harvest_email, harvest_pwd)

  print( harvest.get_today())

if __name__ == '__main__':
  main( sys.argv[1:])
