def calculate_score(meta, structure, commits):
    total = meta + structure + commits
    return min(100, total)
