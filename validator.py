import re

ALLOWED_EXTENSIONS = [".png", ".jpg", ".jpeg"]
MIN_FILE_SIZE = 10 * 1024
MAX_FILE_SIZE = 50 * 1024 * 1024
PATTERNS = [
    r"^[a-z0-9_]+\.\w+$",
    r"^[a-z0-9_]+\.tar\.gz$",
]


def matches_naming_rule(file):
    for pattern in PATTERNS:
        if re.match(pattern, file):
            return True
    return False


def validate_file(file) -> dict:
    errors = []
    if file.is_file():
        if file.suffix not in ALLOWED_EXTENSIONS:
            errors.append(f"invalid file extension : {file.name}")

        if not MIN_FILE_SIZE < file.stat().st_size < MAX_FILE_SIZE:
            errors.append(f"invalid file size : {file.name}")

        if not matches_naming_rule(file.name):
            errors.append(f"invalid file name : {file.name}")

        valid = (len(errors) == 0)

        return {"valid": valid, "errors": errors}

    return {"valid": False, "errors": [f"invalid file : {file.name}"]}
