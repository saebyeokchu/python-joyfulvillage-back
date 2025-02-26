from django.db import transaction
import json
from joyfulset.models import home, qna
from joyfulset.serializers import homeSerializer, qnaSerializer

class QnaService : 
    def get() :
        try : 
            sorted_qna = qna.objects.order_by('sortOrder')  # Ascending order
            serializer = qnaSerializer(sorted_qna, many=True)
            return serializer.data
        except :
            return RuntimeError
 
    def insertQna(question, answer) :
        try:
            # Get the highest sortOrder (or default to 1)
            last_sort_order = qna.objects.order_by('-sortOrder').first()
            next_sort_order = last_sort_order.sortOrder + 1 if last_sort_order else 1


            # Create and save new object
            result = qna.objects.create(
                question=question,
                answer=answer,
                sortOrder=next_sort_order
            )

            if result :
                return qnaSerializer(qna.objects,many=True).data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def upsertQna(data):
        try:
            qna_id = data["id"]
            question = data["question"]
            answer = data["answer"]

            print(qna_id, question, answer)

            if qna_id:
                # Try to update existing entry
                obj, created = qna.objects.update_or_create(
                    id=qna_id,
                    defaults={
                        "question": question,
                        "answer": answer
                    },
                )
            else:
                # Get the highest sortOrder (or default to 1)
                last_sort_order = qna.objects.order_by('-sortOrder').first()
                next_sort_order = last_sort_order.sortOrder + 1 if last_sort_order else 1


                # Create and save new object
                result = qna.objects.create(
                    question=question,
                    answer=answer,
                    sortOrder=next_sort_order
                )

        except Exception as e:
            return {"error": str(e)}
        
    def update_qna_sort_order(order):
        try:
            # Retrieve all affected records in one query
            before_values = [o["before"] for o in order]
            qna_objects = {obj.sortOrder: obj for obj in qna.objects.filter(sortOrder__in=before_values)}

            # Update sortOrder values
            for o in order:
                if o["before"] in qna_objects:
                    qna_objects[o["before"]].sortOrder = o["after"]

            # Use bulk update for efficient database writes
            with transaction.atomic():  # Ensures all updates succeed or none
                qna.objects.bulk_update(qna_objects.values(), ['sortOrder'])

            return True  # Success
        except Exception as e:
            print(f"Error: {e}")
            return False  # Failure

    def delete_qna_entry(qna_id):
        try:
            qna_entry = qna.objects.get(id=qna_id)
            print(qna_entry)
            qna_entry.delete()
            return {"message": f"QNA entry with ID {qna_id} deleted successfully!"}
        except qna.DoesNotExist:
            return {"error": f"QNA entry with ID {qna_id} does not exist."}

        except Exception as e:
            return {"error": str(e)}
   