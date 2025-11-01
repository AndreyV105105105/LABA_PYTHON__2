from src.file_commands.cp_command import command_cp


class TestCommandCp:
    def test_cp_file_to_file(self, fake_filesystem):
        result = command_cp(["/test/file1.txt", "/test/file3.txt"], None)
        assert result is True

    def test_cp_file_to_directory(self, fake_filesystem):
        result = command_cp(["/test/file1.txt", "/test/directory1"], None)
        assert result is True

    def test_cp_nonexistent_source(self, fake_filesystem):
        result = command_cp(["/test/vsdavasdvasv.txt", "/test/directory1"], None)
        assert result is False

    def test_cp_directory_without_r(self, fake_filesystem):
        result = command_cp(["/test/directory1", "/test/directory3"], None)
        assert result is False

    def test_cp_directory_with_r(self, fake_filesystem):
        result = command_cp(["/test/directory1", "/test/directory3"], True)
        assert result is True

    def test_cp_many_files(self, fake_filesystem):
        result = command_cp(["/test/file1.txt", "/test/file2.txt", "/test/directory1"], None)
        assert result is True

    def test_cp_same_file(self, fake_filesystem):
        result = command_cp(["/test/file1.txt", "/test/file1.txt"], None)
        assert result is False