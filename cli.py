#!/usr/bin/python
# -*- coding: utf_8 -*-

import argparse
import datetime

def isodate( date_string):
  try:
    dt = datetime.datetime.strptime( date_string, "%Y-%m-%d")
  except ValueError:
    dt = datetime.datetime.strptime( date_string, "%Y%m%d")
  return dt.date()

parser = argparse.ArgumentParser( description="Migrate Hamster time tracking entries to Harvest.")

parser.add_argument( "--from", required=True, metavar="DATE", type=isodate,
                     help="Start date to filter entries; mandatory")
parser.add_argument( "--to", default=None, metavar="DATE", type=isodate,
                     help="End date to filter entries; defaults to none")
parser.add_argument( "--search", default="", metavar="TERMS",
                     help="Select the activities matching a list of words, separated by space (AND) "
                          "or commas (OR); use '*' acts as a wildchar; for instance: 'RZO* -PAGLadmin'")
parser.add_argument( "--prune", default=False, action="store_const", const=True,
                     help="Remove from the Hamster database those time entries that were migrated "
                          "to Harvest; nothing is removed by default")
parser.add_argument( "--dry-run", default=False, action="store_const", const=True,
                     help="Shows what would happen with the given parameters, but do not actually "
                          "commit any change to the Hamster database or to the Harvest dataset")
