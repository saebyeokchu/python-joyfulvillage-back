import os
from django.utils import timezone

image_path = r"C:/Projects/joyful/code/joyful/public/images/"

def upload_image(image, imageName) :
    global image_path
    print("upload_image")
    try :
        # Ensure the directory exists
        os.makedirs(image_path, exist_ok=True)
        file_extension = os.path.splitext(image.name)[1]  # Extracts '.jpg', '.png', etc.
        # create image name with current time
        # new_image_name =  timezone.now().strftime("%Y_%m_%d_%H_%S_%f") + file_extension
        new_image_name =  imageName + file_extension
        # new_image_name = image.name
        print("new_image_name",new_image_name)

        # Define the full file path
        file_path = os.path.join(image_path, new_image_name) 
        print("file_path",file_path)

        # Save the file
        with open(file_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        return { "result" : True, "new_image_name" : new_image_name }
    except Exception as e:
        print(f"Error uploading image: {e}")
        return {"result": False, "error": str(e)}

def replace_image(existing_image_path, new_image):
    try:
        # ✅ Check if the old image exists, then delete it
        file_path = os.path.join(image_path, existing_image_path)
        print("replace_image")
        print(file_path)
        if os.path.exists(existing_image_path):
            os.remove(existing_image_path)  # ❌ Delete the previous image
            print(f"Deleted previous image: {existing_image_path}")
        else:
            print("Warning: Previous image not found, continuing with upload.")

        # ✅ Extract directory and filename
        image_dir, image_name_with_ext = os.path.split(file_path)
        file_extension = os.path.splitext(new_image.name)[1]  # Extracts '.jpg', '.png', etc.

        # ✅ Ensure directory exists
        os.makedirs(image_dir, exist_ok=True)

        # ✅ Define new image path (same name, new content)
        new_image_path = os.path.join(image_dir, image_name_with_ext)

        # ✅ Save the new file
        with open(new_image_path, 'wb') as f:
            for chunk in new_image.chunks():
                f.write(chunk)

        return {"result": True, "new_image_path": new_image_path}

    except Exception as e:
        print(f"Error replacing image: {e}")
        return {"result": False, "error": str(e)}

def delete_image(image_name):
    global image_path

    try:
        # Ensure the directory exists
        os.makedirs(image_path, exist_ok=True)

        # Define the full file path
        file_path = os.path.join(image_path, image_name)

        print("image_path",image_path)
        print("file_path",file_path)
        
        if os.path.exists(file_path):  # ✅ Check if file exists
            os.remove(file_path)  # ✅ Delete the file
            return {"message": f"Image '{file_path}' deleted successfully", "result" : True}
        else:
            return {"error": "File does not exist", "result" : False}
    except Exception as e:
        return {"error": str(e)}