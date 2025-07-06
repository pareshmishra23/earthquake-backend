
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
    
    # Prevent nested lists
    if isinstance(data, list):
        for item in data:
            if isinstance(item, list):  # Flatten inner lists
                events.extend(item)
            else:
                events.append(item)
    else:
        events.append(data)

    return {"status": "received", "count": len(events)}


@app.get("/events")
def get_events():
    return events

@app.get("/reset")
def reset_events():
    events.clear()
    return {"status": "cleared"}
