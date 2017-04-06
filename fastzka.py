"""
Maintainer script for ruwiki's admin request table ([[:ru:ВП:ЗКАБ]]).

Usage:
    python fastzka.py
"""

import re
from datetime import datetime
import pywikibot

REGEXP = re.compile(r"""
    (?P<indent>\n*)
    ==\s*(?P<header>.*?)\s*==\s+
    (?P<section>
        <onlyinclude>\s*
        (?:[^<]|<(?!/?onlyinclude))*?\s*
        </onlyinclude>
    )
""", re.I | re.VERBOSE)
UTCNOW = datetime.utcnow()

def correct_request(match):
    """
    Fix some errors, for example, update header if it doesn't match the content.
    """
    indent = match.group("indent")
    header = match.group("header")
    template = match.group("section")

    question = re.search(r"\|\s*вопрос\s*=(.*)", template)
    timestamp = re.search(r"\|\s*автор\s*=[^/]+/\s*(\d{14})", template)
    if question is None or timestamp is None:
        # request is completely broken
        return match.group(0)

    correct_header = question.group(1).strip() + "/" + timestamp.group(1)
    if header == correct_header:
        # all is ok
        return match.group(0)
    
    return "{}== {} ==\n{}".format(indent, correct_header, template)

def delete_old_request(match):
    """Process one table row and delete it if it's neccessary."""
    template = match.group("section")
    status_match = re.search(r"\|\s*статус\s*=\s*([+-])", template)
    date_match = re.search(r"\|\s*администратор\s*=[^/]+/\s*(\d{14})", template)
    if status_match is None or date_match is None:
        # request is still open
        return match.group(0)

    delay = (1 if status_match.group(1) == "+" else 3) * 24 * 60 * 60
    date = datetime.strptime(date_match.group(1), "%Y%m%d%H%M%S")
    if (UTCNOW - date).total_seconds() < delay:
        return match.group(0)
    else:
        return ""

def replace(replacement, text):
    """
    Do REGEXP.sub(replacement, text) and return (new_text, status) tuple, where
    status is a boolean which is True if there was at least one replacement.
    """
    new_text = REGEXP.sub(replacement, text)
    return (new_text, new_text != text)

def main():
    """Update list."""
    site = pywikibot.Site()
    page = pywikibot.Page(site, "Википедия:Запросы к администраторам/Быстрые")
    text = page.text

    (text, is_corrected) = replace(correct_request, text)
    (text, is_deleted) = replace(delete_old_request, text)

    page.text = text

    if is_corrected and is_deleted:
        page.save("Исправление ошибок, удаление старых запросов.")
    elif is_corrected:
        page.save("Исправление ошибок.")
    elif is_deleted:
        page.save("Удаление старых запросов.")

if __name__ == "__main__":
    main()