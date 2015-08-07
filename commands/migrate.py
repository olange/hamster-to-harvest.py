# -*- coding: utf_8 -*-

from __future__ import print_function
import logging

logger = logging.getLogger( __name__)

class HarvestTask():
  """An Harvest Task entity. Just a set of attributes."""

  def __init__( self):
    self.note = None
    self.project_id = None
    self.task_id = None
    self.spent_at = None
    self.started_at = None
    self.ended_at = None

  def __str__( self):
    return u"p{0.project_id} t{0.task_id} / {0.spent_at} {0.started_at} - {0.ended_at} / {0.note}".format( self)

def task_and_project_mapping( fact):
  """Given a Fact entity from Hamster, return a tuple with the task and project ids
  matching the fact attributes -- namely from its name, category and tags."""
  # Target Task
  task_id = None
  project_id = 6882158 # Migration Hamster

  # Source Fact
  name = fact.get( "name")
  tags = fact.get( "tags")

  # Mapping
  if name == u"KLMwebdev":
    project_id = 2775024
    if u"Support" in tags:
      task_id = 1378870
    elif u"Publication" in tags:
      task_id = 1680283
    elif u"Strat\xe9gie et prospection" in tags:
      task_id = 1680283
  return (task_id, project_id)

def fact_to_task( fact):
  """Given an Hamster Fact entity, migrate its contents to a new Harvest Task entity.

  The Fact entity should be a dictionary with following attributes (as returned by
  the Hamster API):

  { 'id': 2901, 'name': u'KLMwebdev',
    'category': u'work', 'activity_id': 47,
    'tags': [u'Support'], 'tag': u'Support',
    'description': u'Cr\xe9ation dossier ...',
    'date': datetime.date(2011, 8, 17),
    'start_time': datetime.datetime( 2011, 8, 17, 17, 40),
    'end_time': datetime.datetime( 2011, 8, 17, 18, 0),
    'delta': datetime.timedelta( 0, 1200) }
  """
  task = HarvestTask()
  task.note = u"[{0}] {1}".format( fact.get("category", ""), fact.get( "description", ""))
  task.spent_at = u"{:%Y-%m-%d}".format( fact.get( "start_time"))
  task.started_at = u"{:%H:%M}".format( fact.get( "start_time"))
  task.ended_at = u"{:%H:%M}".format( fact.get( "end_time"))
  task.task_id, task.project_id = task_and_project_mapping( fact)
  return task

def upload_task( harvest_time_tracking_api, task):
  """Given a connection to the Harvest Time Tracking API and a task entity,
     add it to the timesheet (thru a POST request)."""
  data = { "notes": unicode( task.note),
           "project_id": unicode( task.project_id),
           "task_id": unicode( task.task_id),
           "started_at": unicode( task.started_at),
           "ended_at": unicode( task.ended_at),
           "spent_at": unicode( task.spent_at) }
  return harvest_time_tracking_api.add( data)
