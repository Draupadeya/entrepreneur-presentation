# Entrepreneur Presentation — Django

This repository contains a small Django site with two case-study presentations (PepperTap and Walmart), visual animations and a dynamic index page.

Quick push instructions

1. From the project root (`case_study_site`) run:

```bash
git init
git add .
git commit -m "Initial commit — presentation site"
```

2. Add the GitHub remote and push (replace `main` if your default branch differs):

```bash
git remote add origin https://github.com/Draupadeya/entrepreneur-presentation.git
git branch -M main
git push -u origin main
```

Notes

- If your repo is private or you have 2FA enabled, use a Personal Access Token (PAT) instead of your password when prompted, or configure SSH keys and use the SSH remote URL.
- Before pushing to production services, ensure `SECRET_KEY` is set via environment variables and `DEBUG=False`.
- Consider adding a `requirements.txt` by running `pip freeze > requirements.txt`.

If you want, I can create the initial git commit and attempt to push from this environment — but I'll need your guidance on authentication (PAT or SSH) or you can run the commands locally (recommended).