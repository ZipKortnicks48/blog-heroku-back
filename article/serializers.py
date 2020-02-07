from rest_framework import serializers
from article.models import Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields=('id','name','description','body','file','date','subactegory')
