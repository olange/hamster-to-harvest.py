#!/usr/bin/python
# -*- coding: utf_8 -*-
# $Id: hamster-update.py 429 2011-11-07 11:36:34Z olange@petit-atelier.ch $

import hamster.db
import datetime

storage = hamster.db.Storage( database_dir="./data")

date_start = datetime.date( 2011, 01, 01)
date_end = datetime.date( 2011, 10, 31)

facts = storage.get_facts( date_start, date_end, "RZO*")

for fact in facts:
  print "{id} / {start_time} - {end_time} / {date} {delta} / {tags}".format( **fact)

#   self.activity = None
#   self.category = None
#   self.description = None
#   self.tags = []
#   self.start_time = None
#   self.end_time = None
#   self.id = id
#   self.ponies = False
#   self.delta = delta
#   self.date = date
#   self.activity_id = activity_id
