from unittest.mock import patch

import pytest
from darca_executor import DarcaExecError

from darca_git.git import GitException


@patch("darca_git.git.DarcaExecutor")
def test_init(mock_executor, git):
    git.executor = mock_executor()
    git.init("/fake/repo")
    git.executor.run.assert_called_with(["git", "init"], cwd="/fake/repo")


@patch("darca_git.git.DarcaExecutor")
def test_clone(mock_executor, git):
    git.executor = mock_executor()
    git.clone("https://repo.url", "/fake/repo")
    git.executor.run.assert_called_with(
        ["git", "clone", "https://repo.url", "."], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_status(mock_executor, git):
    mock = mock_executor()
    mock.run.return_value.stdout = " M README.md"
    git.executor = mock
    output = git.status("/fake/repo")
    assert output == " M README.md"
    mock.run.assert_called_with(
        ["git", "status", "--porcelain"], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_add(mock_executor, git):
    git.executor = mock_executor()
    git.add("file.txt", "/fake/repo")
    git.executor.run.assert_called_with(
        ["git", "add", "file.txt"], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_commit(mock_executor, git):
    git.executor = mock_executor()
    git.commit("message", "/fake/repo")
    git.executor.run.assert_called_with(
        ["git", "commit", "-m", "message"], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_pull(mock_executor, git):
    git.executor = mock_executor()
    git.pull("/fake/repo")
    git.executor.run.assert_called_with(["git", "pull"], cwd="/fake/repo")


@patch("darca_git.git.DarcaExecutor")
def test_push_with_remote(mock_executor, git):
    git.executor = mock_executor()
    git.push("/fake/repo", remote_url="https://origin.url")
    calls = [
        (["git", "remote", "remove", "origin"],),
        (["git", "remote", "add", "origin", "https://origin.url"],),
        (["git", "push", "-u", "origin", "HEAD"],),
    ]
    actual_calls = [call[0][0] for call in git.executor.run.call_args_list]
    for expected in calls:
        assert expected[0] in actual_calls


@patch("darca_git.git.DarcaExecutor")
def test_checkout_branch(mock_executor, git):
    git.executor = mock_executor()
    git.checkout_branch("/fake/repo", "dev", create=True)
    git.executor.run.assert_called_with(
        ["git", "checkout", "-b", "dev"], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_checkout_path(mock_executor, git):
    git.executor = mock_executor()
    git.checkout_path("/fake/repo", ["file1", "file2"])
    git.executor.run.assert_called_with(
        ["git", "checkout", "--", "file1", "file2"], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_checkout_path_from_branch(mock_executor, git):
    git.executor = mock_executor()
    git.checkout_path_from_branch("/fake/repo", "main", ["file.md"])
    git.executor.run.assert_called_with(
        ["git", "checkout", "main", "--", "file.md"], cwd="/fake/repo"
    )


def test_git_exception_structure():
    # Covers line 11: GitException constructor
    exc = GitException(
        "msg", error_code="ERR", metadata={"x": 1}, cause=ValueError("fail")
    )
    assert isinstance(exc, GitException)
    assert exc.error_code == "ERR"
    assert "fail" in str(exc)


@patch("darca_git.git.DarcaExecutor")
def test_run_raises_git_exception(mock_executor, git):
    # Covers lines 28–30: _run() catching DarcaExecError and
    # raising GitException
    mock = mock_executor()
    mock.run.side_effect = DarcaExecError("mock failure")
    git.executor = mock

    with pytest.raises(GitException) as exc:
        git._run(["status"], "/fake/repo", error_code="GIT_STATUS_FAILED")

    assert exc.value.error_code == "GIT_STATUS_FAILED"
    assert "mock failure" in str(exc.value)


@patch("darca_git.git.DarcaExecutor")
def test_checkout_path_str_input(mock_executor, git):
    # Covers line 80: converting string to list
    git.executor = mock_executor()
    git.checkout_path("/fake/repo", "README.md")
    git.executor.run.assert_called_with(
        ["git", "checkout", "--", "README.md"], cwd="/fake/repo"
    )


@patch("darca_git.git.DarcaExecutor")
def test_checkout_path_from_branch_str_input(mock_executor, git):
    # Covers line 86: converting string to list
    git.executor = mock_executor()
    git.checkout_path_from_branch("/fake/repo", "main", "README.md")
    git.executor.run.assert_called_with(
        ["git", "checkout", "main", "--", "README.md"], cwd="/fake/repo"
    )
