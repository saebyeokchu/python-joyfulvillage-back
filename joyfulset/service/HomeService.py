from joyfulset.models import busniess, home
from joyfulset.serializers import homeSerializer

class HomeService : 
    def get() :
        try : 
            serializer = homeSerializer(home.objects.order_by('createdAt'), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    def getMiddleTitle() :
        try : 
            result = busniess.objects.filter(id=1).values('homeMiddleTitle').first()
            # result will be a dict, e.g., {'homeMiddleTitle': 'Your Title'}
            home_middle_title = result['homeMiddleTitle'] if result else None
            return home_middle_title
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
    
    def updateMiddleTitle(text) :
        try : 
            result = busniess.objects.update_or_create(
                id=1,
                defaults={
                    "homeMiddleTitle": text
                })
        
            print(result)
            return True if result else False
        except :
            return RuntimeError
        
    def deleteById(home_id) :
        try:
            home_entry = home.objects.get(id=home_id)
            print(home_entry)
            home_entry.delete()
            return {"message": f"home entry with ID {home_id} deleted successfully!", "result" : True}
        except home.DoesNotExist:
            return {"error": f"home entry with ID {home_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}
    

   