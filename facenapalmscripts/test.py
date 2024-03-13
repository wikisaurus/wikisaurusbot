#!/usr/bin/env python3
"""
Tiny test script which tries to edit sandbox in ruwiki to make sure that
everything is ok.
"""
from pathlib import Path

# set the path to the user-config.py file before importing pywikibot
curdir = Path(__file__).parent.parent.absolute()
os.environ["PYWIKIBOT_DIR"] = str(curdir)

import pywikibot

site = pywikibot.Site()
site.login()
page = pywikibot.Page(site, "Википедия:Песочница")
page.text = page.text + "\n\nHello, world!"
page.save("WMFlabs test.")
