import unittest
from funker import *


test_path = "F:\\tmp\\testdata"
class TestUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search_files_found(self):
        exp_result = [os.path.join(test_path, 'folder3\\file3.txt'), os.path.join(test_path, 'folder4\\file3.txt'),
                      os.path.join(test_path, 'folder5\\file3.txt')]
        self.assertEqual(exp_result, search_files(test_path, "file3"), f"Search for existing files: not working")

    def test_search_files_not_found(self):
        exp_result = None
        self.assertEqual(exp_result, search_files(test_path, "file99"), f"Search for not existing files: not working")

    def test_count_files(self):
        self.assertEqual(4, count_files(os.path.join(test_path,"folder4"), recursive=False), f"Count: not 20 files")

    def test_count_files_recursive(self):
        self.assertEqual(15, count_files(test_path, recursive=True), f"Count: not 15 files")

    def test_format_size(self):
        self.assertEqual(format_size(0), "0B")
        self.assertEqual(format_size(1024), "1.0 KB")
        self.assertEqual(format_size(1048576), "1.0 MB")
        self.assertEqual(format_size(1073741824), "1.0 GB")
        self.assertEqual(format_size(1099511627776), "1.0 TB")

def setUpModule():
    generate_data(test_path, 5)

def tearDownModule():
    shutil.rmtree(test_path)

if __name__ == '__main__':
    unittest.main()