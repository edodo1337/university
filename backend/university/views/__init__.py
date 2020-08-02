from rest_framework import routers
from .division import DivisionViewSet
from .staff import StaffViewSet

router = routers.DefaultRouter()
router.register(r'division', DivisionViewSet, basename='division')
router.register(r'staff', StaffViewSet, basename='staff')
