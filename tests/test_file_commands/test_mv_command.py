from src.file_commands.mv_command import command_mv


class TestCommandMv:
    def test_mv_file_to_file(self, fake_filesystem):
        result = command_mv(["/test/file1.txt", "/test/file3.txt"])
        assert result is True

    def test_mv_file_to_directory(self, fake_filesystem):
        result = command_mv(["/test/file1.txt", "/test/directory1"])
        assert result is True

    def test_mv_nonexistent_source(self, fake_filesystem):
        result = command_mv(["/test/nonexistent.txt", "/test/directory1"])
        assert result is False

    def test_mv_directory_to_file(self, fake_filesystem):
        result = command_mv(["/test/directory1", "/test/file1.txt"])
        assert result is False

    def test_mv_many_files(self, fake_filesystem):
        result = command_mv(["/test/file1.txt", "/test/file2.txt", "/test/directory1"])
        assert result is True

    def test_mv_same_file(self, fake_filesystem):
        result = command_mv(["/test/file1.txt", "/test/file1.txt"])
        assert result is False