from unittest.mock import patch
from src.auxiliary_functions.cd import cd


class TestCdCommand:
    def test_cd_with_path(self):
        with patch('src.auxiliary_functions.cd.command_cd') as mock_command:
            mock_command.return_value = True
            result = cd(["/test/directory1"])
            assert result is True
            mock_command.assert_called_once_with("/test/directory1")

    def test_cd_no_arguments(self):
        with patch('src.auxiliary_functions.cd.command_cd') as mock_command:
            mock_command.return_value = True
            result = cd([])
            assert result is True
            mock_command.assert_called_once_with(None)

    def test_cd_many_arguments(self):
        with patch('src.auxiliary_functions.cd.command_cd') as mock_command:
            result = cd(["/path1", "/path2"])
            assert result is True