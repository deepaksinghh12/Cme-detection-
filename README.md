# CME Detection & Space Weather Monitoring System

> **Made for Team Digi Shakti - Smart India Hackathon (SIH)**

A comprehensive real-time space weather monitoring and Coronal Mass Ejection (CME) detection system with predictive analytics. This system provides real-time monitoring, detection, and forecasting of space weather events including CMEs, geomagnetic storms, and solar activity.

## 🌟 Features

### Real-Time Monitoring
*   **Live Space Weather Data**: Real-time monitoring of 15+ space weather parameters
*   **CME Detection**: Automated detection of Coronal Mass Ejections using machine learning
*   **Geomagnetic Storm Tracking**: Live geomagnetic indices (Kp, DST, Ap, F10.7)
*   **Solar Activity Monitoring**: Solar flares, sunspot numbers, and solar wind parameters

### Predictive Analytics
*   **7-Day Forecast**: Multi-parameter space weather forecasting using LSTM models
*   **CME Arrival Prediction**: Time and direction prediction for CME events
*   **Geomagnetic Storm Prediction**: Storm intensity and timeline forecasting
*   **Composite Index**: Unified space weather index using Principal Component Analysis (PCA)

### Advanced Features
*   **Satellite Field Data Prediction**: Match satellite coordinates with NOAA wind data for CME probability assessment
*   **3D Visualizations**: Interactive 3D animations for space weather parameters
*   **Data Import/Export**: Support for CDF file uploads and CSV exports
*   **Historical Analysis**: View and analyze past CME events and space weather data

---

## 🛠️ Tech Stack

### Backend
*   **FastAPI**: High-performance Python web framework
*   **Machine Learning**: scikit-learn, scipy for CME detection algorithms
*   **Data Processing**: pandas, numpy for data manipulation
*   **Database**: PostgreSQL with SQLAlchemy ORM
*   **Real-time Data**: Integration with NOAA Space Weather Prediction Center APIs

### Frontend
*   **React 18**: Modern UI framework with TypeScript
*   **Vite**: Fast build tool and dev server
*   **Framer Motion**: Smooth animations and transitions
*   **Three.js**: 3D visualizations and space weather animations
*   **Recharts**: Real-time data visualization
*   **Shadcn UI**: Beautiful, accessible component library
*   **Tailwind CSS**: Utility-first CSS framework

---

## 📋 Prerequisites
*   Python 3.11+
*   Node.js 18+ and npm
*   PostgreSQL (optional, for database features)
*   Git

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/deepaksinghh12/Cme-detection-.git
cd Cme_detection_Phased2
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install
```

---

## 🏃 Running the Application

### Start Backend Server
```bash
cd backend
python main.py
```
> Backend will run on http://localhost:8002

### Start Frontend Server
```bash
cd frontend
npm run dev
```
> Frontend will run on http://localhost:8080

---

## 📖 Usage

### Main Dashboard
Access the main dashboard at `http://localhost:8080` for an overview of:
*   Real-time space weather metrics
*   Recent CME events
*   System status and health monitoring
*   Quick access to all features

### Phase-Based Navigation
The application is organized into phases:

*   **Phase 1 (/phase1): Live Space Weather Data**
    *   Real-time monitoring of 15+ parameters
    *   4-grid layout with graphs, animations, and safety analysis
    *   Auto-refresh every 60 seconds

*   **Phase 2 (/phase2): CME Prediction**
    *   Arrival time prediction
    *   Direction forecasting
    *   Forecast visualizations

*   **Phase 3 (/phase3): Live Geomagnetic Storm**
    *   Real-time geomagnetic monitoring
    *   Storm intensity tracking
    *   Current storm effects

*   **Phase 4 (/phase4): Geomagnetic Storm Prediction**
    *   Time regression models
    *   Storm intensity prediction
    *   Future timeline visualization

*   **Phase 5 (/phase5): Video & Image Animation**
    *   Combined CME + Storm animations
    *   Video generation
    *   Image export capabilities

*   **Field Data Prediction (/phase): Satellite CME Probability**
    *   Select satellite by NORAD ID
    *   Match coordinates with NOAA wind data
    *   Calculate CME occurrence probability

### Recent CME Events
View all recent CME events at `/recent-cme-events` with detailed analysis and detection results.

---

## 🔌 API Endpoints

### Data Endpoints
*   `GET /api/data/summary` - Get data summary and system status
*   `GET /api/data/realtime` - Get real-time solar wind data
*   `GET /api/data/particle` - Get particle data
*   `POST /api/data/upload` - Upload CDF file for analysis

### CME Detection
*   `GET /api/cme/recent` - Get recent CME events
*   `POST /api/ml/analyze-cdf` - Analyze CDF file for CME detection

### Geomagnetic Data
*   `GET /api/geomagnetic/storm/live` - Get live geomagnetic indices
*   `GET /api/forecast/predictions` - Get 7-day forecast predictions

### Satellite Data
*   `GET /api/satellites` - Get list of satellites
*   `GET /api/satellites/{norad_id}` - Get satellite details
*   `GET /api/satellites/{norad_id}/cme-prediction` - Get CME probability for satellite

### NOAA Integration
*   `GET /api/noaa/alerts` - Get space weather alerts
*   `GET /api/noaa/solar-flares` - Get solar flare data
*   `GET /api/noaa/images/{source}` - Get image sequences

---

## 📁 Project Structure
```
Cme_detection_Phased2/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── noaa_realtime_data.py   # NOAA data fetcher
│   ├── database.py             # Database models
│   ├── scripts/                # ML models and scripts
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── pages/              # Page components
│   │   ├── components/         # Reusable components
│   │   ├── lib/                # Utilities and API client
│   │   └── App.tsx             # Main app component
│   ├── package.json            # Node dependencies
│   └── vite.config.ts          # Vite configuration
│
└── README.md                   # This file
```

---

## 🎯 Key Features Explained

### CME Detection Algorithm
The system uses a multi-parameter approach to detect CME events:
*   **Velocity Threshold**: Detects high-speed solar wind streams (>600 km/s)
*   **Density Spikes**: Identifies sudden density increases
*   **Temperature Anomalies**: Monitors proton temperature variations
*   **Bz Component Analysis**: Tracks southward magnetic field (Bz < -10 nT)
*   **Composite Scoring**: Weighted combination of all parameters

### Forecast Model
*   **Training Data**: 29 years of historical space weather data
*   **Model Type**: LSTM (Long Short-Term Memory) neural network
*   **Parameters**: DST, Kp, Ap, Sunspot Number
*   **Accuracy**: 97.3% overall accuracy
*   **Forecast Period**: 7 days ahead

### Composite Index
A unified space weather index combining:
*   DST Index (Disturbance Storm Time)
*   Kp Index (Planetary K-index)
*   Ap Index (Daily geomagnetic activity)
*   Sunspot Number
Uses **Principal Component Analysis (PCA)** for optimal parameter combination.

---

## 🔧 Configuration

### Backend Configuration
Edit `backend/config.yaml` for:
*   Database connection settings
*   NOAA API endpoints
*   Model parameters
*   Detection thresholds

### Frontend Configuration
Edit `frontend/src/lib/api.ts` to configure:
*   API base URL
*   Request timeouts
*   Retry policies

---

## 🐛 Troubleshooting

*   **Backend Issues**:
    *   *Port 8002 already in use*: Change port in `main.py` or kill the process.
    *   *Database connection errors*: Ensure PostgreSQL is running (if using database).
    *   *Missing dependencies*: Run `pip install -r requirements.txt`.

*   **Frontend Issues**:
    *   *Port 8080 already in use*: Vite will automatically use next available port.
    *   *Module not found*: Run `npm install` to install dependencies.
    *   *Build errors*: Check Node.js version (requires 18+).

---

## 📊 Data Sources
*   **NOAA Space Weather Prediction Center**: Real-time solar wind and geomagnetic data
*   **NASA OMNIWeb**: Historical space weather datasets
*   **Aditya L1**: Solar observation data (when available)
*   **External Satellite API**: Satellite position and telemetry data

---

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1.  Fork the repository
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License
This project is developed for **Smart India Hackathon (SIH)** presentation.

---

## 👥 Development Team
**Made for Team Digi Shakti - Smart India Hackathon (SIH)**

End to end developed and produced by **Deepak Singh** as **Tech System Lead & Full Stack Architect**

### 🙏 Special Thanks to Team Members:
*   Akshat Sharma
*   Mayank Saini
*   Lakshay
*   Garima
*   Lily
*   Dhruv Saini

*This project represents a complete full-stack solution for space weather monitoring and CME detection, developed from concept to deployment for the Smart India Hackathon 2024.*

## 🙏 Acknowledgments
*   NOAA Space Weather Prediction Center for real-time data
*   NASA for historical space weather datasets
*   Aditya L1 mission for solar observation data

> **Note**: This system is designed for educational and research purposes. For operational space weather forecasting, please refer to official space weather agencies.
