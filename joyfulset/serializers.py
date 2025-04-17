from os import link
from rest_framework import serializers

from .models import about, headerInfo,  option, program, busniess, cafe, home, imageArchive, qna, room, stay

class homeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = home
        fields = ['id', 'imgSrc', 'lastModifiedAt', 'createdAt']

class cafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = cafe
        fields = ['id',  'section',  'img', 'content', 'note', 'lastModifiedAt', 'createdAt']

class programSerializer(serializers.ModelSerializer):
    class Meta:
        model = program
        fields = ['id',  'name',  'subName', 'img', 'introduction', 'content', 'lastModifiedAt', 'createdAt']

class qnaSerializer(serializers.ModelSerializer) :
    id = serializers.IntegerField()
    question = serializers.CharField()
    answer = serializers.CharField()
    sortOrder = serializers.IntegerField()
    lastModifiedAt = serializers.DateTimeField()

    class Meta:
        model = qna
        fields = ['id', 'question', 'answer', 'sortOrder', 'lastModifiedAt']

class busniessSerializer(serializers.ModelSerializer) :
    class Meta:
        model = busniess
        fields = [
            'id', 
            'longtitude', 
            'latitude', 
            'addressText', 
            'runingHours', 
            'busniessNumber', 
            'instagramUrl', 
            'youtubeUrl', 
            'adminName',
            'adminEmail',
            'lastModifiedAt']

# class bizSerializer(serializers.ModelSerializer) :
#     class Meta:
#         model = biz
#         fields = [
#             'id', 
#             'section', 
#             'name', 
#             'value', 
#             'note', 
#             'lastModifiedAt',
#             'createdAt']
                
# class soksoDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = soksoDetail
#         fields = ['id', 'topImages', 'contentImages', 'content', 'lastModifiedAt', 'createdAt']

# class soksoSerializer(serializers.ModelSerializer):
#     soksoDetail_Id = soksoDetailSerializer()  # ✅ Nested serializer to include full details

#     class Meta:
#         model = sokso
#         fields = ['id', 'level', 'group', 'name', 'introduction', 'mainImg', 'soksoDetail_Id', 'reserveLink', 'lastModifiedAt', 'createdAt']

class imageArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = imageArchive
        fields = ['id',  'imgSrc',  'lastModifiedAt', 'createdAt']

##
class staySerializer(serializers.ModelSerializer):
    class Meta:
        model = stay
        fields = ['id', 'name', 'address', 'introduction1', 'introduction2',  'mainImgs', 'optionAvailable',  'lastModifiedAt', 'createdAt']

class optionSerializer(serializers.ModelSerializer):
    class Meta:
        model = option
        fields = ['id', 'name', 'introduction', 'mainImgs', 'content',  'stay_id', 'lastModifiedAt', 'createdAt']

class roomSerializer(serializers.ModelSerializer):
    stay_id = staySerializer()  # ✅ Nested serializer to include full details

    class Meta:
        model = room
        fields = ['id', 'name', 'structure', 'introduction1', 'introduction2', 'mainImgs', 'content', 'stay_id', 'layout', 'reserveLink', 'reserveNumber', 'lastModifiedAt', 'createdAt']

##
# class linkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = link
#         fields = ['id', 'name', 'url', 'lastModifiedAt', 'createdAt']

class aboutSerializer(serializers.ModelSerializer) :
    class Meta:
        model = about
        fields = [
            'id',
            'section', 
            'imgSrc', 
            'title', 
            'address', 
            'content', 
            'InstagramId', 
            'InstagramLink', 
            'lastModifiedAt', 
            'createdAt'
        ]


class headerInfoSerializer(serializers.ModelSerializer) :
    class Meta:
        model = headerInfo
        fields = [
            'id',
            'name',
            'introduction1', 
            'introduction2', 
            'imgSrc', 
            'lastModifiedAt', 
            'createdAt'
        ]
