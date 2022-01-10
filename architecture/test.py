import json
from urllib.request import urlopen
from urllib.parse import urlencode

params = dict(q="Sausages", format="json")
handel = urlopen("http://api.duckduckgo.com" + "?" + urlencode(params))
raw_text = handel.read().decode('utf-8')
parsed = json.loads(raw_text)

results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + ' - ' + r['Text'])
