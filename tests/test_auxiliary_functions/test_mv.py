from unittest.mock import patch
from src.auxiliary_functions.mv import mv


class TestMvCommand:
    def test_mv_with_files(self):
        with patch('src.auxiliary_functions.mv.command_mv') as mock_command:
            mock_command.return_value = True
            result = mv(["file1.txt", "file2.txt"])
            assert result is True
            mock_command.assert_called_once_with(["file1.txt", "file2.txt"])

    def test_mv_one_argument(self):
        with patch('src.auxiliary_functions.mv.command_mv') as mock_command:
            result = mv(["file1.txt"])
            assert result is True
            mock_command.assert_called_once_with(["file1.txt"])

    def test_mv_no_arguments(self):
        with patch('src.auxiliary_functions.mv.command_mv') as mock_command:
            result = mv([])
            assert result is True