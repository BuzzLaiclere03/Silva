from gcsa.google_calendar import GoogleCalendar

calendar = GoogleCalendar('sarahmauderivard@gmail.com')

for event in calendar:
    print(event)