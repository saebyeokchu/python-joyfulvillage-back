from joyfulset.models import about, home
from joyfulset.serializers import aboutSerializer

class AboutService : 
    def getAll() :
        try : 
            serializer = aboutSerializer(about.objects.order_by('id'), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    # get
    def get_about_by_id(about_id):
        try:
            # Try to retrieve the room instance by its id
            about_instance = about.objects.get(id=about_id)
            print("about found:", about_instance)
            
            # Serialize the instance
            serializer = aboutSerializer(about_instance)
            print("Serialized data:", serializer.data)
            return serializer.data
        
        except about.DoesNotExist:
            # This handles the case where no room is found with the given id
            error_msg = f"No stay found with id {about_id}"
            print(error_msg)
            return {"error": error_msg}
        
        except Exception as e:
            # Log and return any other error that might occur
            print("Error in get_about_by_id:", e)
            return {"error": str(e)}

        except :
            return RuntimeError

    def getBySection(section) :
        try : 
            serializer = aboutSerializer(about.objects.filter(section = section), many=True)
            return serializer.data
        except :
            return RuntimeError
        
    def upsert(data):
        try:
            print("Data received:", data)
            
            # Check if 'id' exists and is truthy
            if "id" in data and data["id"]:
                obj, created = about.objects.update_or_create(
                    id=data["id"],
                    defaults=data
                )
            else:
                # If no 'id' is provided, create a new record
                obj = about.objects.create(**data)
                created = True

            return {"result": True, "created": created, "id": obj.id}
        
        except Exception as e:
            print("Error during upsert:", e)
            return {"result": False, "error": str(e)}
    
    def deleteById(about_id) :
        try:
            about_entry = about.objects.get(id=about_id)
            about_entry.delete()
            return {"message": f"about entry with ID {about_id} deleted successfully!", "result" : True}
        except home.DoesNotExist:
            return {"error": f"about entry with ID {about_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}
    

   