from rest_framework import filters

from django_filters.rest_framework import FilterSet
from django_filters.filters import OrderingFilter

# from v1.{{ app_name }}.models.model_name import Model


# class ModelFilter(FilterSet):
#     o = OrderingFilter(
#         fields=(
#         )
#     )

#     class Meta:
#         model = Model
#         fields = []


# class ModelFilterBackend(filters.BaseFilterBackend):

#     def filter_queryset(self, request, queryset, view):
#         return queryset
