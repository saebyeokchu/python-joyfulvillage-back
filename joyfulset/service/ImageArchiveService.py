from django.db import transaction
import json
from joyfulset.models import home, imageArchive
from joyfulset.serializers import homeSerializer, imageArchiveSerializer

class ImageArchiveService : 
    def getAll() :
        try : 
            print("ImageArchiveService")
            serializer = imageArchiveSerializer(imageArchive.objects, many=True)
            return serializer.data
        except :
            return RuntimeError

    def create(image_name) :
        try:
            result = imageArchive.objects.create(
                imgSrc = image_name
            )
            return { "result" : True}
        except Exception as e:
            return {"error": str(e), "result" : False}
    
    def deleteById(image_id) :
        try:
            image_entry = imageArchive.objects.get(id=image_id)
            print(image_entry)
            image_entry.delete()
            return {"message": f"image entry with ID {image_id} deleted successfully!", "result" : True}
        except imageArchive.DoesNotExist:
            return {"error": f"image entry with ID {image_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}
        
    def replaceImg(fr, to) :
        # from whole url
        # to whole url
        return { "result" : True}
        