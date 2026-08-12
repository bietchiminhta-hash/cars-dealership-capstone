
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('fetchDealer/<int:dealer_id>', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('dealers/<str:state>', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('analyze/<str:text>', views.analyze_review_sentiment, name='analyze_review'),
    path('review', views.add_review, name='add_review'),
    path('dealers/<str:state>', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('analyze/<str:text>', views.analyze_review_sentiment, name='analyze_review'),
    path('review', views.add_review, name='add_review'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
]
