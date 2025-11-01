from unittest.mock import patch
from src.file_commands.rm_command import command_rm


class TestCommandRm:
    def test_rm_file(self, fake_filesystem):
        result = command_rm(["/test/file1.txt"], None)
        assert result is True

    def test_rm_nonexistent_file(self, fake_filesystem):
        result = command_rm(["/test/nonexistent.txt"], None)
        assert result is True

    def test_rm_directory_without_r(self, fake_filesystem):
        result = command_rm(["/test/directory1"], None)
        assert result is True

    def test_rm_directory_with_r_yes(self, fake_filesystem):
        with patch('builtins.input', return_value='y'):
            result = command_rm(["/test/directory1"], True)
            assert result is True

    def test_rm_directory_with_r_no(self, fake_filesystem):
        with patch('builtins.input', return_value='n'):
            result = command_rm(["/test/directory1"], True)
            assert result is True

    def test_rm_many_files(self, fake_filesystem):
        result = command_rm(["/test/file1.txt", "/test/file2.txt"], None)
        assert result is True