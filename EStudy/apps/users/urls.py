from django.conf.urls import url

from .views import UserInfoView, UploadImageView, ChangePwdView, ChangeMobileView, MyCourseView
from .views import MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView


urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="info"),
    url(r'^image/upload/$', UploadImageView.as_view(), name="image"),
    url(r'^update/pwd/$', ChangePwdView.as_view(), name="update_pwd"),
    url(r'^update/mobile/$', ChangeMobileView.as_view(), name="update_mobile"),
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    url(r'^myfavorg/$', MyFavOrgView.as_view(), name="myfavorg"),
    url(r'^myfavteacher/$', MyFavTeacherView.as_view(), name="myfavteacher"),
    url(r'^myfavcourse/$', MyFavCourseView.as_view(), name="myfavcourse"),
    url(r'^messages/$', MyMessageView.as_view(), name="messages"),
]
