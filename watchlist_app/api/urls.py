from django.urls import path,include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('stream', views.StreamPlatfromVS, basename="streamplatform")

urlpatterns = [
    # path('list/',views.movie_list ,name = 'movie-list'),
    # path('<int:pk>',views.movie_details ,name = 'movie-details'),
    
    path('', include(router.urls)),
    # path('list/',views.MovieListAV.as_view()  ,name = 'movie-list'),
    # path('<int:pk>',views.MovieDetailAV.as_view() ,name = 'movie-details'),
    path('list/',views.WatchListAV.as_view()  ,name = 'movie-list'),
    path('<int:pk>',views.WatchDetailAV.as_view() ,name = 'movie-details'),
    # path('stream/',views.StreamPlatformAV.as_view(), name ='stream'),
    # path('stream/<int:pk>',views.StreamPlatformDetailAV.as_view(), name = 'Stream-details'),
    
    path('stream/<int:pk>/review-create',views.ReviewCreate.as_view(), name = 'Review-Create'),
    path('stream/<int:pk>/review',views.ReviewList.as_view(), name = 'Review-List'),
    path('stream/review/<int:pk>',views.ReviewDetail.as_view(), name = 'Review-Detail'),
    # path('review', views.ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(),name='review-Detail')
    
]