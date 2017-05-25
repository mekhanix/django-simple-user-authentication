from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^login/',views.login_view,name='login'),
    url(r'^logout/',views.logout_view,name='logout'),
    url(r'create/',views.PostCreateView.as_view(), name='create'),
    url(r'posts/',views.PostListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[-\d]+)/$',views.PostDetailView.as_view(), name='detail'),
]
