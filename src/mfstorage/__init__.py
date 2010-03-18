import os.path
from hashlib import md5

from django.core.files.storage import FileSystemStorage


class MultiFolderStorage(FileSystemStorage):
    """
    Stores files under multiple folders
    according to a hash of the file.

    ex: uploads/c4/7e/cd/my_file.ext

    usage:
    # models.py

    fs = MultiFolderStorage(location=settings.PROJECT_PATH,
                            base_url='/')

    class FileModel(models.Model):
        upload = models.FileField(upload_to='uploads',storage=fs)

    """
    def save(self, name, content):
        # create md5 hash from content
        data = content.size and content.chunks(chunk_size=1024).next()\
                            or 'empty_file'
        hash = md5(data).hexdigest()

        # generate the new sub path
        dir_name, file_name = os.path.split(name)
        name = os.path.join(dir_name,
                            hash[0:2],
                            hash[2:4],
                            hash[4:6],
                            file_name)

        return super(MultiFolderStorage, self).save(name, content)

