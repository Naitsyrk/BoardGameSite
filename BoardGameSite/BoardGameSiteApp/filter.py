import django_filters

from .models import Game, Category, Mechanic, PublishingHouse


class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Nazwa:", lookup_expr='icontains')
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), label="Kategorie:", lookup_expr='exact')
    mechanics = django_filters.ModelMultipleChoiceFilter(queryset=Mechanic.objects.all(), label="Mechaniki:", lookup_expr='exact')
    minimum_players = django_filters.NumberFilter(label="Minimalna liczba graczy", lookup_expr='gte')
    maximum_players = django_filters.NumberFilter(label="Maksymalna libcza graczy", lookup_expr='lte')
    publishing_house = django_filters.ModelChoiceFilter(queryset=PublishingHouse.objects.all(), label="Wydawnictwo", lookup_expr='exact')
    minimum_age = django_filters.NumberFilter(label="Minimalny wiek:", lookup_expr='gte')

    class Meta:
        model = Game
        fields = [
            'name',
            'categories',
            'mechanics',
            'minimum_players',
            'maximum_players',
            'publishing_house',
            'minimum_age',
        ]


# class RandomGameFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(label="Nazwa:", lookup_expr='icontains')
#     categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), label="Kategorie:", lookup_expr='exact')
#     mechanics = django_filters.ModelMultipleChoiceFilter(queryset=Mechanic.objects.all(), label="Mechaniki:", lookup_expr='exact')
#     minimum_players = django_filters.NumberFilter(label="Minimalna liczba graczy", lookup_expr='gte')
#     maximum_players = django_filters.NumberFilter(label="Maksymalna libcza graczy", lookup_expr='lte')
#     publishing_house = django_filters.ModelChoiceFilter(queryset=PublishingHouse.objects.all(), label="Wydawnictwo", lookup_expr='exact')
#     minimum_age = django_filters.NumberFilter(label="Minimalny wiek:", lookup_expr='gte')
#     games_number = django_filters.NumberFilter(label="Ilośc gier do wylosowania", lookup_expr='exact')
#
#     class Meta:
#         model = Game
#         fields = [
#             'name',
#             'categories',
#             'mechanics',
#             'minimum_players',
#             'maximum_players',
#             'publishing_house',
#             'minimum_age',
#             'choices_games',
#         ]
