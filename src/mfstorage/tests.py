# -*- coding: utf-8 -*-
import unittest
import os
import shutil
import tempfile
from django.core.files.base import ContentFile

from mfstorage import MultiFolderStorage

class MultiFolderStorageTest(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.mktemp()
        os.makedirs(self.temp_dir)
        self.storage = MultiFolderStorage(location=self.temp_dir)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_storage(self):
        for size in (0, 1, 10, 5000):
            # write file
            text = 'X' * size
            content = ContentFile(text)
            path = self.storage.save('data.txt', content)
            
            # open and test file
            f_data = self.storage.open(path).read()
            self.assertEqual(f_data, text)
            self.assertEqual(len(f_data), size)

        # verify that file are saved under 3 sub dirs
        dir, file = os.path.split(path)
        num_dir = len(dir.split('/')) 
        self.assertEqual(num_dir, 3)
