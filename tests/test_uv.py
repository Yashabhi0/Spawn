import subprocess
from unittest.mock import patch

import pytest

from spawn.core.exceptions import SpawnError
from spawn.utils.uv import initialize_uv


def _make_called_process_error(stderr: str) -> subprocess.CalledProcessError:
    exc = subprocess.CalledProcessError(
        returncode=1,
        cmd=["uv", "init", "--bare"],
    )
    exc.stderr = stderr
    return exc


@patch("subprocess.run")
def test_uv_stderr_included_in_spawn_error(mock_run, tmp_path):
    mock_run.side_effect = _make_called_process_error(
        "error: Python 3.12 not found"
    )

    with pytest.raises(SpawnError) as exc_info:
        initialize_uv(tmp_path)

    assert "Python 3.12 not found" in str(exc_info.value)


@patch("subprocess.run")
def test_uv_empty_stderr_uses_fallback_message(mock_run, tmp_path):
    mock_run.side_effect = _make_called_process_error("")

    with pytest.raises(SpawnError) as exc_info:
        initialize_uv(tmp_path)

    assert str(exc_info.value) == "Failed to initialize UV environment."


@patch("subprocess.run")
def test_uv_exception_is_chained(mock_run, tmp_path):
    original = _make_called_process_error("disk full")
    mock_run.side_effect = original

    with pytest.raises(SpawnError) as exc_info:
        initialize_uv(tmp_path)

    assert exc_info.value.__cause__ is original
