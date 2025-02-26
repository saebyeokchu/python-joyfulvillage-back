from django.db import transaction
import json
from joyfulset.models import biz, busniess
from joyfulset.serializers import bizSerializer, busniessSerializer

class BizService : 
    def get() :
        try : 
            result = busniess.objects
            serializer = busniessSerializer(result, many=True)
            # print(serializer.data)/
            return serializer.data
        except :
            return RuntimeError
    
    def getAll() :
        try : 
            serializer = bizSerializer(biz.objects, many=True)
            # print(serializer.data)/
            return serializer.data
        except :
            return RuntimeError
        
    def getKakao() :
        try : 
            result = busniess.objects.values("latitude", "longtitude", "addressText")
            # serializer = busniessSerializer(result, many=True)
            # print(serializer.data)/
            return result
        except :
            return RuntimeError
 
    def updateBiz(long, lan, addressText) :
            try : 
                result = busniess.objects.update_or_create(
                    id=1,
                    defaults={
                        "longtitude": long,
                        "latitude": lan,
                        "addressText" : addressText
                    })
                return result
            except :
                return RuntimeError
    
    def getBySection(section) :
        try : 
            print("getBySection")
            serializer = bizSerializer(biz.objects.filter(section=section), many=True)
            return serializer.data
        except :
            return RuntimeError
   