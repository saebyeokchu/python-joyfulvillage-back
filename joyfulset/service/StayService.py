from django.db import transaction
import json
from joyfulset.models import  stay
from joyfulset.serializers import  staySerializer
from django.utils import timezone

class StayService :
    # get
    def get_stay_by_id(stay_id):
        try:
            # Try to retrieve the room instance by its id
            stay_instance = stay.objects.get(id=stay_id)
            print("stay found:", stay_instance)
            
            # Serialize the instance
            serializer = staySerializer(stay_instance)
            print("Serialized data:", serializer.data)
            return serializer.data
        
        except stay.DoesNotExist:
            # This handles the case where no room is found with the given id
            error_msg = f"No stay found with id {stay_id}"
            print(error_msg)
            return {"error": error_msg}
        
        except Exception as e:
            # Log and return any other error that might occur
            print("Error in get_stay_by_id:", e)
            return {"error": str(e)}
    # get
    def getAll() :
        try : 
            serializer = staySerializer(stay.objects.order_by('id'), many=True)
            return serializer.data
        except :
            return RuntimeError
        
    # # upsert
    # def upsert(data):
    #     print(data)
    #     try:
    #         print(data["name"])
    #         print(data["address"])
    #         print(data["introduction"])
    #         print(data["mainImgs"])
    #         print(bool(int(data["optionAvailable"])))

    #         if data["id"]:
    #             # make target
    #             data["lastModifiedAt"] = timezone.now
    #             print("update")
    #             print(data)
    #             # Try to update existing entry
    #             obj, created = stay.objects.update_or_create(
    #                 id=data["id"],
    #                 defaults=data,
    #             )
    #             return { "result" : True }
    #         else:
    #         # Try to update existing entry
    #             result = stay.objects.create(
    #                 name = str(data["name"]),
    #                 address = str(data["address"]),
    #                 introduction = str(data["introduction"]),
    #                 mainImgs = str(data["mainImgs"]),
    #                 optionAvailable = bool(int(data["optionAvailable"])),
    #             )
    #             print("create")
    #             print(result)
    #             return { "result" : result }

    #     except Exception as e:
    #         return {"error": str(e), "result" : False}
    
    def upsert(data):
        try:
            print("Stay Data received:", data)
            
            # Check if 'id' exists and is truthy
            if "id" in data and data["id"]:
                obj, created = stay.objects.update_or_create(
                    id=data["id"],
                    defaults=data
                )
            else:
                # If no 'id' is provided, create a new record
                obj = stay.objects.create(**data)
                created = True

            return {"result": True, "created": created, "id": obj.id}
        except Exception as e:
            print("Error during upsert:", e)
            return {"result": False, "error": str(e)}
    
    def deleteById(stay_id) :
        try:
            stay_entry = stay.objects.get(id=stay_id)
            print(stay_entry)
            stay_entry.delete()
            return {"message": f"stay entry with ID {stay_id} deleted successfully!", "result" : True}
        except stay.DoesNotExist:
            return {"error": f"stay entry with ID {stay_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}