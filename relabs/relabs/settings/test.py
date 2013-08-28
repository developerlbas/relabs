from base import *

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "test_dev_relabs_db",
        "USER": "dev_relabs_user",
        "PASSWORD": "dev_relabs_pwd",
        "HOST": "10.20.54.12",
        "PORT": "",
    },
}
