from django.utils import timezone
from joyfulset.models import cafe
from joyfulset.serializers import cafeSerializer

class CafeService : 
    def getAll() :
        try : 
            print("getAll")
            serializer = cafeSerializer(cafe.objects.order_by('id'), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    def getBySection(section) :
        try : 
            print("getBySection")
            serializer = cafeSerializer(cafe.objects.filter(section=section), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    def create(data) :
        try:
            result = cafe.objects.create(
                section = data.get("section"),
                content = data.get("content"),
                img = data.get("img"),
                note = data.get("note"),
            )
            return { "result" : True}
        except Exception as e:
            return {"error": str(e), "result" : False}

    # upsert
    def updateCafe(data):
        print("[Update Cafe]")

        try:
            targetCafe = {}

            # make target
            targetCafe = {
                "lastModifiedAt" : timezone.now
            }


            id = data.get("id")
            section = data.get("section")
            content = data.get("content")
            img = data.get("img")
            note = data.get("note")

            if content :
                targetCafe["content"] = str(content)

            if img != None :
                targetCafe["img"] = str(img)
            
            if  note != None :
                targetCafe["note"] = str(note)
            
            print("id",id) 
            

            # Try to update existing entry
            if id != None :
                print("targetCafe",targetCafe) 
                obj, created = cafe.objects.update_or_create(
                    id=int(id),
                    defaults=targetCafe,
                )
            elif section != None :
                print("section",section)
                print("targetCafe",targetCafe)

                obj, created = cafe.objects.update_or_create(
                    section=str(section),
                    defaults=targetCafe,
                )


            return { "result" : True }

        except Exception as e:
            return {"error": str(e), "result" : False}
        
        
    def deleteById(cafe_id) :
        try:
            cafe_entry = cafe.objects.get(id=cafe_id)
            print(cafe_entry)
            cafe_entry.delete()
            return {"message": f"cafe entry with ID {cafe_id} deleted successfully!", "result" : True}
        except cafe.DoesNotExist:
            return {"error": f"cafe entry with ID {cafe_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}