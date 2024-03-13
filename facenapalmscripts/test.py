#!/usr/bin/env python3
"""
Tiny test script which tries to edit sandbox in ruwiki to make sure that
everything is ok.
"""
from pathlib import Path
import pywikibot

# manually load the auth
curdir = Path(__file__).parent.parent.absolute()
userfile = curdir / "user-config.py"
exec(compile(userfile.read_text(), str(userfile), 'exec'), vars(pywikibot.config))

site = pywikibot.Site()
site.login()
page = pywikibot.Page(site, "Википедия:Песочница")
page.text = page.text + "\n\nHello, world!"
page.save("WMFlabs test.")
