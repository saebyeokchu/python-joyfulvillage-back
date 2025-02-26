from joyfulset.models import home
from joyfulset.serializers import homeSerializer

class AboutService : 
    def get() :
        try : 
            serializer = homeSerializer(home.objects, many=True)
            return serializer.data
        except :
            return RuntimeError

    def getBySection(section) :
        try : 
            serializer = homeSerializer(home.objects.filter(section = section), many=True)
            return serializer.data
        except :
            return RuntimeError
        
    def getMainImg() :
        try : 
            serializer = homeSerializer(home.objects.filter(section = 1), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    def updateContents(section, contents) :
        try :        
            targetHome = home.objects.get(section = section)
            targetHome.contents = contents
            targetHome.save()
            return True
        except :
            return RuntimeError

   