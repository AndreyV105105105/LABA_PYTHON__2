from src.additional_functions.functions_for_ls import get_file_permissions, get_file_size, get_file_time

from pathlib import Path

class TestFileInfoFunctions:
    def test_get_permissions_for_real_file(self, fake_filesystem):
        permissions = get_file_permissions("/test/file1.txt")

        assert permissions is not False
        assert isinstance(permissions, str)

    def test_get_permissions_for_missing_file(self, fake_filesystem):
        result = get_file_permissions("/vedvwergvwe/afefwefwfe.txt")
        assert result is False

    def test_get_file_size_success(self, fake_filesystem):
        size = get_file_size("/test/file1.txt")
        expected_size = str(Path("/test/file1.txt").stat().st_size)
        assert size == expected_size

    def test_get_file_size_for_directory(self, fake_filesystem):
        size = get_file_size("/test/directory1")
        assert size is not False

    def test_get_file_time(self, fake_filesystem):
        file_time = get_file_time("/test/file1.txt")

        assert file_time is not False
        assert len(file_time) > 10

    def test_get_file_time_for_bad_path(self, fake_filesystem):
        result = get_file_time("/fewfwefwefwefwe/efwqfqwegrheqrhreqh")
        assert result is False