from django.contrib import admin
from django.urls import include, path


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
