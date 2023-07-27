# Много раз пыталась отсортировать этот файл, isort .
# Fixing D:\Dev\kittygram_final\backend\kittygram_backend\urls.py
# После того как явручную все поправила,isort cноваправит на предыдущий вариант
# Как это исправить?)
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cats.views import AchievementViewSet, CatViewSet

router = routers.DefaultRouter()
router.register('cats', CatViewSet)
router.register('achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
