import django_filters
from django_filters import DateFilter, CharFilter


from .models import *

class fileFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="uploadDate", lookup_expr='gte')
    end_date = DateFilter(field_name="uploadDate", lookup_expr='lte')
    note = CharFilter(field_name="fileNote", lookup_expr='icontains')
    class Meta:
        model = fileStorageSchema
        fields = ['fileType', 'size', 'public', 'uploadDate', 'note']
        exclude = ['id']