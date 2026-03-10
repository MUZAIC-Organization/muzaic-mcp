"""Basic tests for Muzaic MCP Server."""

from muzaic_mcp import __version__
from muzaic_mcp.server import (
    _validate_params,
    _format_generation_result,
)


def test_version():
    assert __version__ == "1.0.0"


def test_validate_params_valid():
    assert _validate_params({"intensity": 5, "tempo": 3}) is None


def test_validate_params_out_of_range():
    result = _validate_params({"intensity": 10})
    assert result is not None
    assert "out of range" in result


def test_validate_params_invalid_key():
    result = _validate_params({"volume": 5})
    assert result is not None
    assert "Unknown parameter" in result


def test_validate_params_keyframes():
    assert _validate_params({"intensity": [[0, 2], [50, 5], [100, 9]]}) is None


def test_validate_params_keyframes_bad_position():
    result = _validate_params({"intensity": [[150, 5]]})
    assert result is not None
    assert "position" in result.lower()


def test_validate_params_tempo_rejects_keyframes():
    result = _validate_params({"tempo": [[0, 3], [100, 7]]})
    assert result is not None
    assert "static" in result.lower() or "keyframes" in result.lower()


def test_format_generation_result():
    data = {"url": "https://example.com/audio.mp3", "hash": "abc123", "duration": 60}
    result = _format_generation_result(data)
    assert result["status"] == "success"
    assert result["audio_url"] == "https://example.com/audio.mp3"
    assert result["tokens_used"] == 60
