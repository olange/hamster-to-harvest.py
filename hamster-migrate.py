#!/usr/bin/env python
# -*- coding: utf_8 -*-

import sys, codecs, logging, datetime
import hamster.db, api.harvest, api.harvest_time_tracking
import cli, options, commands

logging.basicConfig( level=logging.INFO)
logger = logging.getLogger( __name__)

def seed( args, opts):
  harvest_url = opts.get( "Harvest", "url")
  harvest_email = opts.get( "Harvest", "email")
  harvest_pwd = opts.get( "Harvest", "password")
  logger.info( u"Accessing Harvest at {0}".format( harvest_url))
  harvest_client = api.harvest.Harvest( harvest_url, harvest_email, harvest_pwd)
  with codecs.open( "harvest-ids.txt", encoding='utf-8', mode='wb') as harvest_ids_file:
    commands.seed.dump_projects_and_tasks( harvest_client, harvest_ids_file)

def migrate( args, opts):
  harvest_url = opts.get( "Harvest", "url")
  harvest_email = opts.get( "Harvest", "email")
  harvest_pwd = opts.get( "Harvest", "password")
  logger.info( u"Accessing Harvest timesheet at {0}".format( harvest_url))
  harvest_client = api.harvest_time_tracking.Harvest( harvest_url, harvest_email, harvest_pwd)
  logger.info( harvest_client.get_today())

  hamster_db_dir = opts.get( "Hamster", "database-dir")
  logger.info( u"Reading Hamster time entries from {0}".format( hamster_db_dir))
  storage = hamster.db.Storage( database_dir=hamster_db_dir)
  commands.migrate.list_facts( storage, args.start, args.end, args.search)

def main( argv):
  """Parse the command-line args and call the function matching
  the subcommand that was selected."""
  opts = options.read( "hamster-migrate.cfg")

  args = cli.parser.parse_args( argv)
  logger.info( args)

  subcommands = { "seed": seed, "migrate": migrate }
  subcommands[ args.subcommand]( args, opts)

if __name__ == '__main__':
  main( sys.argv[1:])
