def analyze_metadata(repo):
    score = 0
    evidence = {}

    if repo.get("description"):
        score += 5
        evidence["description"] = True
    else:
        evidence["description"] = False

    if repo.get("license"):
        score += 5
        evidence["license"] = True
    else:
        evidence["license"] = False

    if repo.get("size", 0) > 100:
        score += 10

    return score, evidence  # max 20


def analyze_structure(contents):
    filenames = [item["name"].lower() for item in contents]

    score = 0
    evidence = {
        "readme": False,
        "requirements": False,
        "tests": False
    }

    if any("readme" in f for f in filenames):
        score += 10
        evidence["readme"] = True

    if any("requirements" in f or "pyproject" in f for f in filenames):
        score += 5
        evidence["requirements"] = True

    if any("test" in f for f in filenames):
        score += 5
        evidence["tests"] = True

    return score, evidence  # max 20

def analyze_commits(commits):
    if len(commits) >= 15:
        return 20
    elif len(commits) >= 5:
        return 10
    return 5
