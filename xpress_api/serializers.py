from django.db.models import fields
from rest_framework import serializers
from xpress.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','author','excerpt','content','status')

    