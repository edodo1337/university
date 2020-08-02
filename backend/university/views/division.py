from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import mixins
from .mixins import DivisionStaffMixin
from university.serializers import DivisionListSerializer, DivisionDetailSerializer, DivisionStaffSerializer
from university.models.division import Division


class DivisionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, DivisionStaffMixin):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return DivisionListSerializer
        elif self.action == 'retrieve':
            return DivisionDetailSerializer
        elif self.action == 'staff':
            return DivisionStaffSerializer

    def get_serializer_context(self):
        context = super(DivisionViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        order = self.request.query_params.get('ord')
        try:
            return Division.objects.all().order_by(order)
        except:
            return Division.objects.all()
