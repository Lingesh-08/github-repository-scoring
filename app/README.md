# GitHub Repository Quality Scorer

An automated tool that analyzes **public GitHub repositories** and generates a
**quality score out of 100**, along with a concise summary and an actionable improvement roadmap.

The scoring is **rule-based and explainable**, focusing on real engineering signals
rather than subjective opinions.

## What This Tool Does

Given a public GitHub repository URL, the tool:

- Analyzes repository structure, metadata, and commit activity
- Computes a quality score (0–100)
- Generates a short, human-readable summary
- Suggests 2–3 concrete improvements (roadmap)

This tool evaluates **engineering quality**, not business value.

## Input Format

Only **public GitHub repositories** are supported.

Example:
https://github.com/rahul-dev-ai/todo-app