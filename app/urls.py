from django.urls import path
from .views import HomePageView, AboutPageView, PortfolioPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
]