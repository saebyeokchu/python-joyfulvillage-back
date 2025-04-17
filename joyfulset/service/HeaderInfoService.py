from joyfulset.models import headerInfo
from joyfulset.serializers import headerInfoSerializer

class HeaderInfoService : 
    def getAll() :
        try : 
            serializer = headerInfoSerializer(headerInfo.objects.order_by('id'), many=True)
            return serializer.data
        except :
            return RuntimeError
    
    # get
    def get_info_by_id(info_id):
        try:
            # Try to retrieve the room instance by its id
            info_instance = headerInfo.objects.get(name=info_id)
            print("info found:", info_instance)
            
            # Serialize the instance
            serializer = headerInfoSerializer(info_instance)
            print("Serialized data:", serializer.data)
            return serializer.data
        
        except headerInfo.DoesNotExist:
            # This handles the case where no room is found with the given id
            error_msg = f"No stay found with id {info_id}"
            print(error_msg)
            return {"error": error_msg}
        
        except Exception as e:
            # Log and return any other error that might occur
            print("Error in get_info_by_id:", e)
            return {"error": str(e)}

        except :
            return RuntimeError

    def upsert(data):
        try:
            print("Data received:", data)
            
            # Check if 'id' exists and is truthy
            if "id" in data and data["id"]:
                obj, created = headerInfo.objects.update_or_create(
                    id=data["id"],
                    defaults=data
                )
            else:
                # If no 'id' is provided, create a new record
                obj = headerInfo.objects.create(**data)
                created = True

            return {"result": True, "created": created, "id": obj.id}
        
        except Exception as e:
            print("Error during upsert:", e)
            return {"result": False, "error": str(e)}

    

   