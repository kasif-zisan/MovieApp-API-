from MovieList.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
