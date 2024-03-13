#!/usr/bin/env python3
"""
Script updates article list in ruwiki's {{Случайные статьи с КУЛ}} template.

Usage:
    python afi.py
"""

import re
import random
import os
from pathlib import Path

# set the path to the user-config.py file before importing pywikibot
curdir = Path(__file__).parent.parent.absolute()
os.environ["PYWIKIBOT_DIR"] = str(curdir)

import pywikibot

CATEGORY_NAME = "Категория:Википедия:Статьи для срочного улучшения"
TEMPLATE_NAME = "Шаблон:Случайные статьи с КУЛ"

TEXT_BEFORE = "{{fmbox|text=Статьи для доработки: "
TEXT_AFTER = ".|textstyle=text-align: center;}}"

LIST_LEN = 5

COMMENT = "Обновление списка статей."

def main():
    """Main script function."""
    site = pywikibot.Site()
    site.login()

    category = pywikibot.Category(site, CATEGORY_NAME)
    pages = list(category.articles())
    pages = ["[[" + page.title() + "]]" for page in pages]

    random.shuffle(pages)

    text = ", ".join(pages[:LIST_LEN])
    text = TEXT_BEFORE + text + TEXT_AFTER

    template = pywikibot.Page(site, TEMPLATE_NAME)
    noinclude = re.search(r"<noinclude>(?:[^<]|<(?!noinclude)?)+</noinclude>$", template.text)
    if noinclude:
        template.text = text + noinclude.group(0)
    else:
        template.text = text
    template.save(COMMENT, minor=False)

if __name__ == "__main__":
    main()
