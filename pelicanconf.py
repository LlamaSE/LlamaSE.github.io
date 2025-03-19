AUTHOR = 'LlamaSE'
SITENAME = 'Dire Llama Games'
SITEURL = ""

PATH = "content"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

THEME = "../pelican-themes/blue-penguin-dark"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)


TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
