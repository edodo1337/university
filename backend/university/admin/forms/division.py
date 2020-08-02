from django import forms
from university.models.division import Division
from university.models.utils import *


class DivisionAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DivisionAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            if self.instance.type == RECTORATE_TYPE:
                self.fields['head_depart'].queryset = Division.objects.none()
            elif self.instance.type == FACULTY_TYPE:
                self.fields['head_depart'].queryset = Division.objects.filter(type=RECTORATE_TYPE)
            elif self.instance.type == CHAIN_TYPE:
                self.fields['head_depart'].queryset = Division.objects.filter(type=FACULTY_TYPE)

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Division
        fields = '__all__'
