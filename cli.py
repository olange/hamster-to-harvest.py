#!/usr/bin/python
# -*- coding: utf_8 -*-

import argparse
import datetime

def isodate( date_string):
  """Given a string representing a date in either the format YYYYMMDD
  or YYYY-MM-DD, return a corresponding `datetime.date` Object."""
  try:
    dt = datetime.datetime.strptime( date_string, "%Y-%m-%d")
  except ValueError:
    dt = datetime.datetime.strptime( date_string, "%Y%m%d")
  return dt.date()

def setup_parser():
  """Create and return an argument parser to read from the command-line
  the specific flags and subcommands of the migration script."""

  parser = argparse.ArgumentParser( description="Migrate Hamster time tracking entries to Harvest.")
  subparsers = parser.add_subparsers( dest="subcommand", title="subcommands", help="Additional help")

  # Subcommand 'migrate'
  migrate = subparsers.add_parser( "migrate")
  migrate.add_argument( "--start", required=True, metavar="DATE", type=isodate,
                        help="Start date to filter entries (YYYY-MM-DD); mandatory")
  migrate.add_argument( "--end", default=None, metavar="DATE", type=isodate,
                        help="End date to filter entries (YYYY-MM-DD); if not specified, "
                             "defaults to the from date")
  migrate.add_argument( "--search", default="", metavar="TERMS",
                        help="Select the activities matching a list of words, "
                             "separated by space (AND) or commas (OR); '*' acts "
                             "as a wildcard; for instance: 'RZO* -PAGLadmin'")
  migrate.add_argument( "--prune", default=False, action="store_true",
                        help="Remove from the Hamster database those time entries that "
                             "were migrated to Harvest; nothing is removed by default")
  migrate.add_argument( "--dry-run", default=False, action="store_true",
                        help="Shows what would happen with the given parameters, but do "
                             "not actually commit any change to the Hamster database or "
                             "to the Harvest dataset")
  # Subcommand 'seed'
  parser_seed = subparsers.add_parser( "seed")

  return parser

parser = setup_parser()
