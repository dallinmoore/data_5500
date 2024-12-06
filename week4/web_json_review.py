import requests
import json
'''
url = "https://api.datamuse.com/words?ml=duck"

req = requests.get(url)

dct = json.loads(req.text)

score_key = 'score'
word_key = 'word'

for d in dct:
    if d[word_key] == 'mallard':
        print(d[word_key],'score:',d[score_key])
'''

url = "https://api.datamuse.com/words?ml=skiing"

req = requests.get(url)

dct = json.loads(req.text)

score_key = 'score'
word_key = 'word'

score = 0
for d in dct:
    if  'snowboard' in d[word_key]:
        print(d[word_key],'score:',d[score_key])
        score += d[score_key]
print("Total score:",score)