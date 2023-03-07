# Scrapy settings for GithubSpiderProMax project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'GithubSpiderProMax'

SPIDER_MODULES = ['GithubSpiderProMax.spiders']
NEWSPIDER_MODULE = 'GithubSpiderProMax.spiders'

def get_cookies_dict():
    cookies_str = '_octo=GH1.1.1449172623.1654507027; _device_id=0ef38b0fe6eed4c8d440332ab8093ebb; user_session=F9wf3aUjGPrEEaoP8EiGoVBDCUuKcSspprcAnNsaL7hjev-P; __Host-user_session_same_site=F9wf3aUjGPrEEaoP8EiGoVBDCUuKcSspprcAnNsaL7hjev-P; logged_in=yes; dotcom_user=Awlgcu; has_recent_activity=1; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; preferred_color_mode=light; tz=Asia/Shanghai; _gh_sess=cmp9akNSq8HNFj4rX4+BYsWXmKuzB+mbTLxXFoK/aGTSKBDRwEO7X+PL3MVU/CVXJ32fMTmwyJ+sixTR6L3dnYbZm1uE6MACo1U5hpxeSpPZFgXEKjhWztL+v6jhi33H9smdeCTOZYaOghklfL+9oV5GCrn7h5W51stLhw1Wz7SGLVRzrnBe3Mq8Z4XkOE5hQh4li+BXJ+ZJ4ZQF4vTvX1Y+5bu64LVC50SfsjMsLQxI05orIq327xfTVrVoLNZJKK+DGAs8sOL3M2SHVV1XndKrhAbKR4QOUyeFbVzYm5Q=--3eO5/45M4zl8VWkQ--q7i0awZkj5BCV5muEZ/4RA=='
    cookies_dict = {}
    for item in cookies_str.split(';'):
        key, value = item.split('=', maxsplit=1)
        cookies_dict[key] = value
    return cookies_dict

COOKIES_DICT = get_cookies_dict()

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32
# RETRY_ENABLED = True
# RETRY_TIMES = 8
# RETRY_HTTP_CODES = [429]
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'GithubSpiderProMax.middlewares.GithubspiderpromaxSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'GithubSpiderProMax.middlewares.GithubspiderpromaxDownloaderMiddleware': 543,
#    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'GithubSpiderProMax.pipelines.GithubspiderpromaxPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_EXPORT_ENCODING = 'utf-8'