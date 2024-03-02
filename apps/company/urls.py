from django.urls import path
from .api.views import (
    RegionCreateView,
    FilialCreateView,
    VacancyCreateView
)

urlpatterns = [
    path('region_create', RegionCreateView.as_view()),
    path('filial_create', FilialCreateView.as_view()),
    path('vacancy_create', VacancyCreateView.as_view()),

]
