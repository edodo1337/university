from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from university.serializers.division import DivisionStaffSerializer


class SubordinatesMixin:
    @action(detail=True, methods=['GET'])
    def subordinates(self, *args, **kwargs):
        obj = self.get_object()
        data = self.get_serializer(obj).data
        return Response(data=data)
