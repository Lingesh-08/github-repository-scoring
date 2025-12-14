import re

REPO_PATTERN = r"^[a-zA-Z0-9_.-]+\/[a-zA-Z0-9_.-]+$"

def validate_repo_input(repo: str):
    if not re.match(REPO_PATTERN, repo):
        raise ValueError("Invalid format. Use owner/repo")
