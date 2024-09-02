import calendar
from itertools import groupby

import httpx
from icalendar import Calendar
from pelican import signals


def fetch_events(generator):
    """Retrieve events from the ICS calendar file."""

    # Fetch the calendar file
    url = generator.settings.get('CALENDAR_URL')
    response = httpx.get(url)
    cal = Calendar.from_ical(response.text)

    # Add the events to the generator
    events = list(cal.walk('vevent'))
    generator.context['events'] = events
    generator.context['events_by_date'] = {dt: list(ev) for dt, ev in groupby(events, lambda e: e['dtstart'].dt)}
    generator.context['calendar'] = calendar
    generator.context["today"] = calendar.datetime.date.today()


def register():
    signals.page_generator_finalized.connect(fetch_events)
