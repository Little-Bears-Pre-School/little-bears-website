AUTHOR = "Andy Driver"
SITENAME = "Little Bears Pre-School"
SITEURL = ""

EXTRA_PATH_METADATA = {
    "misc/robots.txt": {"path": "robots.txt"},
}

PATH = "content"
ARTICLE_PATHS = ["blog"]
STATIC_PATHS = ["css", "downloads", "images", "misc/robots.txt"]

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