from django.urls import path

from testapp.views import (
    SecuredListsAPIView,
    # OpenListsAPIView,
)

urlpatterns = [
    path('api/securelist/', SecuredListsAPIView.as_view()),
    # path('api/openview/', OpenListsAPIView.as_view()),
    # path('api/checklist/<int:pk>/', CheckListAPIView.as_view()),
]
