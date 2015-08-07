#!/usr/bin/env python
# -*- coding: utf_8 -*-

import sys, codecs, logging, datetime
import hamster.db, api.harvest, api.harvest_time_tracking
import options, commands

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

def explore( args, opts):
  storage = hamster.db.Storage( database_dir=opts.get( "Hamster", "database-dir"))
  commands.explore.list_facts( storage, args.start, args.end, args.search)

def migrate( args, opts):
  hamster_db_dir = opts.get( "Hamster", "database-dir")
  harvest_url = opts.get( "Harvest", "url")
  harvest_email = opts.get( "Harvest", "email")
  harvest_pwd = opts.get( "Harvest", "password")

  print( u"Retrieving Hamster time entries from {0}".format( hamster_db_dir))
  storage = hamster.db.Storage( database_dir=hamster_db_dir)

  start_date = args.start
  end_date = args.end
  search_terms = args.search
  facts = storage.get_facts( start_date, end_date, search_terms)
  print( u"Found {0} time entries matching '{1}' between {2} and {3} ..."
          .format( len( facts), search_terms, start_date, end_date))

  print( u"Accessing Harvest timesheet at {0}".format( harvest_url))
  harvest_tt_api = api.harvest_time_tracking.Harvest( harvest_url, harvest_email, harvest_pwd)

  for fact in facts:
    task = commands.migrate.fact_to_task( fact)
    print( u"Uploading {0}".format( task))
    result = commands.migrate.upload_task( harvest_tt_api, task)
    if u"id" in result:
      print u"Successfull; task was assigned ID {0}".format( result.get(u"id"))
      # TODO: Prune entry from Hamster DB
    else:
      print u"Upload failed: {0}".format( result)

  print "Done."

def main( argv):
  """Parse the command-line args and call the function matching
  the subcommand that was selected."""
  opts = options.opts.read( "hamster-migrate.cfg")

  args = options.cli.parser.parse_args( argv)
  logger.info( args)

  subcommands = { "seed": seed, "migrate": migrate }
  subcommands[ args.subcommand]( args, opts)

if __name__ == '__main__':
  main( sys.argv[1:])
