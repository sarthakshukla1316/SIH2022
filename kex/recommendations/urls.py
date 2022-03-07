from django.contrib import admin
from django.urls.conf import path, include
from kex.recommendations.views import NewUserRecommendation, HistoryRecommendation

app_name = "equipment"

urlpatterns = [
    path("recommend", NewUserRecommendation.as_view(), name="recommends"),
    path(
        "history-recommend", HistoryRecommendation.as_view(), name="history-recommends"
    ),
]
