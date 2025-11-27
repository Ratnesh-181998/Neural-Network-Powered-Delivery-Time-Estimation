# 🚀 Quick Start Guide - Porter NN

Get the Porter Neural Network Delivery Time Prediction system up and running in 5 minutes!

---

## ⚡ Fast Track Setup

### 1️⃣ Clone & Navigate
```powershell
git clone https://github.com/Ratnesh-181998/PORTER_NN.git
cd PORTER_NN
```

### 2️⃣ Backend Setup (2 minutes)
```powershell
# Install Python dependencies
pip install -r backend/requirements.txt

# Start the API server
cd backend
uvicorn main:app --reload --port 8000
```

✅ Backend running at: `http://localhost:8000`

### 3️⃣ Frontend Setup (2 minutes)
Open a **new terminal**:
```powershell
# Install Node dependencies
cd frontend
npm install

# Start the development server
npm run dev
```

✅ Frontend running at: `http://localhost:5173`

### 4️⃣ Test It Out!
1. Open browser: `http://localhost:5173`
2. Fill in the prediction form
3. Click "Predict Delivery Time"
4. See instant results! 🎉

---

## 📊 Sample Prediction

Try these values for a quick test:

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
| Created At | 2024-11-27T20:00:00Z |

**Expected Result**: ~38 minutes

---

## 🔍 Verify Installation

### Check Backend
```powershell
# Test health endpoint
curl http://localhost:8000
```

Expected response:
```json
{"message": "Porter Delivery Prediction API is running"}
```

### Check Frontend
Visit: `http://localhost:5173`

You should see the Porter NN prediction interface.

---

## 🎨 Explore Features

### 1. Make Predictions
- Fill out the form with order details
- Click "Predict Delivery Time"
- View estimated delivery time in minutes

### 2. View Case Study
- Click "View Case Study Graphs"
- Browse 42 visualizations from research
- Each graph includes context and source

### 3. API Documentation
Visit: `http://localhost:8000/docs`
- Interactive Swagger UI
- Test endpoints directly
- View request/response schemas

---

## 🛠️ Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError`
```powershell
# Solution: Reinstall dependencies
pip install -r backend/requirements.txt
```

**Problem**: Port 8000 already in use
```powershell
# Solution: Use different port
uvicorn main:app --reload --port 8001
```

### Frontend Issues

**Problem**: `npm install` fails
```powershell
# Solution: Clear cache and retry
npm cache clean --force
npm install
```

**Problem**: Port 5173 already in use
```powershell
# Solution: Vite will auto-select next available port
# Or specify manually in vite.config.js
```

---

## 📚 Next Steps

1. **Read Full Documentation**: See [README.md](README.md)
2. **Train Custom Model**: Run `python backend/train_model.py`
3. **Customize UI**: Edit `frontend/src/App.jsx`
4. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 💡 Tips

- **Virtual Environment**: Use `python -m venv .venv` for isolated dependencies
- **Hot Reload**: Both backend and frontend support hot reload
- **API Testing**: Use the Swagger UI at `/docs` for easy testing
- **Model Retraining**: Modify `train_model.py` to experiment with architectures

---

## 🆘 Need Help?

- 📖 **Full README**: [README.md](README.md)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/Ratnesh-181998/PORTER_NN/issues)
- 💬 **Contact**: ratnesh.kumar@example.com

---

**Happy Predicting! 🚚💨**
