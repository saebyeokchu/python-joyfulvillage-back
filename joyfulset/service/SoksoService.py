from django.db import transaction
import json
from joyfulset.models import sokso, soksoDetail
from joyfulset.serializers import soksoSerializer
from django.utils import timezone

class SoksoService : 
    # get
    def getById(id) :
        try : 
            result = sokso.objects.get(id=id)
            serializer = soksoSerializer(result)
            return serializer.data
        except :
            return RuntimeError
        
    def getByLevel(level) :
        try : 
            result = sokso.objects.filter(level = level).order_by('createdAt')
            serializer = soksoSerializer(result, many=True)
            # print(serializer.data)/
            return serializer.data
        except :
            return RuntimeError
    
    def getByLevelAndGroup(level,group) :
        try : 
            print(level+" | "+group)
            result = sokso.objects.filter(level = level, group = group).order_by('createdAt')
            serializer = soksoSerializer(result, many=True)
            print(serializer.data)
            return serializer.data
        except Exception as e:  # Catch specific exceptions
            print(f"Error occurred: {e}")
            return {"error": str(e)}  # Return error as a JSON-serializable dictionary
    
    #     level = models.IntegerField(default=1)
    # group = models.IntegerField(null=True, blank=True)
    # name = models.CharField(max_length=50)
    # introduction = models.TextField(null=True, blank=True)
    # mainImg = models.TextField()
    # soksoDetail_Id = models.ForeignKey(
    #     soksoDetail,  on_delete=models.CASCADE, 
    #     db_column="soksoDetail_Id", null=True, default=None
    # )
    # reserveLink = models.TextField(null=True, blank=True)
    # lastModifiedAt = models.DateTimeField(default=timezone.now)
    # createdAt = models.DateTimeField(default=timezone.now)

    # upsert
    def upsert(data):
        try:
            sokso_id = data["id"]   

            if sokso_id == None:
                new_sokso = sokso(
                    level = int(data["level"]),
                    group = int(data["group"]) if data["group"] else None,
                    name = str(data["name"]),
                    introduction = str(data["introduction"]),
                    mainImg = str(data["mainImg"]),
                    soksoDetail_Id = None,
                    reserveLink = str(data["reserveLink"]),
                )
                new_sokso.save()
                print("[Create Sokso]", new_sokso)

                return { "result" : True }
            else:
                print("[Update Sokso]")

                # make target
                targetSokso = {
                    "lastModifiedAt" : timezone.now
                }

                level = int(data["level"])
                group = data["group"]
                name = str(data["name"])
                introduction = data["introduction"]
                mainImg = str(data["mainImg"])
                reserveLink = str(data["reserveLink"])
                soksoDetail_Id = data["soksoDetail_Id"]


                if level > -1 :
                    targetSokso["level"] = level
                
                if group != None :
                    targetSokso["group"] = int(group)
                
                if name != '' :
                    targetSokso["name"] = name
                
                if  introduction != None :
                    targetSokso["introduction"] = str(introduction)
                
                if mainImg != '' :
                    targetSokso["mainImg"] = mainImg
                
                if reserveLink != '' :
                    targetSokso["reserveLink"] = reserveLink
                
                if  soksoDetail_Id != None :
                    targetSokso["soksoDetail_Id"] = int(soksoDetail_Id)
                

                print("update target", sokso_id, targetSokso)

                # Try to update existing entry
                obj, created = sokso.objects.update_or_create(
                    id=sokso_id,
                    defaults=targetSokso,
                )

                return { "result" : True }

        except Exception as e:
            return {"error": str(e), "result" : False}
    
    # upsert
    def upsertSoksoDetail(data):
        try:
            sokso_detail_id = data["id"]   

            # insert new sokso detail
            if sokso_detail_id == None: 
                print("[upsert new sokso detail]")
                return { "result" : True }
            else :
                print("[Update Sokso Detail]")

                # make target
                target_sokso_detail = {
                    "lastModifiedAt" : timezone.now
                }

                topImages = data["topImages"]
                contentImages = data["contentImages"]
                content = data["content"]

                if topImages != None :
                    target_sokso_detail["topImages"] = str(topImages)
                
                if  contentImages != None :
                    target_sokso_detail["contentImages"] = str(contentImages)
                
                if  content != None :
                    target_sokso_detail["content"] = str(content)
                

                print("update target detail sokso", target_sokso_detail)

                # Try to update existing entry
                obj, created = soksoDetail.objects.update_or_create(
                    id=sokso_detail_id,
                    defaults=targetSokso,
                )

                return { "result" : True }
        except Exception as e:
            return {"error": str(e), "result" : False}
    
    def deleteById(sokso_id) :
        try:
            sokso_entry = sokso.objects.get(id=sokso_id)
            print(sokso_entry)
            sokso_entry.delete()
            return {"message": f"sokso entry with ID {sokso_id} deleted successfully!", "result" : True}
        except sokso.DoesNotExist:
            return {"error": f"sokso entry with ID {sokso_id} does not exist.", "result" : False}

        except Exception as e:
            return {"error": str(e)}