from rest_framework import serializers
from university.models.staff import Staff
from university.models.division import Division
from university.models.utils import *


class StaffShortSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'patronymic',)
        model = Staff


class StaffDetailSerializer(serializers.ModelSerializer):
    position_display = serializers.CharField(source='get_position_display')
    division_display = serializers.CharField(source='division.title')

    class Meta:
        fields = (
            'id', 'first_name', 'last_name', 'patronymic', 'birthday', 'photo', 'position_display', 'division_display',)
        model = Staff


class StaffSubordinatesSerializer(serializers.ModelSerializer):
    position_display = serializers.CharField(source='get_position_display')
    division_display = serializers.CharField(source='division.title')

    class Meta:
        fields = (
            'id', 'first_name', 'last_name', 'patronymic', 'birthday', 'photo', 'position_display', 'division_display',)
        model = Staff

    def to_representation(self, instance):
        data = super().to_representation(instance)

        staff_list = []

        def dfs(staff_list, div):

            try:
                order = self.context['request'].query_params['ord']
                childs = Division.objects.filter(head_depart=div).order_by(order)
            except:
                childs = Division.objects.filter(head_depart=div)

            staff_list.extend(list(div.staff.all()))
            for child in childs:
                dfs(staff_list, child)

        if instance.position == RECTORATE_LEAD_POSITION:
            staff_list = [x for x in instance.division.staff.all() if x != instance]

        try:
            order = self.context['request'].query_params['ord']
            childs = Division.objects.filter(head_depart=instance.division).order_by(order)
        except:
            childs = Division.objects.filter(head_depart=instance.division)

        for child in childs:
            dfs(staff_list, child)
        data['subordinates'] = StaffDetailSerializer(staff_list, many=True).data

        return data
