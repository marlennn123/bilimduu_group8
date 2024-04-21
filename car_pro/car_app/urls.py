from django.urls import path, include
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):

        swagger = super().get_schema(request, public)
        swagger.tags = [

            {
                "name": "car",
                "description": "Get car by car id"
            },
            {
                "name": "cars",
                "description": "Get all cars"
            },
        ]

        return swagger


schema_view = get_schema_view(
    openapi.Info(
        title="Swagger documentation",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
    generator_class=CustomOpenAPISchemaGenerator,
)

urlpatterns = [

    path('cars/', CarViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='car_list'),
    path('car/<int:pk>/', CarViewSet.as_view({'get': 'retrieve', ' put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('bet/', BetViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='bet_list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='bet_detail'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
