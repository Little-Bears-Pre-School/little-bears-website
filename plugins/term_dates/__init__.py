import calendar
from datetime import timedelta

import httpx
from icalendar import Calendar
from pelican import signals


def get_event_color(event):
    """Return the color of the event."""
    str_hash = hash(event.get('summary', ''))
    hue = int(((str_hash & 0xff0000) >> 16) / 255 * 360)
    sat = int(((str_hash & 0x00ff00) >> 8) / 255 * 100)
    return {'hue': hue, 'sat': sat}


def fix_end_date(event):
    """Fix the end date of the event."""
    event["dtend"].dt -= timedelta(days=1)
    return event


def fetch_events(generator):
    """Retrieve events from the ICS calendar file."""

    # Fetch the calendar file
    url = generator.settings.get('CALENDAR_URL')
    response = httpx.get(url)
    cal = Calendar.from_ical(response.text)

    # Add the events to the generator
    events = [fix_end_date(event) for event in cal.walk('vevent')]

    generator.context['events'] = events
    generator.context['calendar'] = calendar
    generator.context["today"] = calendar.datetime.date.today()
    generator.context['get_event_color'] = get_event_color


def register():
    signals.page_generator_finalized.connect(fetch_events)
