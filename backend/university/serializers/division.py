from rest_framework import serializers
from university.models.division import Division
from university.models.staff import Staff
from university.serializers.staff import StaffShortSerializer, StaffDetailSerializer


class DivisionStaffSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display')

    staff_list = serializers.SerializerMethodField()

    def get_staff_list(self, instance):
        try:
            order = self.context['request'].query_params['ord']
            objs = Staff.objects.filter(division=instance).order_by(order)
            return StaffDetailSerializer(objs, many=True).data
        except:
            objs = Staff.objects.filter(division=instance)
            return StaffDetailSerializer(objs, many=True).data

    class Meta:
        fields = ('id', 'type_display', 'title', 'staff_list',)
        model = Division


class DivisionShortSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display')

    class Meta:
        fields = ('id', 'type_display', 'title',)
        model = Division


class DivisionListSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display')

    lead_staff = StaffShortSerializer(source='lead')

    head_division = DivisionShortSerializer(source='head_depart')

    class Meta:
        fields = ('id', 'type_display', 'title', 'lead_staff', 'head_division',)
        model = Division


class DivisionDetailSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display')
    lead_staff = StaffShortSerializer(source='lead')

    class Meta:
        fields = ('id', 'type_display', 'title', 'lead_staff',)
        model = Division

    def to_representation(self, instance):
        data = super().to_representation(instance)

        def dfs(obj):
            item = self.__class__(obj).data
            order = self.context.get('request')

            try:
                order = self.context['request'].query_params['ord']
                childs = Division.objects.filter(head_depart=obj).order_by(order)
            except:
                childs = Division.objects.filter(head_depart=obj)

            for i in childs:
                item['childs'] = []
                sub_item = dfs(i)
                if sub_item:
                    item['childs'].append(sub_item)
            return item

        try:
            order = self.context['request'].query_params['ord']
            childs = Division.objects.filter(head_depart=instance).order_by(order)
        except:
            childs = Division.objects.filter(head_depart=instance)

        if childs:
            data['childs'] = []
            for child in childs:
                item = dfs(child)
                if bool(item):
                    data['childs'].append(item)
        return data
