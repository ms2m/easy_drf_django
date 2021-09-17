from django.urls import path

from core.views import CheckListsAPIView, TestAPIView

urlpatterns = [
    path('', TestAPIView.as_view()),
    path('api/checklists/', CheckListsAPIView.as_view()),

]
