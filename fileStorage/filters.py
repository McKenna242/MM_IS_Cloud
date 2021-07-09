import django_filters
from django_filters import *
from django.forms.widgets import *

from .models import *

class fileFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="uploadDate", lookup_expr='gte')
    #end_date = DateFilter(field_name="uploadDate", lookup_expr='lte')
    note = CharFilter(field_name="fileNote", lookup_expr='icontains')
    startDate = DateFilter(field_name="uploadDate", lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}))
    endDate = DateFilter(field_name="uploadDate", lookup_expr='lte', widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = fileStorageSchema
        fields = ['fileType', 'public', 'note']
        exclude = ['id']