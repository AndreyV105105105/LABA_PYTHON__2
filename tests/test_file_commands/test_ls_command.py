import os
from src.file_commands.ls_command import command_ls


class TestCommandLsImplementation:
    def test_ls_current_directory(self, fake_filesystem):
        os.chdir("/test")
        result = command_ls()
        assert result is not False
        assert isinstance(result, list)

    def test_ls_specific_folder(self, fake_filesystem):
        result = command_ls("/test")
        assert result is not False
        assert isinstance(result, list)

    def test_ls_nonexistent_folder(self, fake_filesystem):
        result = command_ls("/rgregwerhreh")
        assert result is False

    def test_ls_one_file(self, fake_filesystem):
        result = command_ls("/test/file1.txt")
        assert result is not False
        assert len(result) == 1

    def test_ls_full_version(self, fake_filesystem):
        result = command_ls("/test", full_version=True)
        assert result is not False
        assert isinstance(result, list)

    def test_ls_empty_folder(self, fake_filesystem):
        fake_filesystem.create_dir("/paaaa")
        result = command_ls("/paaaa")
        assert result == []