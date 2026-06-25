# 🐍 **FastAPI Backend Setup Guide**

**FastAPI** is a modern Python web framework. It's faster and easier to deploy than Node.js for Python developers.

---

## ⚡ **Quick Start (Local Testing)**

### **Step 1: Install Python Dependencies**

```bash
# Make sure you're in your cpa-redesign folder
cd cpa-redesign

# Install required packages
pip install -r requirements.txt
```

Or use `pip3` if you're on macOS:
```bash
pip3 install -r requirements.txt
```

### **Step 2: Update `.env` File**

Make sure your `.env` has your Cohere API key:

```env
COHERE_API_KEY=sk-your-actual-key-here
PORT=3000
```

### **Step 3: Run the Server**

```bash
python main.py
```

Or on macOS:
```bash
python3 main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:3000
INFO:     Application startup complete
```

**Success!** ✓

---

## 🧪 **Test the Backend**

In a new terminal:

```bash
# Health check
curl http://localhost:3000/health

# Should return:
# {"status":"ok"}
```

Test the chat:
```bash
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is a CPA?",
    "chat_history": [],
    "system": "You are helpful"
  }'
```

Should return a response from Cohere! ✓

---

## 🌐 **Test with Frontend**

1. Keep `python main.py` running
2. Open `index.html` in your browser
3. Click the 💬 chat button
4. Type a question
5. **Should get response in 2-3 seconds** ✓

---

## 📦 **Deploy to Render (Production)**

### **Step 1: Push to GitHub**

```bash
git init
git add .
git commit -m "CPA redesign with FastAPI backend"
git remote add origin https://github.com/YOUR-USERNAME/cpa-redesign.git
git push -u origin main
```

### **Step 2: Create Render Web Service**

1. Go to **render.com** → Sign up with GitHub
2. Click **New** → **Web Service**
3. Select your `cpa-redesign` repo
4. Fill in:
   - **Name:** `cpa-chat-backend`
   - **Runtime:** `Python 3`
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port 3000`
5. Add Environment Variable:
   - **Key:** `COHERE_API_KEY`
   - **Value:** (your Cohere API key)
6. Click **Create Web Service**

Wait 2-3 minutes for deployment.

You get a URL like:
```
https://cpa-chat-backend.onrender.com
```

### **Step 3: Test Deployed Backend**

```bash
curl https://cpa-chat-backend.onrender.com/health

# Should return:
# {"status":"ok"}
```

### **Step 4: Update Frontend URL**

In `index.html`, change line ~550:

```javascript
const BACKEND_URL = 'https://cpa-chat-backend.onrender.com';
```

Push to GitHub:
```bash
git add index.html
git commit -m "Update to production backend"
git push
```

### **Step 5: Deploy Frontend to GitHub Pages**

1. Go to GitHub repo **Settings** → **Pages**
2. Select **main** branch
3. GitHub creates: `https://your-username.github.io/cpa-redesign`

**Test:** Click chat widget — it works! ✓

---

## 📁 **FastAPI vs Node.js — What Changed**

| Part | Node.js | FastAPI |
|------|---------|---------|
| Server file | `server.js` | `main.py` |
| Dependencies | `package.json` | `requirements.txt` |
| Install | `npm install` | `pip install -r requirements.txt` |
| Start | `npm start` | `python main.py` |
| Port | 3000 | 3000 |
| Render start cmd | `node server.js` | `uvicorn main:app --host 0.0.0.0 --port 3000` |

**Everything else is the same!** Same HTML, same chat widget, same Cohere API.

---

## 🔧 **Troubleshooting**

### **"ModuleNotFoundError: No module named 'fastapi'"**

**Problem:** Dependencies not installed.

**Fix:**
```bash
pip install -r requirements.txt
```

### **"COHERE_API_KEY not found"**

**Problem:** `.env` file missing or API key not set.

**Fix:**
1. Check `.env` exists in your folder
2. Add your key: `COHERE_API_KEY=sk-xxxxx`
3. Save and restart: `python main.py`

### **"Connection refused on localhost:3000"**

**Problem:** Server not running.

**Fix:**
```bash
# Make sure to run:
python main.py
# Then test in another terminal
```

### **"Chat widget timeout"**

**Problem:** Backend not responding or Cohere API slow.

**Fix:**
1. Check server is running: `curl http://localhost:3000/health`
2. Wait 5 seconds (Cohere may be slow)
3. Check Cohere API key is valid

---

## 📊 **API Endpoints**

### **Health Check**
```
GET /health
Response: {"status":"ok"}
```

### **Chat**
```
POST /api/chat

Request:
{
  "message": "What is a CPA?",
  "chat_history": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi!"}
  ],
  "system": "You are helpful"
}

Response:
{
  "text": "A CPA is a Certified Public Accountant...",
  "finish_reason": "end_turn"
}
```

### **Root**
```
GET /
Response: {"message":"CPA Chat Backend API","endpoints":{...}}
```

---

## ✅ **Deployment Checklist**

- [ ] `pip install -r requirements.txt` runs without errors
- [ ] `python main.py` starts server on localhost:3000
- [ ] Health check works: `curl http://localhost:3000/health`
- [ ] Chat works locally with frontend
- [ ] Code pushed to GitHub
- [ ] Render service created and deployed
- [ ] Backend URL updated in `index.html`
- [ ] Frontend deployed to GitHub Pages
- [ ] Live prototype works end-to-end

---

## 🚀 **Your File Structure (FastAPI)**

```
cpa-redesign/
├── main.py              (FastAPI backend)
├── requirements.txt     (Python dependencies)
├── index.html           (frontend)
├── .env                 (API key)
├── .gitignore           (ignore .env)
└── README.md            (docs)
```

---

**FastAPI is ready!** Start with `python main.py` 🐍

For production, Render will run:
```
uvicorn main:app --host 0.0.0.0 --port 3000
```

(You don't need to type this locally — just use `python main.py`)
