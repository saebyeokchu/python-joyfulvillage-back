from joyfulset.models import home
from joyfulset.serializers import homeSerializer

class HomeService : 
    def get() :
        try : 
            serializer = homeSerializer(home.objects.order_by('createdAt'), many=True)
            return serializer.data
        except :
            return RuntimeError

    def add(src) :
        try : 
            result = home.objects.create(
                imgSrc = src,
            )
            return {"result" : True}
        except :
            return RuntimeError
        
    def delete(id) :
        try:
            home_entry = home.objects.get(id=id)
            home_entry.delete()
            return {"message": f"home entry with ID {d} deleted successfully!", "result" : True}
        except home.DoesNotExist:
            return {"error": f"home entry with ID {program_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}
    

   