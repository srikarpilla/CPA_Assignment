# CPA Canada Website Redesign — Full Setup Guide
## Cohere API Backend + Frontend Integration

---

## 📋 **What You Have**

✅ **Frontend** (`index.html`) — Responsive prototype with audience picker, search, and chat widget  
✅ **Backend** (`server.js`) — Express server that securely calls Cohere API  
✅ **Dependencies** (`package.json`) — npm packages needed  
✅ **Environment Config** (`.env`) — API key storage  

---

## 🚀 **Quick Start — Local Testing (5 minutes)**

### **Step 1: Get a Cohere API Key**

1. Go to **cohere.com** → Sign up (free tier included)
2. Navigate to **API keys** in your account dashboard
3. Copy your API key (looks like: `sk-xxxxxxxxxxxxxxxx`)

### **Step 2: Set Up Your Folder**

```bash
# Create a new folder
mkdir cpa-redesign
cd cpa-redesign

# Copy these files into the folder:
# - server.js
# - package.json
# - .env
# - index.html
```

### **Step 3: Install Dependencies**

```bash
npm install
```

This installs:
- `express` — backend framework
- `cors` — allows browser to talk to backend
- `dotenv` — loads environment variables

### **Step 4: Add Your Cohere API Key**

Open `.env` file and replace:
```
COHERE_API_KEY=your_cohere_api_key_here
```

With your actual key:
```
COHERE_API_KEY=sk-abcd1234efgh5678ijkl9012
```

**Important:** Save the file. `.env` is never committed to GitHub (it's in `.gitignore`).

### **Step 5: Start the Server**

```bash
npm start
```

You should see:
```
✓ Chat server running on http://localhost:3000
✓ Chat endpoint: POST http://localhost:3000/api/chat
✓ Health check: GET http://localhost:3000/health
```

### **Step 6: Test It**

**In a new terminal:**

```bash
# Test the health check
curl http://localhost:3000/health

# You should see:
# {"status":"ok"}
```

**In your browser:**
```
Open: file:///path/to/your/index.html
```

- Click the 💬 chat bubble (bottom-right)
- Type: "What is a CPA?"
- **It should respond** using Cohere API through your backend ✓

---

## 🔧 **Testing the Chat Widget (Step-by-Step)**

### **Local Browser Test:**

1. Keep `npm start` running in terminal
2. Open `index.html` in your browser (or serve it with `npx http-server .`)
3. Click the **💬** button (bottom-right corner)
4. Type a question, e.g.:
   - "How do I become a CPA?"
   - "What is the CFE exam?"
   - "How much does membership cost?"
5. Click **Send** or press Enter
6. **Wait 2-3 seconds** — Cohere API processes the request
7. Response appears in the chat

### **Test Different Audiences:**

1. Click the **audience buttons** (Public / Student / Member / Firm)
2. Notice the hero section, rail cards, and rail title change ✓
3. Try searching in the search bar (top)

---

## 📦 **Deploy to Render (Free, 10 minutes)**

Render.com hosts your backend for free (with sleep limits on free tier).

### **Step 1: Push to GitHub**

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: CPA redesign with Cohere backend"

# Create repo on github.com, then:
git remote add origin https://github.com/YOUR-USERNAME/cpa-redesign.git
git branch -M main
git push -u origin main
```

**Important:** Make sure `.gitignore` includes `.env` so your API key is NOT pushed:

```bash
echo ".env" >> .gitignore
```

### **Step 2: Create Render Web Service**

1. Go to **render.com** → Sign up with GitHub
2. Click **New** → **Web Service**
3. Connect your GitHub repo (`cpa-redesign`)
4. Fill in:
   - **Name:** `cpa-chat-backend`
   - **Runtime:** `Node`
   - **Build command:** `npm install`
   - **Start command:** `node server.js`
5. Under **Environment**, add:
   - **Key:** `COHERE_API_KEY`
   - **Value:** (paste your Cohere API key)
   - Click **Add**
6. Click **Create Web Service**

Render deploys automatically. Wait ~2 min for the URL, e.g.:
```
https://cpa-chat-backend.onrender.com
```

### **Step 3: Test the Deployed Backend**

```bash
curl https://cpa-chat-backend.onrender.com/health

# Should return:
# {"status":"ok"}
```

### **Step 4: Update Frontend to Use Deployed Backend**

In `index.html`, find this line (around line 550):

```javascript
const BACKEND_URL = 'http://localhost:3000'; // Local development
```

Change to:

```javascript
const BACKEND_URL = 'https://cpa-chat-backend.onrender.com'; // Production
```

Save and commit:

```bash
git add index.html
git commit -m "Update backend URL to production"
git push
```

### **Step 5: Host Frontend on GitHub Pages**

1. Push `index.html` to your GitHub repo (if not already)
2. Go to repo **Settings** → **Pages**
3. Under "Source," select **main** branch
4. GitHub automatically serves at: `https://YOUR-USERNAME.github.io/cpa-redesign`

Now test the **live prototype:**
```
https://your-username.github.io/cpa-redesign
```

Click the chat widget — it should call your Render backend! ✓

---

## 🛠️ **Troubleshooting**

### **Chat widget shows "Connection error"**

**Problem:** Backend URL is wrong or server isn't running.

**Fix:**
1. Check `BACKEND_URL` in `index.html` matches your deployed URL
2. Verify backend is running: `curl https://your-backend.onrender.com/health`
3. If Render backend is sleeping (free tier), wait 10 sec and try again

### **"COHERE_API_KEY is undefined"**

**Problem:** `.env` file not loaded or API key is wrong.

**Fix:**
1. Verify `.env` exists in your server folder
2. Restart the server: `npm start`
3. Check Cohere key is pasted correctly (no spaces before/after)

### **CORS error in browser console**

**Problem:** Browser blocked the request to backend.

**Fix:**
- This shouldn't happen (CORS is configured in `server.js`)
- If it does, verify backend is running and URL is correct

### **Chat response is slow (5+ seconds)**

**Problem:** Cohere API is processing or network is slow.

**Fix:**
- First response is usually slower
- Cohere free tier has rate limits — wait a few seconds between messages
- Use a paid Cohere plan for faster responses

---

## 📁 **File Structure**

```
cpa-redesign/
├── index.html           (frontend prototype)
├── server.js            (backend server)
├── package.json         (dependencies)
├── .env                 (API keys — NOT COMMITTED)
├── .gitignore           (ignores .env)
└── README.md            (this file)
```

---

## 🔑 **Environment Variables**

The backend reads from `.env`:

```
COHERE_API_KEY=sk-your-key-here
PORT=3000
```

**On Render.com:**
- Set `COHERE_API_KEY` in the **Environment** section of your service
- `PORT` is automatic (Render sets it)

---

## 📊 **API Endpoints**

### **Health Check**
```
GET /health
Response: { "status": "ok" }
```

### **Chat**
```
POST /api/chat

Request body:
{
  "message": "What is a CPA?",
  "chat_history": [
    { "role": "user", "content": "Hello" },
    { "role": "assistant", "content": "Hi there!" }
  ],
  "system": "You are a helpful assistant..."
}

Response:
{
  "text": "A CPA is a Certified Public Accountant...",
  "finish_reason": "end_turn"
}
```

---

## 🎯 **Submission Checklist**

Before submitting to InternShala:

- [ ] Backend deployed on Render (or similar)
- [ ] Frontend updated with production backend URL
- [ ] Chat widget tested and working
- [ ] GitHub repo public with code
- [ ] Live prototype link in submission (GitHub Pages URL)
- [ ] API key NOT in GitHub (use `.env` + Render environment variables)

**Submit:**
```
Live prototype: https://your-username.github.io/cpa-redesign
Backend: https://cpa-chat-backend.onrender.com
GitHub repo: https://github.com/your-username/cpa-redesign
```

---

## 💡 **What Happens in the Chat**

1. **User types** a question in the chat widget
2. **Frontend sends** message + chat history to backend
3. **Backend receives** request at `/api/chat`
4. **Server calls** Cohere API with your API key
5. **Cohere responds** with an answer
6. **Backend sends** the response back to frontend
7. **Chat displays** the answer in real-time ✓

**Your API key is NEVER exposed** — it stays on the server.

---

## 🚨 **Important Notes**

- **Free Cohere tier:** 100 API calls/month. Upgrade if you exceed.
- **Free Render tier:** Free dyno sleeps after 15 min inactivity. May take 10 sec to wake up on first call.
- **GitHub Pages:** Hosts your HTML/CSS/JS for free, forever.
- **API key in .env:** Never commit `.env` to GitHub. Always use environment variables on servers.

---

## 📞 **Quick Command Reference**

```bash
# Local development
npm install              # Install dependencies
npm start                # Start backend on localhost:3000

# Testing
curl http://localhost:3000/health     # Health check
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello","chat_history":[],"system":"You are helpful"}'

# GitHub
git init                 # First time only
git add .
git commit -m "message"
git push                 # Push to GitHub

# Render deployment
# Done via web interface at render.com
```

---

## ✅ **You're Done!**

Once deployed, you have:
- ✓ Live prototype on GitHub Pages
- ✓ Secure backend on Render
- ✓ Working Cohere chat widget
- ✓ No API key exposed
- ✓ Everything tested and ready to submit

Good luck with the assignment! 🚀
