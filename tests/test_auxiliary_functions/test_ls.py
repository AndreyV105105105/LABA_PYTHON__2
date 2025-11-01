from unittest.mock import patch
from src.auxiliary_functions.ls import ls


class TestLsCommand:
    def test_ls_without_arguments(self):
        with patch('src.auxiliary_functions.ls.command_ls') as mock_command:
            mock_command.return_value = ["file1.txt", "file2.txt"]
            result = ls([])
            assert result is True
            mock_command.assert_called_once_with(None, False)

    def test_ls_with_folder_argument(self):
        with patch('src.auxiliary_functions.ls.command_ls') as mock_command:
            mock_command.return_value = ["file1.txt"]
            result = ls(["/test/directory1"])
            assert result is True
            mock_command.assert_called_once_with("/test/directory1", False)

    def test_ls_with_l(self):
        with patch('src.auxiliary_functions.ls.command_ls') as mock_command:
            mock_command.return_value = ["много инфы"]
            result = ls(["-l"])
            assert result is True
            mock_command.assert_called_once_with(None, True)

    def test_ls_with_many_folders(self):
        with patch('src.auxiliary_functions.ls.command_ls') as mock_command:
            mock_command.side_effect = [
                ["файлы из первой папки"],
                ["файлы из второй папки"]
            ]
            result = ls(["/папка1", "/папка2"])
            assert result is True
            assert mock_command.call_count == 2

    def test_ls_when_command_fails(self):
        with patch('src.auxiliary_functions.ls.command_ls') as mock_command:
            mock_command.return_value = False
            result = ls(["/thrthyrhhwthrt"])
            assert result is True