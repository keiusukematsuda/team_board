from django_filters import FilterSet
from django_filters import filters

from .models import Event


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class EventFilter(FilterSet):

    name = filters.CharFilter(label='イベント名', lookup_expr='contains')
    memo = filters.CharFilter(label='詳細', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('type', 'type'),
        ),
        field_labels={
            'name': 'イベント名',
            'type': '種類',
        },
        label='並び順'
    )

    class Meta:
        model = Event
        fields = ('name', 'date', 'memo',)
