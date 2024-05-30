#!/usr/bin/env python3
"""
Maintainer script for ruwiki's {{очищать кэш}} aka {{autopurge}} template.

Usage:
    python autopurge.py [--hourly] [--daily] [--null]

Each key process one category, see template documentation; period should be correctly set via crontab.
"""
import sys
from pathlib import Path
import pywikibot
import pywikibot.exceptions
import logging

# manually load the auth
curdir = Path(__file__).parent.parent.absolute()
userfile = curdir / "user-config.py"
exec(compile(userfile.read_text(), str(userfile), "exec"), vars(pywikibot.config))

def process_purge(site, catname, limit=50):
    """Purge all pages from category and return status for logging."""
    members = list(pywikibot.Category(site, catname).members())
    length = len(members)
    for i in range(0, length, limit):
        try:
            if not site.purgepages(members[i : i + limit]):
                return "неожиданный ответ сервера"
        except Exception as error:
            logging.error(
                "Failed trying to purge members %d to %d for category %s: %s",
                i,
                i + limit,
                catname,
                str(error),
            )
            raise
    return str(length)

def process_hourly(site):
    return "срочных: " + process_purge(
        site, "К:Википедия:Страницы с ежечасно очищаемым кэшем"
    )

def process_daily(site):
    return "ежедневных: " + process_purge(
        site, "К:Википедия:Страницы с ежедневно очищаемым кэшем"
    )

def process_null(site):
    catname = "К:Википедия:Страницы с ежедневно совершаемой нулевой правкой"
    members = list(pywikibot.Category(site, catname).members())
    errors = 0
    for page in members:
        try:
            # if page was deleted while script is working, touch() can create empty page (WHY?!)
            # temporary pywikibot.Page() object initialization should fix this problem
            temp = pywikibot.Page(site, page.title())
            temp.touch()
        except pywikibot.exceptions.LockedPage:
            errors += 1
    return "нулевых правок: " + str(len(members) - errors)

KEYS = {"--hourly": process_hourly, "--daily": process_daily, "--null": process_null}

def main():
    """Get console arguments and call corresponding fucntions."""
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.ERROR,
    )
    if len(sys.argv) == 1:
        return
    args = sys.argv[1:]
    site = pywikibot.Site()
    site.login()
    respond = []
    for arg in args:
        if arg in KEYS:
            respond.append(KEYS[arg](site))

if __name__ == "__main__":
    main()
