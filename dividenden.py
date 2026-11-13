from datetime import datetime

ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Dividenden Kalender//DE
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:test-dividende-20261114@yashin84
DTSTAMP:20261113T200000Z
DTSTART;VALUE=DATE:20261114
DTEND;VALUE=DATE:20261115
SUMMARY:Test-Dividende: Allianz SE (13,80 EUR)
DESCRIPTION:Automatisierter Test-Eintrag aus GitHub Actions
END:VEVENT
END:VCALENDAR
"""

with open('dividenden.ics', 'wb') as f:
    f.write(ics_content.strip().encode('utf-8'))

print("Kalender erfolgreich generiert!")
