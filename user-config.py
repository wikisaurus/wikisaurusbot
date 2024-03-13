# https://www.mediawiki.org/wiki/Manual:Pywikibot/OAuth/Wikimedia
# Load the auth info from the environment

import os

family = "wikipedia"
mylang = "ru"

usernames['wikipedia']['*'] = \
  usernames['meta']['*'] = \
  usernames['commons']['*'] = \
  usernames['wikidata']['*'] = \
  usernames['wiktionary']['*'] = \
  usernames['wikibooks']['*'] = \
  usernames['wikinews']['*'] = \
  usernames['wikiquote']['*'] = \
  usernames['wikisource']['*'] = \
  usernames['wikiversity']['*'] = \
  usernames['wikivoyage']['*'] = \
  usernames['wikifunctions']['*'] = \
  usernames['wikitech']['*'] = \
    os.environ.get('PWB_USERNAME')

authenticate['*.wikipedia.org'] = \
  authenticate['*.wikimedia.org'] = \
  authenticate['*.wikidata.org'] = \
  authenticate['*.wiktionary.org'] = \
  authenticate['*.wikibooks.org'] = \
  authenticate['*.wikinews.org'] = \
  authenticate['*.wikiquote.org'] = \
  authenticate['*.wikisource.org'] = \
  authenticate['*.wikiversity.org'] = \
  authenticate['*.wikivoyage.org'] = \
  authenticate['*.mediawiki.org'] = \
  authenticate['*.wikifunctions.org'] = \
    (
      os.environ.get('PWB_CONSUMER_TOKEN'),
      os.environ.get('PWB_CONSUMER_SECRET'),
      os.environ.get('PWB_ACCESS_TOKEN'),
      os.environ.get('PWB_ACCESS_SECRET')
    )

