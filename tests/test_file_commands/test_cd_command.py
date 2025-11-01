import os
from src.file_commands.cd_command import command_cd


class TestCommandCd:
    def test_cd_existing_directory(self, fake_filesystem):
        original_dir = os.getcwd()
        result = command_cd("/test/directory1")
        assert result is True
        assert os.getcwd() == "C:\\test\\directory1"
        os.chdir(original_dir)

    def test_cd_nonexistent_directory(self, fake_filesystem):
        result = command_cd("/vsavsdav")
        assert result is False

    def test_cd_file_path(self, fake_filesystem):
        result = command_cd("/test/file1.txt")
        assert result is False

    def test_cd_home_directory(self, fake_filesystem):
        original_dir = os.getcwd()
        result = command_cd("~")
        assert result is True
        os.chdir(original_dir)

    def test_cd_no_arguments(self, fake_filesystem):
        original_dir = os.getcwd()
        result = command_cd(None)
        assert result is True
        os.chdir(original_dir)