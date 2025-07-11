from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # include if you have other apps
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('nebo-admin/', admin.site.urls),
    path('', include('insurance_website.urls')), 
]

# Serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# # This allows media files to be served even when DEBUG = False (for dev/testing)
# if not settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]


# from django.conf.urls import handler404, handler500

handler404 = 'insurance_website.views.custom_404_view'
# handler404 = 'insurance_website.views.custom_page_not_found'
# handler500 = 'insurance_website.views.custom_server_error'
