from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import mixins
from .mixins import SubordinatesMixin
from university.serializers import StaffDetailSerializer, StaffSubordinatesSerializer
from university.models import Staff


class StaffViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, SubordinatesMixin):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AllowAny,)
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StaffDetailSerializer
        elif self.action == 'subordinates':
            return StaffSubordinatesSerializer
        elif self.action == 'retrieve':
            return StaffDetailSerializer

    def get_serializer_context(self):
        context = super(StaffViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        order = self.request.query_params.get('ord')
        try:
            return Staff.objects.all().order_by(order)
        except:
            return Staff.objects.all()
