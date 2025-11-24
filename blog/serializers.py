from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "slug": {"required": True, "allow_blank": False},
        }

    # Field-level validation: name
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Category name must be at least 3 characters.")
        return value

    # Field-level validation: slug
    def validate_slug(self, value):
        if " " in value:
            raise serializers.ValidationError("Slug cannot contain spaces.")
        if value != value.lower():
            raise serializers.ValidationError("Slug must be lowercase.")
        return value


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "title": {"required": True},
            "content": {"required": True, 'allow_blank': False},
        }

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Title must be at least 5 characters long.")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Content must be at least 10 characters long.")
        return value

    def validate(self, attrs):
        if attrs.get("category") is None:
            raise serializers.ValidationError("Category is required.")
        return attrs
