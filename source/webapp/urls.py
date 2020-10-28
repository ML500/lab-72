from django.urls import path

from webapp.views import IndexView, QuoteCreateView

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', QuoteCreateView.as_view(), name='create'),
]
