import pytest


@pytest.fixture
def fake_filesystem(fs):
    fs.create_dir("/test")
    fs.create_dir("/test/directory1")
    fs.create_dir("/test/directory2")
    fs.create_file("/test/file1.txt", contents="casic")
    fs.create_file("/test/file2.txt", contents="zlo")
    fs.create_file("/test/directory1/aboba.txt", contents="ivanZolo")
    return fs


@pytest.fixture
def home_directory(fake_filesystem):
    fake_filesystem.create_dir("/home/user")
    fake_filesystem.create_file("/home/user/zalupa.txt", contents="fart")
    return fake_filesystem


@pytest.fixture
def mock_logger(mocker):
    return mocker.Mock()


@pytest.fixture
def mock_path(mocker):
    return mocker.patch("pathlib.Path")