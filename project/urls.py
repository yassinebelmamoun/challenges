from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

v1 = ([
          path('', include('core.urls')),
      ], 'v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
    path('documentation/', include_docs_urls(title='Test assignment API'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
