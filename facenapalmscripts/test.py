#!/usr/bin/env python3
"""
Tiny test script which tries to edit sandbox in ruwiki to make sure that
everything is ok.
"""
import pywikibot
site = pywikibot.Site()
site.login()
page = pywikibot.Page(site, "Википедия:Песочница")
page.text = page.text + "\n\nHello, world!"
page.save("WMFlabs test.")
