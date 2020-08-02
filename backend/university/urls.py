from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from .views import router

schema_view = get_swagger_view(title='University')

urlpatterns = [
    path('', include(router.urls)),
]
