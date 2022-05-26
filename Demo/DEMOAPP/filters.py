from .models import personalbanking3
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = personalbanking3
        fields = ['cid', 'AN', 'CN','Amt','email' ]