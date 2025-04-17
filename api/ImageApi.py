import os
from django.conf import settings

# IMAGE_UPLOAD_PATH = r"C:/Projects/joyful/code/joyful/public/images/"
# IMAGE_UPLOAD_PATH = os.getenv("IMAGE_UPLOAD_PATH", "/code/public/images")

def upload_image(image, imageName):
    """
    Upload an image to the MEDIA_ROOT directory and return its accessible URL.
    
    Parameters:
        image (InMemoryUploadedFile): The uploaded image file.
        imageName (str): The base name to save the image as (without extension).
    
    Returns:
        dict: Contains 'result', 'new_image_name', and 'image_url' if successful.
    """
    try:
        # Ensure the media directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        print(f"Media directory created at: {settings.MEDIA_ROOT}")
        # Extract the file extension from the uploaded image
        file_extension = os.path.splitext(image.name)[1]  # e.g., '.jpg', '.png'
        
        # Generate the new image file name
        new_image_name = imageName + file_extension

        print("new_image_name",new_image_name)
        
        # Create the full file system path where the image will be saved
        file_path = os.path.join(settings.MEDIA_ROOT, new_image_name)
        print("file_path",file_path)
        
        # Save the file in chunks (good for large files)
        with open(file_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        
        
        # Generate the publicly accessible URL using MEDIA_URL
        # If your backend domain is, for example, http://backend:8000, you might prepend that
        image_url = settings.MEDIA_URL + new_image_name
        print("image_url",image_url)
        
        return {
            "result": True,
            "new_image_name": new_image_name,
            "image_url": image_url
        }
    
    except Exception as e:
        print(f"Error uploading image: {e}")
        return {
            "result": False,
            "error": str(e)
        }

# def upload_image(image, imageName) :
#     global IMAGE_UPLOAD_PATH
#     print("upload_image")
#     try :
#         # Ensure the directory exists
#         os.makedirs(IMAGE_UPLOAD_PATH, exist_ok=True)
#         file_extension = os.path.splitext(image.name)[1]  # Extracts '.jpg', '.png', etc.
#         # create image name with current time
#         # new_image_name =  timezone.now().strftime("%Y_%m_%d_%H_%S_%f") + file_extension
#         new_image_name =  imageName + file_extension
#         # new_image_name = image.name
#         print("new_image_name",new_image_name)

#         # Define the full file path
#         file_path = os.path.join(IMAGE_UPLOAD_PATH, new_image_name) 
#         print("file_path",file_path)

#         # Save the file
#         with open(file_path, 'wb') as f:
#             for chunk in image.chunks():
#                 f.write(chunk)

#         return { "result" : True, "new_image_name" : new_image_name }
#     except Exception as e:
#         print(f"Error uploading image: {e}")
#         return {"result": False, "error": str(e)}

def replace_image(existing_image_path, new_image):
    try:
        # ✅ Check if the old image exists, then delete it
        # file_path = os.path.join(IMAGE_UPLOAD_PATH, existing_image_path)
        file_path = os.path.join(settings.MEDIA_ROOT, existing_image_path)

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

    try:
        # Ensure the directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        # Define the full file path
        file_path = os.path.join(settings.MEDIA_ROOT, image_name)
        
        if os.path.exists(file_path):  # ✅ Check if file exists
            os.remove(file_path)  # ✅ Delete the file
            return {"message": f"Image '{file_path}' deleted successfully", "result" : True}
        else:
            return {"error": "File does not exist", "result" : False}
    except Exception as e:
        return {"error": str(e)}