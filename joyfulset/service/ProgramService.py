from django.utils import timezone
from joyfulset.models import program
from joyfulset.serializers import programSerializer

class ProgramService : 
    def getAll() :
        try : 
            print("getAll")
            data = program.objects.order_by('id')
            print(data)
            for d in data :
                print(d.introduction)
            serializer = programSerializer(data, many=True)
            return serializer.data
        except :
            return RuntimeError
        
    # get
    def get_program_by_id(program_id):
        try:
            # Try to retrieve the room instance by its id
            program_instance = program.objects.get(id=program_id)
            print("program found:", program_instance)
            
            # Serialize the instance
            serializer = programSerializer(program_instance)
            print("Serialized data:", serializer.data)
            return serializer.data
    
            
        except program.DoesNotExist:
            # This handles the case where no room is found with the given id
            error_msg = f"No stay found with id {program_id}"
            print(error_msg)
            return {"error": error_msg}
        
        except Exception as e:
            # Log and return any other error that might occur
            print("Error in get_program_by_id:", e)
            return {"error": str(e)}

        except :
            return RuntimeError
    
    def create(data) :
        try:
            result = program.objects.create(
                name = data.get("name"),
                subName = data.get("subName"),
                introduction = data.get("introduction"),
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
            introduction = data.get("introduction")

            content = data.get("content")
            img = data.get("img")

            if name :
                targetProgram["name"] = str(name)
            
            if subName :
                targetProgram["subName"] = str(subName)
            
            if introduction :
                targetProgram["introduction"] = str(introduction)
            
            if content :
                targetProgram["content"] = str(content)
            
            if img :
                targetProgram["img"] = str(img)
            
            print("introduction", targetProgram["introduction"])

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