About
-----

This Django FileSystemStorage will save files under a path with 3 sub-directories.

Sub-directories are 2 hexadecimal characters long, which makes 256*256*256 = 16777216 directories.

The main reason is to limit the number of files per directory for easy listing and increased performance with some old file systems.

The directories are created according to a hash of the file name and it's content. Same files will be stored under the same directory tree and will be renamed if another file already existed.

Usage
-----

ex: uploads/c4/7e/cd/my_file.ext

models.py::

    fs = MultiFolderStorage(location=settings.PROJECT_PATH,
                            base_url='/')

    class FileModel(models.Model):
        upload = models.FileField(upload_to='uploads',storage=fs)
