import django_filters
from rest_framework import viewsets
from django_filters import rest_framework as filters
from accident.models import Call
from accident.serializers import CallSerializer


class CallFilter(django_filters.rest_framework.FilterSet):
    report_date = django_filters.rest_framework.DateFromToRangeFilter(
        field_name='report_date',
    )


class CallViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Call.objects.all()
    serializer_class = CallSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CallFilter


