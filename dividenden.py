from datetime import datetime, timedelta
import yfinance as yf

# Deine echten Aktien-Ticker
tickers = [
    "TLX.DE",   # Talanx
    "SIE.DE",   # Siemens
    "TD",       # Toronto Dominion
    "GOOG",     # Alphabet C
    "BMY",      # Bristol Myers Squibb
    "PFE",      # Pfizer
    "LIN",      # Linde
    "ALV.DE",   # Allianz
    "KKR",      # KKR
    "2318.HK",  # Ping An Insurance
    "HHH",      # Howard Hughes
    "INTC"      # Intel
]

vevents = []
# Das heutige Datum als Startpunkt, damit nur die Zukunft angezeigt wird
heute = datetime.utcnow().date()

for ticker_symbol in tickers:
    try:
        stock = yf.Ticker(ticker_symbol)
        dividends = stock.dividends
        
        # Durchsuche alle bekannten Dividenden, filtere aber auf das Datum ab heute
        for date, amount in dividends.items():
            div_date = date.date() if hasattr(date, 'date') else date
            if div_date >= heute:
                dt_start = date.strftime('%Y%m%d')
                dt_end = (date + timedelta(days=1)).strftime('%Y%m%d')
                uid = f"div-{ticker_symbol}-{dt_start}@yashin84"
                
                event = f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}
DTSTART;VALUE=DATE:{dt_start}
DTEND;VALUE=DATE:{dt_end}
SUMMARY:Dividende: {ticker_symbol} ({amount:.2f})
DESCRIPTION:Zukünftiger Termin via yfinance
END:VEVENT"""
                vevents.append(event)
    except Exception as e:
        print(f"Fehler bei {ticker_symbol}: {e}")

# ICS-Grundgerüst zusammenbauen
ics_header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Dividenden Kalender//DE
CALSCALE:GREGORIAN
METHOD:PUBLISH"""

ics_footer = "END:VCALENDAR"

ics_content = "\n".join([ics_header] + vevents + [ics_footer])

with open('dividenden.ics', 'wb') as f:
    f.write(ics_content.strip().encode('utf-8'))

print(f"Kalender mit {len(vevents)} zukünftigen Terminen generiert!")
