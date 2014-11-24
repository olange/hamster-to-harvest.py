# -*- coding: utf_8 -*-

from __future__ import print_function
import sys, logging

logger = logging.getLogger( __name__)

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

def seed_tasks( opts, harvest_client):
  """Seed the configuration file with the list of tasks IDs and names from Harvest."""
  opts.remove_section( "Harvest Tasks")
  opts.add_section( "Harvest Tasks")
  for task in harvest_client.tasks():
    task = vars( task)
    opts.set( "Harvest Tasks", task["name"], str( task["id"]))
    logger.info( u"Harvest task {name} ({id})".format( **task))

def seed_projects( opts, harvest_client):
  """Seed the configuration file with the list of project IDs and names from Harvest."""
  opts.remove_section( "Harvest Projects")
  opts.add_section( "Harvest Projects")
  for project in harvest_client.projects():
    project = vars( project)
    opts.set( "Harvest Projects", project["name"], str( project["id"]))
    logger.info( u"Harvest project {name} ({id})".format( **project))

