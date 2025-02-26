from django.utils import timezone
from joyfulset.models import program
from joyfulset.serializers import programSerializer

class ProgramService : 
    def getAll() :
        try : 
            print("getAll")
            serializer = programSerializer(program.objects.order_by('id'), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    def create(data) :
        try:
            result = program.objects.create(
                name = data.get("name"),
                subName = data.get("subName"),
                content = data.get("content"),
                img = data.get("img")
            )
            return {"result" : True}
        except Exception as e:
            return {"error": str(e), "result" : False}

    # upsert
    def updateProgram(data):
        print("[Update Cafe]")

        try:
            targetProgram = {}

            # make target
            targetProgram = {
                "lastModifiedAt" : timezone.now
            }

            id = int(data.get("id"))
            name = data.get("name")
            subName = data.get("subName")
            content = data.get("content")
            img = data.get("img")

            if name :
                targetProgram["name"] = str(name)
            
            if subName :
                targetProgram["subName"] = str(subName)
            
            if content :
                targetProgram["content"] = str(content)
            
            if img :
                targetProgram["img"] = str(img)


            # Try to update existing entry
            obj, created = program.objects.update_or_create(
                    id=id,
                    defaults=targetProgram,
                )
            
            return {"result" : True }
        except Exception as e:
            return {"error": str(e), "result" : False}
    
    def deleteById(program_id) :
        try:
            program_entry = program.objects.get(id=program_id)
            print(program_entry)
            program_entry.delete()
            return {"message": f"program entry with ID {program_id} deleted successfully!", "result" : True}
        except program.DoesNotExist:
            return {"error": f"program entry with ID {program_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}