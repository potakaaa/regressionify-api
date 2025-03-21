import os
from django.core.files.storage import default_storage
from django.conf import settings
from file_upload.models import File

def clearMedia():
    File.objects.all().delete()

    upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    os.makedirs(upload_path, exist_ok=True)

    files = default_storage.listdir('uploads/')
    for file in files[1]: 
        default_storage.delete(f'uploads/{file}')

        
    

# this could be optimized.. somehow..