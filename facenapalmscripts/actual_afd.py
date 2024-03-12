#!/usr/bin/env python3
"""Update ruwiki's [[ВП:КУП]] shortcut to the actual 'Articles for deletion' page."""
import os
from pathlib import Path

# set the path to the user-config.py file before importing pywikibot
curdir = Path(__file__).parent.parent.absolute()
os.environ["PYWIKIBOT_DIR"] = str(curdir)

import pywikibot

TEXT = """#REDIRECT [[Википедия:К удалению/{{subst:#time:j xg Y}}]]"""

def main():
    """Main script function."""
    site = pywikibot.Site()
    site.login()
    page = pywikibot.Page(site, "Википедия:КУП")
    page.text = TEXT
    page.save("Обновление даты.")

if __name__ == "__main__":
    main()
