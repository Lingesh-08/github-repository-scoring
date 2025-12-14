def generate_roadmap(evidence, score):
    roadmap = []

    # Always prioritize based on missing signals
    if not evidence.get("readme"):
        roadmap.append("Add README with setup and usage instructions")

    if not evidence.get("tests"):
        roadmap.append("Add unit tests to improve reliability")

    if not evidence.get("requirements"):
        roadmap.append("Specify dependencies using requirements.txt or pyproject.toml")

    # Score-based fallback (to guarantee 2–3 items)
    if score < 60:
        if len(roadmap) < 3:
            roadmap.append("Restructure folders for better maintainability")
        if len(roadmap) < 3:
            roadmap.append("Commit code more frequently with meaningful messages")

    elif score < 85:
        if len(roadmap) < 2:
            roadmap.append("Improve documentation and inline comments")
        if len(roadmap) < 3:
            roadmap.append("Introduce basic CI using GitHub Actions")

    else:  # High score repos
        if len(roadmap) < 2:
            roadmap.append("Add automated test coverage")
        if len(roadmap) < 3:
            roadmap.append("Improve issue tracking and contribution guidelines")

    # Final guarantee: max 3 items
    return roadmap[:3]
