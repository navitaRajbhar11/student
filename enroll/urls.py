from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from enroll.views import add,show,update,delete

urlpatterns = [
    path("", add, name='add_data'),
    path("show/", show, name="show"),
    path("update/<int:id>/", update, name='update_data'),  
    path("del/<int:id>/", delete, name='delete'), #dynamic url
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

