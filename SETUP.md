# 🚀 Setup & GitHub Push Instructions

This guide will help you initialize git and push this repository to GitHub.

---

## Prerequisites

1. **Git installed** — Check with `git --version`
2. **GitHub account** — https://github.com
3. **GitHub CLI (optional but recommended)** — `brew install gh` (macOS)

---

## Step 1: Initialize Local Git Repository

Navigate to the repository folder and initialize git:

```bash
cd ~/Documents/ClaudePractice/dsa-mastery-30-days
git init
```

---

## Step 2: Configure Git (First Time Only)

Set your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "devathrajharish@gmail.com"
```

To verify:
```bash
git config --global user.name
git config --global user.email
```

---

## Step 3: Create Initial Commit

```bash
git add .
git commit -m "Initial commit: 30-Day DSA Mastery Plan structure"
```

---

## Step 4: Create GitHub Repository

### Option A: Using GitHub Web Interface (Easiest)

1. Go to https://github.com/new
2. Repository name: `dsa-mastery-30-days`
3. Description: "30-Day DSA Mastery Plan in Python — Master 15 core patterns"
4. Make it **Public** (so others can benefit)
5. **Do NOT** initialize with README, .gitignore, or LICENSE
6. Click **Create repository**

### Option B: Using GitHub CLI

```bash
gh repo create dsa-mastery-30-days \
  --public \
  --description "30-Day DSA Mastery Plan in Python — Master 15 core patterns" \
  --source=. \
  --remote=origin \
  --push
```

---

## Step 5: Link Remote and Push

If you used the web interface, link your remote and push:

```bash
git remote add origin https://github.com/devathrajharish/dsa-mastery-30-days.git
git branch -M main
git push -u origin main
```

Verify the remote:
```bash
git remote -v
```

---

## Step 6: Verify on GitHub

Visit: https://github.com/devathrajharish/dsa-mastery-30-days

You should see:
- ✅ All 30 Day folders
- ✅ README.md
- ✅ PROGRESS.md
- ✅ MISTAKES_LOG.md
- ✅ Your solutions in each day's folder

---

## Daily Workflow

### After completing each day:

```bash
# See changes
git status

# Stage all changes for the day
git add Day-XX/

# Commit with meaningful message
git commit -m "Complete Day XX: [Topic Name] - Solved 2 problems, mastered pattern"

# Push to GitHub
git push
```

### Example commits:
```bash
git commit -m "Complete Day 01: Big-O and Array Fundamentals"
git commit -m "Complete Day 05: Two Pointers Arrays - Solutions working"
git commit -m "Update Day 10: Add Prefix Sum detailed explanation"
```

---

## Useful Git Commands

### View commit history:
```bash
git log --oneline
```

### See what changed:
```bash
git diff Day-XX/
```

### Undo last commit (if you made a mistake):
```bash
git reset --soft HEAD~1
```

### Check status:
```bash
git status
```

---

## GitHub Features to Use

### 1. Track Progress with Issues
Create GitHub Issues for:
- [ ] Days that need review
- [ ] Patterns you want to revisit
- [ ] Challenging problems

### 2. Use Discussions
Start discussions for:
- Sharing insights
- Asking for code review
- Problem explanations

### 3. GitHub Projects
Create a GitHub Project board:
- Column 1: Not Started (30 items)
- Column 2: In Progress
- Column 3: Completed

To create: Settings → Projects → New project

### 4. Add Badges to README
Show your progress with badges:

```markdown
![Progress](https://img.shields.io/badge/progress-0%2F30-blue)
![Week 1](https://img.shields.io/badge/week%201-0%2F7-inactive)
![Week 2](https://img.shields.io/badge/week%202-0%2F8-inactive)
![Week 3](https://img.shields.io/badge/week%203-0%2F7-inactive)
![Week 4](https://img.shields.io/badge/week%204-0%2F8-inactive)
```

---

## Make It Awesome

### Add a Cover Image
Create a simple cover image and save as `cover.png`, then update README:

```markdown
![DSA Mastery Cover](cover.png)
```

### Add a GitHub Actions Workflow (Optional)
Automatically run your Python solutions when you push:

Create `.github/workflows/test.yml`:

```yaml
name: Test Solutions

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Run solutions
      run: |
        for day in Day-*/solutions/*.py; do
          python $day
        done
```

### Star and Share
- ⭐ Star your own repository (motivation!)
- 📢 Share with friends
- 🤝 Contribute to others' DSA repositories

---

## Troubleshooting

### "fatal: not a git repository"
Make sure you're in the correct directory:
```bash
cd ~/Documents/ClaudePractice/dsa-mastery-30-days
```

### "Permission denied (publickey)"
Set up SSH keys:
```bash
ssh-keygen -t ed25519 -C "devathrajharish@gmail.com"
# Add the public key to GitHub: Settings → SSH and GPG keys
```

### "Everything up-to-date"
This means there are no changes since the last push. Make changes and commit first.

---

## Next Steps

1. ✅ Initialize git
2. ✅ Create GitHub repository
3. ✅ Push initial commit
4. ✅ Start Day 01 — Big-O and Array Fundamentals
5. ✅ Commit daily progress
6. ✅ Review PROGRESS.md weekly
7. ✅ Share your repository on Twitter/LinkedIn
8. ✅ Celebrate on Day 30! 🎉

---

## Resources

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com
- **GitHub CLI:** https://cli.github.com
- **How to write good commit messages:** https://chris.beams.io/posts/git-commit/

---

*Good luck! Track your progress and push consistently. You've got this! 🚀*
