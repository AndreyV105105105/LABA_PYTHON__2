from unittest.mock import patch
from src.auxiliary_functions.cat import cat


class TestCatCommand:
    def test_cat_with_files(self, fake_filesystem):
        with patch('src.auxiliary_functions.cat.command_cat') as mock_command:
            mock_command.return_value = "file content"
            result = cat(["file1.txt", "file2.txt"])
            assert result is True
            assert mock_command.call_count == 2

    def test_cat_with_single_file(self, fake_filesystem):
        with patch('src.auxiliary_functions.cat.command_cat') as mock_command:
            mock_command.return_value = "file content"
            result = cat(["file1.txt"])
            assert result is True
            mock_command.assert_called_once_with("file1.txt")

    def test_cat_no_arguments(self, fake_filesystem):
        with patch('src.auxiliary_functions.cat.command_cat') as mock_command:
            result = cat([])
            assert result is True
            mock_command.assert_not_called()

    def test_cat_command_fails(self, fake_filesystem):
        with patch('src.auxiliary_functions.cat.command_cat') as mock_command:
            mock_command.return_value = False
            result = cat(["nonexistent.txt"])
            assert result is True