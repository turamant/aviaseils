from django.forms import ModelForm
from .models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "slug",
            "address",
            "email",

        ]