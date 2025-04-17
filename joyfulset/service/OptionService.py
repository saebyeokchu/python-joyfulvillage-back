from django.db import transaction
from joyfulset.models import option, stay
from joyfulset.serializers import optionSerializer
from django.utils import timezone

class OptionService : 
    # get
    def getById(id) :
        try : 
            serializer = optionSerializer(option.objects.get(id=id))
            return serializer.data
        except :
            return RuntimeError
        
    def getAll() :
        try : 
            serializer = optionSerializer(option.objects.order_by('id'), many=True)
            return serializer.data
        except :
            return RuntimeError

    def getByStayId(stay_id) :
        try : 
            serializer = optionSerializer( option.objects.filter(stay_id = stay_id), many=True)
            return serializer.data
        except :
            return RuntimeError
        
    def upsert(data):
        try:
            print("Data received:", data)

            if "stay_id" in data:
            # Move the integer value from 'stay_id' to 'stay_id_id'
                data["stay_id"] = stay.objects.get(id=data["stay_id"])
            
            # Check if 'id' exists and is truthy
            if "id" in data and data["id"]:
                data["lastModifiedAt"] = timezone.now
                obj, created = option.objects.update_or_create(
                    id=data["id"],
                    defaults=data
                )
            else:
                # If no 'id' is provided, create a new record
                obj = option.objects.create(**data)
                created = True

            return {"result": True, "created": created, "id": obj.id}
        except Exception as e:
            print("Error during upsert:", e)
            return {"result": False, "error": str(e)}
    
    def deleteById(option_id) :
        try:
            option_entry = option.objects.get(id=option_id)
            option_entry.delete()
            return {"message": f"option entry with ID {option_id} deleted successfully!", "result" : True}
        except option.DoesNotExist:
            return {"error": f"option entry with ID {option_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}