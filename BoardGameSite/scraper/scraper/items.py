from scrapy_djangoitem import DjangoItem
from BoardGameSiteApp.models import APGame


class AlePlanszowkiGameItem(DjangoItem):
    django_model = APGame
