# 📤 GitHub Upload Guide - Porter Neural Network Project

This guide will walk you through uploading the Porter NN project to your GitHub repository.

---

## 📋 Pre-Upload Checklist

Before uploading, ensure:

- ✅ All code is tested and working
- ✅ README.md is complete and accurate
- ✅ LICENSE file is present
- ✅ .gitignore is configured
- ✅ Sensitive data removed (API keys, passwords)
- ✅ Large files handled appropriately
- ✅ Documentation is up to date

---

## 🚀 Step-by-Step Upload Process

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon → **"New repository"**
3. Configure your repository:
   - **Repository name**: `PORTER_NN` or `Porter-Delivery-AI`
   - **Description**: `AI-Powered Delivery Time Estimation using Deep Learning Neural Networks for Porter's Intra-City Logistics`
   - **Visibility**: Public (recommended for portfolio) or Private
   - **DO NOT** initialize with README, .gitignore, or license (we have these)
4. Click **"Create repository"**

### Step 2: Initialize Local Git Repository

Open PowerShell/Terminal in the project directory:

```powershell
# Navigate to project directory
cd C:\Users\rattu\Downloads\PORTER_NN

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "feat: initial commit - Porter NN delivery time prediction system"
```

### Step 3: Connect to GitHub

```powershell
# Add remote repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/PORTER_NN.git

# Verify remote
git remote -v
```

### Step 4: Push to GitHub

```powershell
# Push to main branch
git branch -M main
git push -u origin main
```

**If prompted for credentials:**
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (not your password)

---

## 🔑 Creating a Personal Access Token (PAT)

If you need authentication:

1. Go to **GitHub Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Configure:
   - **Note**: "PORTER_NN Upload"
   - **Expiration**: 90 days (or your preference)
   - **Scopes**: Select `repo` (full control of private repositories)
4. Click **"Generate token"**
5. **Copy the token immediately** (you won't see it again!)
6. Use this token as your password when pushing

---

## 📦 Handling Large Files

### Check File Sizes

```powershell
# Find large files (>50MB)
Get-ChildItem -Recurse | Where-Object {$_.Length -gt 50MB} | Select-Object FullName, @{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

### Large File Options

**Option 1: Git LFS (Large File Storage)**

```powershell
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.csv"
git lfs track "*.keras"

# Add .gitattributes
git add .gitattributes
git commit -m "chore: configure Git LFS for large files"
```

**Option 2: Exclude from Repository**

Add to `.gitignore`:
```
# Large data files
data_2.csv
*.keras
```

Then provide download instructions in README.

**Option 3: Use Git Releases**

Upload large files as release assets after initial push.

---

## 🎨 Enhance Your Repository

### Add Topics/Tags

1. Go to your repository on GitHub
2. Click **"⚙️ Settings"** (or the gear icon near "About")
3. Add topics:
   - `machine-learning`
   - `deep-learning`
   - `neural-network`
   - `delivery-prediction`
   - `fastapi`
   - `react`
   - `tensorflow`
   - `logistics`
   - `porter`
   - `eta-prediction`

### Update Repository Description

In the "About" section, add:
- **Description**: AI-Powered Delivery Time Estimation using Deep Learning
- **Website**: Your portfolio URL (if applicable)
- **Topics**: As listed above

### Create a Release

```powershell
# Tag your first release
git tag -a v1.0.0 -m "Release v1.0.0 - Initial production-ready version"
git push origin v1.0.0
```

Then on GitHub:
1. Go to **"Releases"** → **"Create a new release"**
2. Select tag `v1.0.0`
3. Title: `v1.0.0 - Initial Release`
4. Description: Highlight key features
5. Attach large files if needed
6. Click **"Publish release"**

---

## 📸 Add Screenshots

### Create Screenshots Directory

```powershell
# Create directory
mkdir screenshots

# Add screenshots
# - prediction_form.png
# - graph_gallery.png
# - api_docs.png
```

### Capture Screenshots

1. **Prediction Form**: Run the app and capture the main interface
2. **Graph Gallery**: Show the case study visualization
3. **API Docs**: Visit `http://localhost:8000/docs` and capture

### Update README

Ensure screenshot paths in README.md are correct:
```markdown
![Prediction Form](screenshots/prediction_form.png)
```

---

## 🔍 Verify Upload

After pushing, verify:

1. ✅ All files uploaded correctly
2. ✅ README displays properly
3. ✅ License is recognized by GitHub
4. ✅ .gitignore is working (node_modules, __pycache__ not uploaded)
5. ✅ Topics/tags are visible
6. ✅ Repository description is clear

---

## 🛠️ Troubleshooting

### Issue: "Repository not found"

**Solution**: Verify remote URL
```powershell
git remote -v
git remote set-url origin https://github.com/YOUR_USERNAME/PORTER_NN.git
```

### Issue: "Authentication failed"

**Solution**: Use Personal Access Token instead of password

### Issue: "File too large" (>100MB)

**Solutions**:
1. Use Git LFS
2. Exclude from repository
3. Split into smaller files

### Issue: "Permission denied"

**Solution**: Check repository permissions and PAT scopes

### Issue: "Merge conflicts"

**Solution**: 
```powershell
git pull origin main --rebase
# Resolve conflicts
git push origin main
```

---

## 📝 Post-Upload Tasks

### 1. Enable GitHub Pages (Optional)

For project documentation:
1. Go to **Settings** → **Pages**
2. Source: Deploy from branch `main` → `/docs`
3. Create `/docs` folder with documentation

### 2. Set Up Branch Protection

1. Go to **Settings** → **Branches**
2. Add rule for `main` branch
3. Enable:
   - Require pull request reviews
   - Require status checks

### 3. Add GitHub Actions (Optional)

Create `.github/workflows/ci.yml` for automated testing:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r backend/requirements.txt
      - name: Run tests
        run: |
          pytest backend/tests/
```

### 4. Add Social Preview Image

1. Create a 1280x640px banner image
2. Go to **Settings** → **Options**
3. Upload in "Social preview" section

---

## 🎯 Quick Command Reference

```powershell
# Initial setup
git init
git add .
git commit -m "feat: initial commit"
git remote add origin https://github.com/YOUR_USERNAME/PORTER_NN.git
git branch -M main
git push -u origin main

# Subsequent updates
git add .
git commit -m "feat: add new feature"
git push

# Create new branch
git checkout -b feature/new-feature
git push -u origin feature/new-feature

# Pull latest changes
git pull origin main

# Check status
git status
git log --oneline
```

---

## 📞 Need Help?

- 📖 [GitHub Docs](https://docs.github.com)
- 💬 [GitHub Community](https://github.community)
- 🎓 [Git Tutorial](https://git-scm.com/docs/gittutorial)

---

## ✅ Final Checklist

Before sharing your repository:

- [ ] Repository is public (if intended for portfolio)
- [ ] README is complete and professional
- [ ] All links in README work
- [ ] Screenshots are added and display correctly
- [ ] License is present
- [ ] Topics/tags are added
- [ ] Repository description is clear
- [ ] No sensitive data committed
- [ ] Installation instructions tested
- [ ] Contact information is correct
- [ ] Contributing guidelines present

---

## 🎉 Success!

Your Porter NN project is now on GitHub! 

**Next Steps:**
1. Share the repository link on LinkedIn
2. Add to your portfolio
3. Star your own repo (why not? 😄)
4. Share with the community

**Repository URL Format:**
```
https://github.com/YOUR_USERNAME/PORTER_NN
```

---

**Good luck with your project showcase! 🚀**

Made with ❤️ by Ratnesh Kumar
