from challengenews.views.articles import ArticleListView
from challengenews.views.authors import AuthorsViewSet
from django.urls.conf import include,path
from rest_framework import routers
from challengenews.views import *

admin_router = routers.DefaultRouter()
admin_router.register('articles', ArticleViewSet, basename='admin-articles')
admin_router.register('authors', AuthorsViewSet, basename='admin-authors')

router = routers.DefaultRouter()
router.register('articles', ArticleListView, basename='articles')

urlpatterns = [
    path('admin/', include(admin_router.urls), name='admin'),
    path('', include(router.urls))
]