from django.urls import path

from .views import MarkerViewPost

urlpatterns = [
    path('point', MarkerViewPost.as_view()),
    # path('marker/', MarkerViewGet.as_view())
]
