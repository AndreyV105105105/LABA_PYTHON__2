from unittest.mock import patch
from src.auxiliary_functions.rm import rm


class TestRmCommand:
    def test_rm_with_files(self):
        with patch('src.auxiliary_functions.rm.command_rm') as mock_command:
            mock_command.return_value = True
            result = rm(["file1.txt", "file2.txt"])
            assert result is True
            mock_command.assert_called_once_with(["file1.txt", "file2.txt"], False)

    def test_rm_with_r(self):
        with patch('src.auxiliary_functions.rm.command_rm') as mock_command:
            mock_command.return_value = True
            result = rm(["-r", "dir1"])
            assert result is True
            mock_command.assert_called_once_with(["dir1"], True)

    def test_rm_no_arguments(self):
        with patch('src.auxiliary_functions.rm.command_rm') as mock_command:
            result = rm([])
            assert result is True