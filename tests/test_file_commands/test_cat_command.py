from src.file_commands.cat_command import command_cat


class TestCommandCat:
    def test_cat_existing_file(self, fake_filesystem):
        result = command_cat("/test/file1.txt")
        assert result == "casic"

    def test_cat_nonexistent_file(self, fake_filesystem):
        result = command_cat("/test/vasdvas.txt")
        assert result is False

    def test_cat_directory(self, fake_filesystem):
        result = command_cat("/test/directory1")
        assert result is False