import uuid
import os

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(f'uploads/{instance.__class__.__name__}/images', filename)