<div align="center">

# 🚚 Neural Network-Powered Delivery Time Estimation

### *AI-Driven Logistics Intelligence for Porter's Intra-City Platform*

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Production-Ready Deep Learning System | 4.16 Min MAE | 175K+ Training Samples**

[🚀 Quick Start](#-quick-start) • [📊 Live Demo](#-usage) • [📖 Documentation](#-table-of-contents) • [🤝 Contribute](#-contributing)

<img width="2433" height="1148" alt="image" src="https://github.com/user-attachments/assets/72d64e91-7dbb-4392-86a0-56a966d4c10f" />

---

### 🏆 **Project Highlights**

| Metric | Achievement |
|--------|-------------|
| **Accuracy** | 4.16 minutes MAE |
| **Dataset Size** | 175,777 real deliveries |
| **Features** | 14 engineered features |
| **Model Type** | Deep Neural Network |
| **Response Time** | <100ms per prediction |
| **Status** | Production Ready ✅ |

</div>

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [💻 Installation](#-installation)
- [📊 Usage](#-usage)
- [📈 Model Performance](#-model-performance)
- [🔌 API Documentation](#-api-documentation)
- [📸 Screenshots](#-screenshots)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author & Contact](#-author--contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🎯 Overview

**Porter** is India's largest intra-city logistics marketplace, connecting **5+ million customers** with **150,000+ driver-partners** across major cities. Accurate delivery time predictions are crucial for customer satisfaction and operational efficiency.

### 🎓 The Challenge

Traditional rule-based ETA systems struggle with:
- Dynamic traffic patterns
- Varying order complexities
- Market-specific characteristics
- Real-time demand fluctuations

### 💡 Our Solution

A **Deep Learning Neural Network** that learns from **175,777 real-world deliveries** to predict accurate delivery times by analyzing:

- 📍 **Market Dynamics** - Location-specific patterns
- 🛒 **Order Characteristics** - Items, prices, complexity
- 🚗 **Logistics Factors** - Distance, traffic, driver availability
- ⏰ **Temporal Patterns** - Time of day, day of week

### 🎯 Business Impact

| Impact Area | Benefit |
|-------------|---------|
| **Customer Satisfaction** | Accurate ETAs improve trust and experience |
| **Operational Efficiency** | Better driver allocation and route planning |
| **Cost Reduction** | Optimized resource utilization |
| **Data-Driven Decisions** | Insights from 175K+ delivery patterns |
| **Scalability** | Ready for production deployment at scale |

### 🔬 Technical Achievement

- ✅ **Mean Absolute Error**: 4.16 minutes (industry-leading accuracy)
- ✅ **R² Score**: ~0.85 (85% variance explained)
- ✅ **Inference Speed**: <100ms per prediction
- ✅ **Model Size**: 305KB (lightweight and efficient)

---

## ✨ Features

### 🧠 Machine Learning
- **Deep Neural Network** with multiple hidden layers and dropout regularization
- **Feature Engineering**: Time-based features (hour, day of week), order characteristics
- **Robust Preprocessing**: Handles missing data, outliers, and categorical encoding
- **Model Artifacts**: Saved model and preprocessor for instant predictions

### 🖥️ Full-Stack Application
- **React Frontend**: Modern, responsive UI with real-time predictions
- **FastAPI Backend**: High-performance REST API serving the ML model
- **Interactive Dashboard**: 5-column compact layout for easy data entry
- **Case Study Gallery**: 42 visualizations from research PDFs with context

### 📊 Data Visualization
- **Automated Graph Extraction**: Extracts all charts from PDF documentation
- **Contextual Information**: Each graph paired with source and description
- **High-Resolution Rendering**: 2x zoom for clarity

---

## 🛠️ Tech Stack

### Backend
- **Python 3.11**
- **TensorFlow/Keras** - Deep Learning framework
- **FastAPI** - Modern web framework for APIs
- **Scikit-learn** - Preprocessing and metrics
- **Pandas/NumPy** - Data manipulation
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **Axios** - HTTP client
- **CSS3** - Custom styling with glassmorphism effects

### Machine Learning
- **Architecture**: Sequential Neural Network
  - Input Layer: Dynamic based on features
  - Hidden Layers: 128 → 64 → 32 neurons (ReLU activation)
  - Dropout: 0.2 and 0.1 for regularization
  - Output: 1 neuron (Linear activation for regression)
- **Optimizer**: Adam
- **Loss Function**: Mean Squared Error (MSE)
- **Metrics**: MAE, RMSE, R²

---

## 📁 Project Structure

```
PORTER_NN/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── train_model.py          # Model training script
│   ├── model.keras             # Trained neural network
│   ├── preprocessor.joblib     # Fitted preprocessor
│   └── requirements.txt        # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main React component
│   │   ├── App.css            # Styling
│   │   └── graphs.json        # Graph metadata
│   ├── public/
│   │   └── graphs/            # Extracted PDF visualizations
│   └── package.json           # Node dependencies
├── Doc File/                   # Original PDF documentation
├── data_2.csv                  # Training dataset (175K rows)
├── extract_graphs.py           # PDF graph extraction utility
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                 # Git ignore rules
```

---

## 🚀 Quick Start

Get up and running in **5 minutes**!

### ⚡ Automated Setup (Recommended)

```powershell
# Clone the repository
git clone https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation.git
cd Neural-Network-Powered-Delivery-Time-Estimation

# Run automated setup
.\setup.ps1

# Start the application
.\run.ps1
```

The browser will automatically open at `http://localhost:5173` 🎉

### 🎯 Manual Setup

**Terminal 1 - Backend:**
```bash
pip install -r backend/requirements.txt
cd backend
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Access the application:**
- 🌐 Frontend: `http://localhost:5173`
- 📡 API: `http://localhost:8000`
- 📚 API Docs: `http://localhost:8000/docs`

---

## 💻 Installation

### Prerequisites
- **Python 3.8+**
- **Node.js 16+** and npm
- **Git**

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/PORTER_NN.git
cd PORTER_NN
```

### Step 2: Backend Setup
```bash
# Install Python dependencies
pip install -r backend/requirements.txt

# Train the model (optional - pre-trained model included)
cd backend
python train_model.py
```

### Step 3: Frontend Setup
```bash
cd frontend
npm install
```

---

## 💻 Usage

### Running the Application

#### 1. Start the Backend API
```bash
cd backend
uvicorn main:app --reload --port 8000
```
The API will be available at `http://localhost:8000`

#### 2. Start the Frontend
```bash
cd frontend
npm run dev
```
The UI will be available at `http://localhost:5173`

### Making Predictions

1. **Open the web app** at `http://localhost:5173`
2. **Fill in the order details**:
   - Market ID
   - Store Category (dropdown)
   - Order Protocol
   - Total Items & Prices
   - Outstanding Orders
   - Estimated Driving Duration
3. **Click "Predict Delivery Time"**
4. **View the estimated delivery time** in minutes

### Viewing Case Study Analysis
- Click **"View Case Study Graphs"** to see 42 pages of analysis
- Each graph includes source PDF, page number, and context

---

## 📈 Model Performance

### Metrics (Test Set)
| Metric | Value |
|--------|-------|
| **MAE** | 4.16 minutes |
| **RMSE** | ~4.7 minutes |
| **R² Score** | ~0.85 |

### Training Details
- **Dataset**: 175,777 delivery records
- **Features**: 14 (after preprocessing)
- **Train/Test Split**: 80/20
- **Epochs**: 20 (with early stopping)
- **Batch Size**: 128
- **Validation Split**: 20% of training data

### Key Features
1. Market ID
2. Store Category (One-Hot Encoded)
3. Order Protocol
4. Total Items & Distinct Items
5. Subtotal, Min/Max Item Price
6. Outstanding Orders
7. Estimated Driving Duration
8. Order Hour & Day of Week

---

## 🔌 API Documentation

### Endpoints

#### `GET /`
Health check endpoint
```json
{
  "message": "Porter Delivery Prediction API is running"
}
```

#### `POST /predict`
Predict delivery time for an order

**Request Body:**
```json
{
  "market_id": 1.0,
  "store_primary_category": "american",
  "order_protocol": 1.0,
  "total_items": 2,
  "subtotal": 1500,
  "num_distinct_items": 2,
  "min_item_price": 500,
  "max_item_price": 1000,
  "total_outstanding_orders": 10,
  "estimated_store_to_consumer_driving_duration": 400,
  "created_at": "2024-11-27T20:00:00Z"
}
```

**Response:**
```json
{
  "predicted_delivery_time_minutes": 38.2,
  "input_summary": { ... }
}
```

### Interactive API Docs
Visit `http://localhost:8000/docs` for Swagger UI documentation

---

## 📸 Screenshots

### Prediction Interface
![Prediction Form](screenshots/prediction_form.png)

### Case Study Gallery
![Graph Gallery](screenshots/graph_gallery.png)

### API Response
![API Docs](screenshots/api_docs.png)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author & Contact

<div align="center">

### **Ratnesh Kumar**
*Full-Stack Data Scientist | AI/ML Engineer | GeN AI | Agentic AI | AI Enthusiast | Data Science Professional*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratnesh-kumar-3a4671191/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ratneshkumar181998@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://github.com/Ratnesh-181998)

</div>

### 📬 Get in Touch

I'm always open to discussing:
- 💼 **Job Opportunities** - Full-time roles in ML/AI
- 🤝 **Collaborations** - Open source projects and research
- 💡 **Ideas** - Innovative AI/ML applications
- 🎓 **Mentorship** - Helping others learn ML/AI

### 📧 Contact Information

| Platform | Link |
|----------|------|
| 📧 **Email** | [rattudacsit2021gate@gmail.com](mailto:rattudacsit2021gate@gmail.com) |
| 💼 **LinkedIn** | [https://www.linkedin.com/in/ratneshkumar1998/](https://www.linkedin.com/in/ratneshkumar1998/) |
| 🐙 **GitHub** | [@Ratnesh-181998](https://github.com/Ratnesh-181998) |
| 🌐 **Portfolio** | [GitHub Profile](https://github.com/Ratnesh-181998) |

### 🔗 Project Links

- **📦 Repository**: [Neural-Network-Powered-Delivery-Time-Estimation](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation)
- **🐛 Report Issues**: [Issue Tracker](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/discussions)
- **📖 Documentation**: [Wiki](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/wiki)

### 🌟 Support This Project

If you find this project helpful, please consider:

- ⭐ **Starring** the repository
- 🍴 **Forking** for your own projects
- 📢 **Sharing** with your network
- 🐛 **Reporting** bugs or issues
- 💡 **Suggesting** new features
- 🤝 **Contributing** code improvements

<div align="center">

**💬 Let's Connect and Build Amazing Things Together!**

</div>

---

## 🙏 Acknowledgments

- **Porter** for the business case and dataset
- **TensorFlow** team for the deep learning framework
- **FastAPI** for the excellent web framework
- **React** community for frontend tools

---

## 🔮 Future Enhancements

### 🎯 Roadmap

#### Phase 1: Enhanced Intelligence (Q1 2025)
- [ ] **Real-time Traffic Integration** - Live traffic data from Google Maps API
- [ ] **Weather Impact Analysis** - Weather conditions affecting delivery times
- [ ] **Multi-model Ensemble** - Combine multiple models for better accuracy
- [ ] **Confidence Intervals** - Provide prediction uncertainty ranges

#### Phase 2: Production Hardening (Q2 2025)
- [ ] **Docker Containerization** - Easy deployment with Docker
- [ ] **CI/CD Pipeline** - Automated testing and deployment
- [ ] **Model Monitoring** - Track model performance in production
- [ ] **A/B Testing Framework** - Test model improvements

#### Phase 3: Advanced Features (Q3 2025)
- [ ] **Mobile Application** - React Native mobile app
- [ ] **Automated Retraining** - Continuous learning from new data
- [ ] **Feature Store** - Centralized feature management
- [ ] **Explainable AI** - SHAP/LIME for prediction explanations

#### Phase 4: Scale & Optimize (Q4 2025)
- [ ] **Microservices Architecture** - Scalable service design
- [ ] **Kubernetes Deployment** - Container orchestration
- [ ] **Global CDN** - Fast content delivery worldwide
- [ ] **Multi-region Support** - Deploy across multiple regions

---

<div align="center">

## 🌟 **Star This Repository!**

If this project helped you or you found it interesting, please give it a ⭐!

### **Share Your Feedback**

💬 Have suggestions? Found a bug? Want to contribute?  
[Open an issue](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/issues) or [start a discussion](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/discussions)!

---

### **Built with ❤️ and ☕ by [Ratnesh Kumar](https://github.com/Ratnesh-181998)**

*Empowering logistics with AI, one prediction at a time* 🚚💨

---

[![GitHub stars](https://img.shields.io/github/stars/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation?style=social)](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation?style=social)](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation?style=social)](https://github.com/Ratnesh-181998/Neural-Network-Powered-Delivery-Time-Estimation/watchers)

**© 2024 Ratnesh Kumar. Licensed under MIT.**

</div>


---


<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=24,20,12,6&height=3" width="100%">


## 📜 **License**

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

**Licensed under the MIT License** - Feel free to fork and build upon this innovation! 🚀

---

# 📞 **CONTACT & NETWORKING** 📞


### 💼 Professional Networks

[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RatneshS16497)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![Email](https://img.shields.io/badge/✉️_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rattudacsit2021gate@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@rattudacsit2021gate)
[![Stack Overflow](https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/32068937/ratnesh-kumar)

### 🚀 AI/ML & Data Science
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/RattuDa98)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/rattuda)

### 💻 Competitive Programming
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Ratnesh_1998/)
[![HackerRank](https://img.shields.io/badge/HackerRank-00EA64?style=for-the-badge&logo=hackerrank&logoColor=black)](https://www.hackerrank.com/profile/rattudacsit20211)
[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/ratnesh_181998)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/Ratnesh_181998)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/ratnesh1998)
[![HackerEarth](https://img.shields.io/badge/HackerEarth-323754?style=for-the-badge&logo=hackerearth&logoColor=white)](https://www.hackerearth.com/@ratnesh138/)
[![InterviewBit](https://img.shields.io/badge/InterviewBit-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.interviewbit.com/profile/rattudacsit2021gate_d9a25bc44230/)


---

## 📊 **GitHub Stats & Metrics** 📊



![Profile Views](https://komarev.com/ghpvc/?username=Ratnesh-181998&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS)





<img src="https://github-readme-streak-stats.herokuapp.com/?user=Ratnesh-181998&theme=radical&hide_border=true&background=0D1117&stroke=4ECDC4&ring=F38181&fire=FF6B6B&currStreakLabel=4ECDC4" width="48%" />




<img src="https://github-readme-activity-graph.vercel.app/graph?username=Ratnesh-181998&theme=react-dark&hide_border=true&bg_color=0D1117&color=4ECDC4&line=F38181&point=FF6B6B" width="48%" />

---

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4ECDC4&center=true&vCenter=true&width=600&lines=Ratnesh+Kumar+Singh;Data+Scientist+%7C+AI%2FML+Engineer;4%2B+Years+Building+Production+AI+Systems" alt="Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=F38181&center=true&vCenter=true&width=600&lines=Built+with+passion+for+the+AI+Community+🚀;Innovating+the+Future+of+AI+%26+ML;MLOps+%7C+LLMOps+%7C+AIOps+%7C+GenAI+%7C+AgenticAI+Excellence" alt="Footer Typing SVG" />


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%">

