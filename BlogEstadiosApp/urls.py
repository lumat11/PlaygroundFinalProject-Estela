
from django.contrib import admin
from django.urls import path
from BlogEstadiosApp.views import login_view, signup_view, estadios, crear_estadio, update_user_profile, estadio_detail, about_me, logout_view
from .views import EstadioDeleteView, EstadioUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('about_me/', about_me, name='about_me'),
    path('update_profile/', update_user_profile, name='update_profile'),
    path('pages/<int:estadio_id>/', estadio_detail, name='estadio_detail'),
    path('signup/', signup_view, name='signup'),
    path('pages/', estadios, name='estadios'),
    path('create/', crear_estadio, name='crear_estadio'),
    path('pages/<int:pk>/delete/',
         EstadioDeleteView.as_view(), name='delete_estadio'),
    path('pages/<int:pk>/edit/', EstadioUpdateView.as_view(), name='edit_estadio'),
]
