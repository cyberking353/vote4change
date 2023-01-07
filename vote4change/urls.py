"""vote4change URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from pages.views import(
    voter_profile,
    election_page,
    dashboard_view,
    voter_deteil_view,
    voter_update_view,
    voter_delete_view,
    candidate_create_view,
    
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('election/',election_page,name='election_page'),
    path('voter/profile/',voter_profile,name='profile'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('voter/<int:pk>/deteils/',voter_deteil_view,name='deteils'),
    path('voter/<int:pk>/update/',voter_update_view,name='update'),
    path('voter/<int:pk>/delete/',voter_delete_view,name='delete'),
    path('candidate/create/',candidate_create_view,name='candidate_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
