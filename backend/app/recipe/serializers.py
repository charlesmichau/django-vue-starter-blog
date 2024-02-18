"""
Serializers for the recipe APIs.
"""

from rest_framework import serializers
from core.models import Recipe, Tag


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the Recipe object."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for the Recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the Tag object."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
