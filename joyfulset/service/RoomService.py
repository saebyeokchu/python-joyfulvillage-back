from django.db import transaction
import json
from joyfulset.models import room, stay
from joyfulset.serializers import roomSerializer
from django.utils import timezone

class RoomService : 
    # get
    def get_room_by_id(room_id):
        try:
            # Try to retrieve the room instance by its id
            room_instance = room.objects.get(id=room_id)
            print("Room found:", room_instance)
            
            # Serialize the instance
            serializer = roomSerializer(room_instance)
            print("Serialized data:", serializer.data)
            return serializer.data
        
        except room.DoesNotExist:
            # This handles the case where no room is found with the given id
            error_msg = f"No room found with id {room_id}"
            print(error_msg)
            return {"error": error_msg}
        
        except Exception as e:
            # Log and return any other error that might occur
            print("Error in get_room_by_id:", e)
            return {"error": str(e)}
        
    def getAll() :
        try : 
            result = room.objects
            serializer = roomSerializer(result)
            return serializer.data
        except :
            return RuntimeError
        
    def getByStayId(stay_id) :
        try : 
            serializer = roomSerializer( room.objects.filter(stay_id = stay_id).order_by("id"), many=True)
            return serializer.data
        except :
            return RuntimeError
   
    # upsert
    def upsert(data):
        try:
            print("Data received:", data)
            data["stay_id"] = stay.objects.get(id=data["stay_id"])

            # Check if 'id' exists and is truthy
            if "id" in data and data["id"]:
                obj, created = room.objects.update_or_create(
                    id=data["id"],
                    defaults=data
                )
            else:
                # If no 'id' is provided, create a new record
                obj = room.objects.create(**data)
                created = True

            return {"result": True, "created": created, "id": obj.id}
        except Exception as e:
            print("Error during upsert:", e)
            return {"result": False, "error": str(e)}
        
    def deleteById(room_id) :
        try:
            room_entry = room.objects.get(id=room_id)
            print(room_entry)
            room_entry.delete()
            return {"message": f"room entry with ID {room_id} deleted successfully!", "result" : True}
        except room.DoesNotExist:
            return {"error": f"room entry with ID {room_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}