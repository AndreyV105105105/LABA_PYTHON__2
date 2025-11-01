from unittest.mock import patch
from src.auxiliary_functions.cp import cp


class TestCpCommand:
    def test_cp_with_files(self):
        with patch('src.auxiliary_functions.cp.command_cp') as mock_command:
            mock_command.return_value = True
            result = cp(["file1.txt", "file2.txt"])
            assert result is True
            mock_command.assert_called_once_with(["file1.txt", "file2.txt"], False)

    def test_cp_with_r(self):
        with patch('src.auxiliary_functions.cp.command_cp') as mock_command:
            mock_command.return_value = True
            result = cp(["-r", "dir1", "dir2"])
            assert result is True
            mock_command.assert_called_once_with(["dir1", "dir2"], True)

    def test_cp_no_arguments(self):
        with patch('src.auxiliary_functions.cp.command_cp') as mock_command:
            result = cp([])
            assert result is True