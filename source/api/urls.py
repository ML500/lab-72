from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet, QuotePlusView, QuoteMinusView

router = DefaultRouter()
router.register('quote', QuoteViewSet, basename='quote')


app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('quote/plus/<int:pk>/', QuotePlusView.as_view(), name='quote_plus'),
    path('quote/minus/<int:pk>/', QuoteMinusView.as_view(), name='quote_minus'),

]
