from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseLessonView, CourseCommentView, CoursePlayView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="list"),
    url(r'^(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
    url(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name="lesson"),
    url(r'^(?P<course_id>\d+)/comment/$', CourseCommentView.as_view(), name="comment"),
    url(r'^(?P<course_id>\d+)/video/(?P<video_id>\d+)/$', CoursePlayView.as_view(), name="video"),
]
