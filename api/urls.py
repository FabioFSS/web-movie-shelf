from django.urls import path
from .views import ListView, RatingView, ProgressView, JSONCacheView, IndexView, UserView, DetailMovieView, DetailTvView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user/<int:pk>', UserView.as_view(), name="users"),
    path('list/', ListView.as_view(), name="lists"),
    path('rating/', RatingView.as_view(), name="ratings"),
    path('progress/', ProgressView.as_view(), name="progresses"),
    path('jsoncache/', JSONCacheView.as_view(), name="jsoncache"),
    path('detailsmovie/<int:id>', DetailMovieView.as_view(), name="detailsmovie"),
    path('detailstv/<int:id>', DetailTvView.as_view(), name="detailstv"),
]