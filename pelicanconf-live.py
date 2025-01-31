"""This config is used when you run `make live`.

It inherits most of the settings from pelicanconf.py.
"""
from __future__ import unicode_literals

# First load all the defaults from pelicanconf.py
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

CACHE_CONTENT = False

ANALYTICS = ("""<script language="javascript" id="_fed_an_ua_tag" src="//dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=NASA"></script>""",
             """<script language="javascript" id="_fed_an_ua_tag" src="//dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=NASA&subagency=GSFC&dclink=true"></script>""")
