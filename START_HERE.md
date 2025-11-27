# 🎯 START HERE - Porter NN Project

Welcome to the **Porter Neural Network Delivery Time Prediction** project! 

This document will guide you through getting started quickly.

---

## 🚀 Quick Start (5 Minutes)

### Option 1: Automated Setup (Recommended)

```powershell
# Run the automated setup script
.\setup.ps1

# Then run the application
.\run.ps1
```

That's it! The browser will open automatically at `http://localhost:5173`

### Option 2: Manual Setup

**Terminal 1 - Backend:**
```powershell
pip install -r backend/requirements.txt
cd backend
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm install
npm run dev
```

---

## 📚 Documentation Guide

Depending on what you need, start with the right document:

### 🎯 For First-Time Users
- **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
- **[README.md](README.md)** - Complete project documentation

### 👨‍💻 For Developers
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Technical deep dive

### 📤 For GitHub Upload
- **[GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)** - Step-by-step upload instructions
- **[UPLOAD_CHECKLIST.md](UPLOAD_CHECKLIST.md)** - Pre-upload verification

### 📖 For Reference
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[LICENSE](LICENSE)** - MIT License

---

## 🎓 What This Project Does

Porter NN predicts delivery times for intra-city logistics using:

- **Deep Learning**: Neural network with 175K+ training samples
- **High Accuracy**: 4.16 minutes Mean Absolute Error
- **Full Stack**: React frontend + FastAPI backend
- **Production Ready**: Complete with API, UI, and documentation

---

## 🏗️ Project Structure

```
PORTER_NN/
├── 📄 START_HERE.md          ← You are here!
├── 📄 README.md              ← Main documentation
├── 📄 QUICKSTART.md          ← Quick setup guide
├── 📄 GITHUB_UPLOAD_GUIDE.md ← Upload instructions
│
├── 🐍 backend/               ← Python API
│   ├── main.py              ← FastAPI server
│   ├── train_model.py       ← Model training
│   ├── model.keras          ← Trained model
│   └── requirements.txt     ← Dependencies
│
├── ⚛️ frontend/              ← React UI
│   ├── src/App.jsx          ← Main component
│   ├── package.json         ← Dependencies
│   └── public/graphs/       ← Visualizations
│
├── 🔧 setup.ps1             ← Automated setup
└── ▶️ run.ps1               ← Quick run script
```

---

## ✅ Prerequisites

Before you start, ensure you have:

- ✅ **Python 3.8+** - [Download](https://www.python.org/downloads/)
- ✅ **Node.js 16+** - [Download](https://nodejs.org/)
- ✅ **Git** - [Download](https://git-scm.com/)

Check your installations:
```powershell
python --version
node --version
git --version
```

---

## 🎯 Common Tasks

### Run the Application
```powershell
.\run.ps1
```

### Train a New Model
```powershell
cd backend
python train_model.py
```

### View API Documentation
Open: `http://localhost:8000/docs`

### Build for Production
```powershell
# Frontend
cd frontend
npm run build

# Backend
cd backend
pip install gunicorn
gunicorn main:app
```

---

## 🧪 Test the System

### Sample Prediction

Use these values in the UI:

| Field | Value |
|-------|-------|
| Market ID | 1.0 |
| Store Category | american |
| Order Protocol | 1.0 |
| Total Items | 2 |
| Subtotal | 1500 |
| Distinct Items | 2 |
| Min Item Price | 500 |
| Max Item Price | 1000 |
| Outstanding Orders | 10 |
| Estimated Driving Duration | 400 |

**Expected Result**: ~38 minutes

---

## 🐛 Troubleshooting

### Backend won't start
```powershell
# Reinstall dependencies
pip install -r backend/requirements.txt --force-reinstall
```

### Frontend won't start
```powershell
# Clear cache and reinstall
cd frontend
npm cache clean --force
rm -rf node_modules
npm install
```

### Port already in use
```powershell
# Backend: Use different port
uvicorn main:app --reload --port 8001

# Frontend: Vite will auto-select next port
```

---

## 📞 Get Help

- 📖 **Documentation**: See [README.md](README.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/Ratnesh-181998/PORTER_NN/issues)
- 💬 **Contact**: ratnesh.kumar@example.com

---

## 🎯 Next Steps

1. ✅ Run the application
2. ✅ Make a test prediction
3. ✅ Explore the case study graphs
4. ✅ Read the full [README.md](README.md)
5. ✅ Upload to GitHub (see [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md))

---

## 🌟 Features to Explore

- **Prediction Form**: 5-column compact layout
- **Case Study Gallery**: 42 visualizations from research
- **API Documentation**: Interactive Swagger UI
- **Model Training**: Customize and retrain

---

## 📊 Project Highlights

- ✅ **175,777** training samples
- ✅ **4.16 min** Mean Absolute Error
- ✅ **14** engineered features
- ✅ **42** case study visualizations
- ✅ **100%** production ready

---

## 🎓 Learning Path

### Beginner
1. Run the application
2. Make predictions
3. Explore the UI

### Intermediate
1. Read the code
2. Understand the model
3. Modify features

### Advanced
1. Retrain the model
2. Add new features
3. Deploy to production

---

## 🚀 Ready to Start?

Choose your path:

### 🏃 I want to run it NOW!
```powershell
.\setup.ps1
.\run.ps1
```

### 📖 I want to understand it first
Read: [README.md](README.md)

### 👨‍💻 I want to contribute
Read: [CONTRIBUTING.md](CONTRIBUTING.md)

### 📤 I want to upload to GitHub
Read: [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)

---

## 💡 Pro Tips

- 💾 **Save your work**: Commit changes regularly
- 🧪 **Test thoroughly**: Use the sample data
- 📝 **Document changes**: Update README if needed
- 🌟 **Star the repo**: Show your support!

---

## 🎉 Success Checklist

After setup, you should have:

- [ ] Backend running at `http://localhost:8000`
- [ ] Frontend running at `http://localhost:5173`
- [ ] API docs at `http://localhost:8000/docs`
- [ ] Successful test prediction
- [ ] Case study graphs loading

---

<div align="center">

**🚀 Let's Get Started!**

Run `.\setup.ps1` to begin your journey

---

Made with ❤️ by [Ratnesh Kumar](https://github.com/Ratnesh-181998)

⭐ Star this repo if you find it helpful!

</div>
