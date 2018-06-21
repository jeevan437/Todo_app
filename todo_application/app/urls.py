from django.conf.urls import url
from.views import todo_view


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^todo_details/',todo_view)   # function based views
    #url(r'book_details',BookView.as_view()) # class based views
]