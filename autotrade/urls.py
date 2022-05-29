from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from autotrade.views import Home, SearchResultView

urlpatterns = [
                  path('admin_admin/', admin.site.urls),
                  path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

                  path('', Home.as_view(), name='home'),
                  path('search/', SearchResultView.as_view(), name='search bar'),

                  path('', include('autotrade.userapp.urls')),

                  path('', include('autotrade.products.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# import autotrade.signals
