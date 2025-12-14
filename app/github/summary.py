def generate_summary(score, evidence):
    if score >= 85:
        return "Excellent project depth and clean codebase."
    elif score >= 60:
        return "Strong code consistency and folder structure; needs more tests and documentation."
    else:
        return "Basic project structure but poor documentation and inconsistent commits."
