from django.urls import path
from .views import ImageUploadView, PredictionList
from .live_feed_view import classify_frame
urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('predictions/', PredictionList.as_view(), name='predictions-list'),
    path('classify_image', classify_frame, name='Live Detection'),
]
