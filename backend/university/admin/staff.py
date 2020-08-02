from django.contrib import admin
from university.models.staff import Staff
from university.models.division import Division
from django.urls import resolve
from university.models.utils import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'position', 'division',)


class StaffInline(admin.TabularInline):
    fields = ('first_name', 'last_name', 'patronymic', 'position', 'birthday',)
    model = Staff
    extra = 0
    show_change_link = True

    def get_parent_object_from_request(self, request):
        resolved = resolve(request.path_info)
        if resolved.kwargs:
            return self.parent_model.objects.get(pk=resolved.kwargs['object_id'])
        return None

    def formfield_for_choice_field(self, db_field, request=None, **kwargs):
        obj = self.get_parent_object_from_request(request)
        if obj:
            if obj.type == RECTORATE_TYPE:
                kwargs['choices'] = RECTORATE_POSITION_CHOICES
            elif obj.type == FACULTY_TYPE:
                kwargs['choices'] = FACULTY_POSITION_CHOICES
            elif obj.type == CHAIN_TYPE:
                kwargs['choices'] = FACULTY_POSITION_CHOICES

        return db_field.formfield(**kwargs)
