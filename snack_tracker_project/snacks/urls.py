from django.urls import path
from .views import SnackListView, SnackDetailView

# , SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path("detail-view/<int:pk>", SnackDetailView.as_view(), name="snack_detail"),
    # path("", SnackListView.as_view(), name="snack_list"),
]
