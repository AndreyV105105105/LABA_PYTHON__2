import pytest
from src.additional_functions.is_directory_protected import is_path_protected


class TestProtectedDirectories:
    def test_root_directory_is_protected(self):
        assert is_path_protected("/") is True

    def test_parent_directory_is_protected(self):
        assert is_path_protected("..") is True

    def test_current_directory_is_protected(self):
        assert is_path_protected(".") is True

    def test_regular_folder_is_not_protected(self, fake_filesystem):
        assert is_path_protected("/test/directory1") is False

    def test_regular_file_is_not_protected(self, fake_filesystem):
        assert is_path_protected("/test/file1.txt") is False