from validator import validate_file


def test_valid_file(tmp_path):
    tmp_file = tmp_path / "test_file.png"
    target_size = 5 * 1024 * 1024

    with open(tmp_file, "wb") as f:
        f.truncate(target_size)

    result = validate_file(tmp_file)
    assert result["valid"] is True and result["errors"] == []


def test_invalid_file_ext(tmp_path):
    tmp_file = tmp_path / "random.txt"
    target_size = 12 * 1024

    with open(tmp_file, "wb") as f:
        f.truncate(target_size)

    result = validate_file(tmp_file)
    assert result["valid"] is False and any(
        "invalid file extension" in error for error in result["errors"])


def test_invalid_file_size(tmp_path):
    tmp_file = tmp_path / "image.jpg"
    target_size = 2 * 1024

    with open(tmp_file, "wb") as f:
        f.truncate(target_size)

    result = validate_file(tmp_file)
    assert result["valid"] is False and any(
        "invalid file size" in error for error in result["errors"])


def test_invalid_file_name(tmp_path):
    tmp_file = tmp_path / "12-Na Me.jpeg"
    target_size = 50 * 1024

    with open(tmp_file, "wb") as f:
        f.truncate(target_size)

    result = validate_file(tmp_file)
    assert result["valid"] is False and any(
        "invalid file name" in error for error in result["errors"])


def test_multiple_errors(tmp_path):
    tmp_file = tmp_path / "some_model.blend"
    target_size = 100 * 1024 * 1024

    with open(tmp_file, "wb") as f:
        f.truncate(target_size)

    result = validate_file(tmp_file)
    size_error = any(
        "invalid file size" in error for error in result["errors"])
    ext_error = any(
        "invalid file extension" in error for error in result["errors"])
    assert result["valid"] is False and size_error and ext_error


def test_not_a_file(tmp_path):
    tmp_file = tmp_path / "nothing.jpeg"

    result = validate_file(tmp_file)
    assert result["valid"] is False and any(
        "invalid file" in error for error in result["errors"])
