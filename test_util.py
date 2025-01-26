import unittest
from funker import *


test_path = "F:\\tmp\\testdata"
class TestUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search_files_found(self):
        # Rewrite this one for relative path
        exp_result = ['F:\\tmp\\testdata\\folder3\\file3.txt', 'F:\\tmp\\testdata\\folder4\\file3.txt',
                      'F:\\tmp\\testdata\\folder5\\file3.txt']
        self.assertEqual(exp_result, search_files(test_path, "file3"), f"Search for existing files: not working")

    def test_search_files_not_found(self):
        exp_result = None
        self.assertEqual(exp_result, search_files(test_path, "file99"), f"Search for not existing files: not working")

    def test_count_files(self):
        self.assertEqual(4, count_files(os.path.join(test_path,"folder4"), recursive=False), f"Count: not 20 files")

    def test_count_files_recursive(self):
        self.assertEqual(15, count_files(test_path, recursive=True), f"Count: not 15 files")

def setUpModule():
    generate_data(test_path, 5)

def tearDownModule():
    pass

if __name__ == '__main__':
    unittest.main()