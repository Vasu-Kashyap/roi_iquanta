from django_filters import FilterSet
from django_filters.filters import RangeFilter
from .models import college
from .forms import PeopleFilterFormHelper
from .widgets import CustomRangeWidget

class AllRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [p.fees for p in college.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class CollegeFilter(FilterSet):
  fees = AllRangeFilter()

  class Meta:
      model = college
      fields = ['fees']
      form = PeopleFilterFormHelper