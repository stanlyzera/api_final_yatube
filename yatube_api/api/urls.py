from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = "api"

v1_router = routers.DefaultRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="group")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
v1_router.register("follow", FollowViewSet, basename="follows")

v1_urls = [
    path("", include("djoser.urls.jwt")),
    path("", include(v1_router.urls)),
]

urlpatterns = [
    path("v1/", include(v1_urls)),
]
