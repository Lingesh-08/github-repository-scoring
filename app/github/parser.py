import re

def parse_github_input(text: str):
    text = text.strip()

    # Full GitHub URL
    match = re.match(r"https:\/\/github\.com\/([^\/]+)\/([^\/]+)", text)
    if match:
        return match.group(1), match.group(2)

    # owner/repo format
    if "/" in text:
        owner, repo = text.split("/")
        return owner, repo

    raise ValueError("Invalid GitHub repository input")
