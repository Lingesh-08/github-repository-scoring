from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.github.parser import parse_github_input
from app.github.client import get_repo, get_contents, get_commits, GitHubRepoError
from app.github.analyzer import analyze_metadata, analyze_structure, analyze_commits
from app.github.scorer import calculate_score
from app.github.roadmap import generate_roadmap
from app.github.validator import validate_repo_input
from app.github.summary import generate_summary
from app.github.confidence import calculate_confidence

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
def analyze(request: Request, repo: str = Form(...)):
    try:
        owner, name = parse_github_input(repo)
        repo_data = get_repo(owner, name)
        contents = get_contents(owner, name)
        commits = get_commits(owner, name)

        meta_score, meta_evidence = analyze_metadata(repo_data)
        struct_score, struct_evidence = analyze_structure(contents)
        commit_score = analyze_commits(commits)

        score = meta_score + struct_score + commit_score

        evidence = {**meta_evidence, **struct_evidence}

        summary = generate_summary(score, evidence)
        roadmap = generate_roadmap(evidence, score)
        confidence = calculate_confidence(evidence, len(commits))

        breakdown = {
            "Repository Hygiene": f"{meta_score} / 20",
            "Structure & Practicality": f"{struct_score} / 20",
            "Commit Quality": f"{commit_score} / 20"
        }

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "score": score,
                "summary": summary,
                "roadmap": roadmap,
                "breakdown": breakdown,
                "confidence": confidence
            }

        )

    except (ValueError, GitHubRepoError) as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": str(e)
            }
        )
