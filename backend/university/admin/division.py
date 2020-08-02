from django.contrib import admin
from django.urls import resolve
from university.models.division import Division
from .staff import StaffInline
from .forms import DivisionAdminForm
from university.models.utils import *


class DivisionInline(admin.TabularInline):
    model = Division
    extra = 0

    def get_parent_object_from_request(self, request):
        resolved = resolve(request.path_info)
        if resolved.kwargs:
            return self.parent_model.objects.get(pk=resolved.kwargs['object_id'])
        return None

    def formfield_for_choice_field(self, db_field, request=None, **kwargs):
        obj = self.get_parent_object_from_request(request)
        if obj:
            if obj.type == RECTORATE_TYPE:
                kwargs['choices'] = (DIVISION_TYPE_CHOICES[FACULTY_TYPE],)
            elif obj.type == FACULTY_TYPE:
                kwargs['choices'] = (DIVISION_TYPE_CHOICES[CHAIN_TYPE],)
            elif obj.type == CHAIN_TYPE:
                kwargs['choices'] = (DIVISION_TYPE_CHOICES[NONE_TYPE],)

        return db_field.formfield(**kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        obj = self.get_parent_object_from_request(request)
        if obj:
            if obj.type == CHAIN_TYPE:
                self.max_num = 0

        return super(DivisionInline, self).get_formset(request, obj, **kwargs)


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    form = DivisionAdminForm
    list_display = ('title', 'type', 'lead', 'head_depart',)
    list_filter = ('type',)
    fields = ('type', 'title', 'lead', 'head_depart',)
    inlines = [
        StaffInline,
        DivisionInline,
    ]
