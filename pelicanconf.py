AUTHOR = "Andy Driver"
SITENAME = "Little Bears Pre-School"
SITEURL = ""

EXTRA_PATH_METADATA = {
    "misc/robots.txt": {"path": "robots.txt"},
    "misc/sitemap.xml": {"path": "sitemap.xml"},
}

PATH = "content"
ARTICLE_PATHS = ["blog"]
STATIC_PATHS = [
    "css",
    "downloads",
    "images",
    "misc/robots.txt",
    "misc/sitemap.xml",
]

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/littlebears"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

CALENDAR_URL = "https://calendar.google.com/calendar/ical/c_063b785ddacd833d62af3ba0ff9eb174df0cfb49ada8bb99ad650febbf78a516%40group.calendar.google.com/public/basic.ics"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["term_dates"]