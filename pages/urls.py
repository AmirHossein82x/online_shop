from django.urls import path

from .views import HomeTemplateView, AboutUsView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutUsView.as_view(), name='about us')

]