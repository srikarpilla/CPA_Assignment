# ⚡ QUICK START (Copy-Paste These Commands)

## Step 1: Get Cohere API Key (2 min)
```
1. Go to: https://cohere.com
2. Sign up (free)
3. Go to API keys: https://dashboard.cohere.com/api-keys
4. Copy your key (looks like: sk-...)
```

## Step 2: Create Folder & Install (1 min)
```bash
mkdir cpa-redesign
cd cpa-redesign

# Create the 5 files (copy from main folder):
# - index.html
# - server.js
# - package.json
# - .env
# - .gitignore

npm install
```

## Step 3: Add Your API Key (30 sec)
Edit `.env` file:
```
COHERE_API_KEY=sk-paste-your-key-here
PORT=3000
```

## Step 4: Run Locally (30 sec)
```bash
npm start
```

You should see:
```
✓ Chat server running on http://localhost:3000
✓ Chat endpoint: POST http://localhost:3000/api/chat
```

## Step 5: Test in Browser (1 min)
```
1. Open: file:///path/to/your/index.html
   (or: npx http-server . → http://localhost:8080)

2. Click the 💬 chat bubble (bottom right)

3. Type: "What is a CPA?"

4. Hit Send

5. Wait 2-3 seconds for response
```

**If it works, you're done with local testing!** ✓

---

## Deploy to Render (FREE) — 10 min

### Push to GitHub
```bash
git init
git add .
git commit -m "CPA redesign with Cohere backend"
git remote add origin https://github.com/YOUR-USERNAME/cpa-redesign.git
git push -u origin main
```

### Deploy
1. Go to: https://render.com
2. Sign up with GitHub
3. Click **New** → **Web Service**
4. Select your `cpa-redesign` repo
5. Fill in:
   - **Name:** cpa-chat-backend
   - **Build:** npm install
   - **Start:** node server.js
6. Add Environment Variable:
   - **Key:** COHERE_API_KEY
   - **Value:** sk-your-key
7. Click **Create**

Wait 2 minutes. You get a URL like:
```
https://cpa-chat-backend.onrender.com
```

### Update Frontend
In `index.html`, change line ~550:
```javascript
const BACKEND_URL = 'https://cpa-chat-backend.onrender.com'; // Change this
```

Push to GitHub:
```bash
git add index.html
git commit -m "Update backend URL"
git push
```

### Host Frontend on GitHub Pages
1. Go to your repo **Settings** → **Pages**
2. Select **main** branch
3. GitHub creates: https://your-username.github.io/cpa-redesign

**Test:** https://your-username.github.io/cpa-redesign → click chat → should work! ✓

---

## 🎯 To Submit:

Copy-paste this into InternShala:

```
LIVE PROTOTYPE: https://your-username.github.io/cpa-redesign
BACKEND: https://cpa-chat-backend.onrender.com
GITHUB REPO: https://github.com/your-username/cpa-redesign

AI Tools: Cohere API (backend) + Claude (prototype code)
Key Feature: Live chat widget with Cohere API integration
Audience Personalization: Toggle between Public/Student/Member/Firm
```

**Done!** 🚀
