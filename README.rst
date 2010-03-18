About
-----

This Django FileSystemStorage will save files under a path with 3 sub-directories.

Sub-directories are 2 hexadecimal characters long, which makes 256*256*256 = 16777216 directories max.

The main reason is to limit the number of files per directory for easy listing and increased performance with some file systems.

The directories are created according to a hash of the file's content. Same files will be stored under the same directory tree and will be renamed if another file already existed.

Usage
-----

ex: uploads/c4/7e/cd/my_file.ext

models.py::

    from mfstorage import MultiFolderStorage
    
    fs = MultiFolderStorage(location=settings.PROJECT_PATH,
                            base_url='/')

    class FileModel(models.Model):
        upload = models.FileField(upload_to='uploads',storage=fs)


Installation
------------

::

    git clone git@github.com:samueladam/django-mfstorage.git
    cd django-mfstorage
    python setup.py install
