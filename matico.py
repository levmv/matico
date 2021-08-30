import json
import os
import re
import sys
import urllib.request

GOOGLE_FONTS_LINK = 'http://fonts.googleapis.com/css?family=Material+Icons+Outlined'
OUTPUT_FONT_NAME = 'icon'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'


def encode_codepoint(code):
    return ''.join('%' + "%0.2X" % x for x in (chr(int(code, 16)).encode('utf8')))


with open(os.path.dirname(__file__) + '/codepoints.json') as file:
    codepoints = json.load(file)

names = []
for line in sys.stdin:
    names.extend([name.strip() for name in line.split(',')])
names = set([name for name in names if name in codepoints])

if len(names) == 1:
    print("Input is empty", file=sys.stderr)
    sys.exit(1)

text_part = ''
data = {}
for name in names:
    print(".%s-%s:before {\n content: '\\%s';  \n}" % (OUTPUT_FONT_NAME, name, codepoints[name]))
    text_part += encode_codepoint(codepoints[name])

req = urllib.request.Request(
    GOOGLE_FONTS_LINK + '&text=' + text_part,
    data=None,
    headers={
        'User-Agent': USER_AGENT
    }
)

content = urllib.request.urlopen(req).read().decode('utf8')
p = re.compile(r"url\((.*)\)\s", re.RegexFlag.MULTILINE)

woff2 = p.search(content).group(1)

with urllib.request.urlopen(woff2) as f:
    with open(OUTPUT_FONT_NAME + '.woff2', 'wb') as output:
        output.write(f.read())
