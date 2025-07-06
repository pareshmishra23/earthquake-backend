
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
events = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_event(request: Request):
    data = await request.json()
    events.append(data)
    return {"status": "received", "event": data}

@app.get("/events")
def get_events():
    return events
