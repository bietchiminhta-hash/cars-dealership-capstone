from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('login', TemplateView.as_view(template_name='Login.html')),
    path('dealer', TemplateView.as_view(template_name='dealer.html')),
    path('postreview', TemplateView.as_view(template_name='postReview.html')),
    path('djangoapp/', include('djangoapp.urls')),
    path('admin/', admin.site.urls),
]
