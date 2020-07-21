from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('front/', TemplateView.as_view(template_name='index.html')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('tinymce/', include('tinymce.urls')),
    path('', include('articles.urls')),
    path('about/', views.about),
    path('admin/', admin.site.urls)
]

# urlpatterns += i18n_patterns(path('', include('articles.urls')), prefix_default_language=False)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
