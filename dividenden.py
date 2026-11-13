import urllib.request
import json
from datetime import datetime

try:
    with open('aktien.txt', 'r') as f:
        isins = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    isins = []

ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Dividenden Kalender//DE
CALSCALE:GREGORIAN
METHOD:PUBLISH
"""

ics_content += "END:VCALENDAR"

with open('dividenden.ics', 'wb') as f:
    f.write(ics_content.encode('utf-8'))

print("Kalender erfolgreich generiert!")
