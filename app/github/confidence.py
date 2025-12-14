def calculate_confidence(evidence, commits_count):
    signals = sum(1 for v in evidence.values() if v)
    confidence = (signals / len(evidence)) * 0.6

    if commits_count >= 10:
        confidence += 0.3
    elif commits_count >= 3:
        confidence += 0.2
    else:
        confidence += 0.1

    return round(min(confidence, 1.0), 2)
