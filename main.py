from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import httpx, os, uvicorn
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COHERE_API_KEY")
if not API_KEY:
    raise RuntimeError("COHERE_API_KEY missing in .env")

SYSTEM_PROMPT = (
    "You are a friendly, concise demo assistant for the CPA Canada website redesign prototype. "
    "Help visitors with becoming a CPA, CFE exam, membership, CPD, member benefits and firms. "
    "Reply in 3-4 short sentences."
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    chat_history: Optional[List[ChatMessage]] = []
    system: Optional[str] = None

class ChatResponse(BaseModel):
    text: str
    finish_reason: str = "COMPLETE"

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    msg = (req.message or "").strip()
    if not msg:
        raise HTTPException(status_code=400, detail="Empty message")

    messages = []

    sys = (req.system or SYSTEM_PROMPT).strip()
    if sys:
        messages.append({"role": "system", "content": sys})

    last_user = None
    for h in req.chat_history or []:
        c = (h.content or "").strip()
        if not c:
            continue
        if h.role == "user":
            last_user = c
        messages.append({"role": h.role, "content": c})

    if last_user != msg:
        messages.append({"role": "user", "content": msg})

    payload = {
        "model": "command-r-plus-08-2024",
        "messages": messages,
        "temperature": 0.6,
        "max_tokens": 400
    }

    print("Sending payload:")
    print(payload)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            "https://api.cohere.com/v2/chat",
            headers=headers,
            json=payload
        )

    if r.status_code != 200:
        print(r.text)
        raise HTTPException(status_code=r.status_code, detail=r.text)

    data = r.json()
    text = ""

    if "message" in data and "content" in data["message"]:
        for item in data["message"]["content"]:
            if item.get("type") == "text":
                text += item.get("text", "")

    return ChatResponse(text=text.strip() or "No response")

@app.get("/")
async def root():
    return {"message": "CPA Backend Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
