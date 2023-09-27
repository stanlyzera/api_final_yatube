from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("post",)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source="user.username")
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    def validate_following(self, value):
        user = self.context["request"].user
        if user == value:
            raise serializers.ValidationError(
                "Невозможно подписаться на самого себя."
            )
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        if "following" not in validated_data:
            raise serializers.ValidationError(
                {"following": "Это поле требуется."}
            )
        following = validated_data["following"]
        instance, created = Follow.objects.get_or_create(
            user=user, following=following
        )
        if not created:
            raise serializers.ValidationError(
                {"following": "Вы уже подписаны на этого пользователя."}
            )
        return instance

    class Meta:
        model = Follow
        fields = ("user", "following")
