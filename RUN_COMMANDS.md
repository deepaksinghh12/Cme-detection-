# Commands to Run Phased Project

## Quick Start Commands

### Option 1: Run Both (Two Separate Terminals)

**Terminal 1 - Backend:**
```bash
cd D:\sih\Cme_detection_Phased\backend
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd D:\sih\Cme_detection_Phased\frontend
npm run dev
```

---

### Option 2: PowerShell Script (Run Both Together)

Create a file `start.ps1` in the project root and run:
```powershell
cd D:\sih\Cme_detection_Phased
.\start.ps1
```

---

## Detailed Steps

### Step 1: Start Backend Server

Open **Terminal 1** (PowerShell or Command Prompt):

```powershell
cd D:\sih\Cme_detection_Phased\backend
python main.py
```

**Expected Output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8002
```

✅ Backend will run on: `http://localhost:8002`

---

### Step 2: Start Frontend Server

Open **Terminal 2** (PowerShell or Command Prompt):

```powershell
cd D:\sih\Cme_detection_Phased\frontend
npm run dev
```

**Expected Output:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

✅ Frontend will run on: `http://localhost:5173`

---

## Access Phases

Once both servers are running:

1. **Open Browser:** `http://localhost:5173/phase1`
2. **Navigate through phases:**
   - Phase 1: `http://localhost:5173/phase1`
   - Phase 2: `http://localhost:5173/phase2`
   - Phase 3: `http://localhost:5173/phase3`
   - Phase 4: `http://localhost:5173/phase4`
   - Phase 5: `http://localhost:5173/phase5`

---

## Troubleshooting

### Backend Issues:

**If Python not found:**
```powershell
# Check Python version
python --version

# Or try
python3 --version
```

**If port 8002 is busy:**
- Change port in `backend/main.py` (last line)
- Or kill process using port 8002

**If dependencies missing:**
```powershell
cd D:\sih\Cme_detection_Phased\backend
pip install -r requirements.txt
```

---

### Frontend Issues:

**If npm not found:**
```powershell
# Check Node.js
node --version
npm --version
```

**If dependencies missing:**
```powershell
cd D:\sih\Cme_detection_Phased\frontend
npm install
```

**If port 5173 is busy:**
- Vite will automatically use next available port
- Check terminal output for actual port

---

## Quick Commands Summary

```powershell
# Backend (Terminal 1)
cd D:\sih\Cme_detection_Phased\backend
python main.py

# Frontend (Terminal 2)
cd D:\sih\Cme_detection_Phased\frontend
npm run dev
```

---

## Stop Servers

- **Backend:** Press `Ctrl + C` in Terminal 1
- **Frontend:** Press `Ctrl + C` in Terminal 2


