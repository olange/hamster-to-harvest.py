# -*- coding: utf-8 -*-

# The Harvest Time Tracking API offers read/write access to the Time Tracking entities.
# The Python Harvest API Wrapper offers read-only access to all entities of Harvest.
# So I needed both.

# Harvest Time Tracking API
# https://github.com/lionheart/python-harvest
#
# The file 'harvest_time_tracking.py' of this directory is a copy of:
#
#   https://github.com/lionheart/python-harvest/blob/master/harvest/harvest.py
#
# with a slight modification to further fix an issue. I embedded it because it
# can't currently be installed with 'pip install' and added to the requirements.
# (see https://github.com/lionheart/python-harvest/issues/1 and 2).
# Credits go to the authors.

from . import harvest_time_tracking

# Python Harvest API Wrapper
# https://github.com/lann/Harvest
#
# The file 'harvest.py' of this directory is a copy of:
#
#   https://github.com/lann/Harvest/blob/master/harvest.py
#
# which I embedded, because it was not available for installation
# with 'pip install'. Credits go to the authors.

from . import harvest
