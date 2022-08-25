from rest_framework import serializers
from .models import BlogPost





class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'category','image','small_description','description','created','updated']
