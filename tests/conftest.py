import pytest

from darca_git.git import Git


@pytest.fixture
def git():
    return Git()
