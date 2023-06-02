from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta

# Set the OAuth 2.0 scopes required for calendar access
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Authenticate and authorize the user using OAuth 2.0
flow = InstalledAppFlow.from_client_secrets_file('~/.credentials/credentials.json', SCOPES)
credentials = flow.run_local_server(port=0)
service = build('calendar', 'v3', credentials=credentials)

# Get the current date and time
now = datetime.utcnow().isoformat() + 'Z'

# Calculate the end of the day
end_of_day = (datetime.utcnow() + timedelta(days=1)).replace(hour=0, minute=0, second=0).isoformat() + 'Z'

# Retrieve events from now until the end of the day
events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end_of_day,
                                      maxResults=3, singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])

# Print the details of the upcoming events
for event in events:
    start_time = event['start'].get('dateTime', event['start'].get('date'))
    end_time = event['end'].get('dateTime', event['end'].get('date'))
    summary = event['summary']
    print(f"Event: {summary}")
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print("")
