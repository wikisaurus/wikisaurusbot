#!/usr/bin/env python3
"""Update ruwiki's [[ВП:КУП]] shortcut to the actual 'Articles for deletion' page."""
import pywikibot
from pathlib import Path

# manually load the auth
curdir = Path(__file__).parent.parent.absolute()
userfile = curdir / "user-config.py"
exec(compile(userfile.read_text(), str(userfile), 'exec'), vars(pywikibot.config))


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
