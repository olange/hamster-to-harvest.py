#!/usr/bin/env python
# -*- coding: utf_8 -*-

from __future__ import print_function
import sys, codecs, logging, datetime
import hamster.db
import harvest.api
import cli, config

logging.basicConfig( level=logging.INFO)
logger = logging.getLogger( __name__)

def dump_fact( fact):
  print( u"{id} / start {start_time} duration {delta} {tags} {category}".format( **fact))

def list_facts( storage, date_start, date_end, search_terms):
  logger.info( "Retrieving facts '{query}' from {date_start} to {date_end}".format( query=search_terms, date_start=date_start, date_end=date_end))
  facts = storage.get_facts( date_start, date_end, search_terms)
  if not facts:
    print( "No matching facts.")
  else:
    for fact in facts:
      dump_fact( fact)

def dump_projects_and_tasks( harvest_client, stream=sys.stdout):
  logger.info( u"Retrieving Harvest tasks")
  print( u"\n[Harvest Tasks]", file=stream)
  for task in harvest_client.tasks():
    print( u"{0} ({1})".format( task.name, task.id), file=stream)

  logger.info( u"Retrieving Harvest projects and assignments")
  print( u"\n[Harvest Projects and Task assignments]", file=stream)
  for project in harvest_client.projects():
    print( u"Project {0} ({1})\n Client {2} ({3})".format(
           project.name, project.id, project.client.name, project.client.id), file=stream)
    for assignment in project.task_assignments:
      print( u"\t{0}".format( str( assignment)), file=stream)

def seed_tasks( config, harvest_client):
  """Seed the configuration file with the list of tasks IDs and names from Harvest."""
  config.remove_section( 'Harvest Tasks')
  config.add_section( 'Harvest Tasks')
  for task in harvest_client.tasks():
    task = vars( task)
    config.set( 'Harvest Tasks', task['name'], str( task['id']))
    logger.info( u"Harvest task {name} ({id})".format( **task))

def seed_projects( config, harvest_client):
  """Seed the configuration file with the list of project IDs and names from Harvest."""
  config.remove_section( 'Harvest Projects')
  config.add_section( 'Harvest Projects')
  for project in harvest_client.projects():
    project = vars( project)
    config.set( 'Harvest Projects', project['name'], str( project['id']))
    logger.info( u"Harvest project {name} ({id})".format( **project))

def main( argv):
  args = vars( cli.parser.parse_args( argv))
  logger.info( args)

  cfg = config.read( 'hamster-migrate.cfg')

#   hamster_db_dir = cfg.get( 'Hamster', 'database-dir')
#   logger.info( "Reading Hamster time entries from {database_dir}".format( database_dir=hamster_db_dir))
#   storage = hamster.db.Storage( database_dir=hamster_db_dir)
#   list_facts( storage, args['from'], args['to'], args['search'])

  harvest_url = cfg.get( 'Harvest', 'url')
  harvest_email = cfg.get( 'Harvest', 'email')
  harvest_pwd = cfg.get( 'Harvest', 'password')
  logger.info( "Accessing Harvest timesheet at {harvest_url}".format( harvest_url=harvest_url))
  harvest_client = harvest.api.Harvest( harvest_url, harvest_email, harvest_pwd)
  with codecs.open( "harvest-ids.txt", encoding='utf-8', mode='wb') as harvest_ids_file:
    dump_projects_and_tasks( harvest_client, harvest_ids_file)

#   config.write( cfg, 'hamster-migrate.cfg')

if __name__ == '__main__':
  main( sys.argv[1:])
