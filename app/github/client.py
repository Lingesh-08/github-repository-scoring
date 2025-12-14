import requests

BASE_URL = "https://api.github.com"

class GitHubRepoError(Exception):
    pass


def get_repo(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}"
    r = requests.get(url)

    if r.status_code == 404:
        raise GitHubRepoError("Repository not found or is private")

    if r.status_code != 200:
        raise GitHubRepoError("GitHub API error")

    data = r.json()

    if data.get("private") is True:
        raise GitHubRepoError("Private repositories are not supported")

    return data


def get_contents(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/contents"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else []


def get_commits(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else []
