from scrapy_djangoitem import DjangoItem
from BoardGameSiteApp.models import AlePlanszowkiGame


class AlePlanszowkiGameItem(DjangoItem):
    django_model = AlePlanszowkiGame

