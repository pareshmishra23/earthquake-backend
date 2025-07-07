
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

import requests
from fastapi import APIRouter

router = APIRouter()

@router.get("/external-events")
def get_usgs_earthquakes():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    r = requests.get(url)
    data = r.json()

    results = []
    for feature in data.get("features", []):
        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]
        results.append({
            "lat": coords[1],
            "lon": coords[0],
            "label": f"M{props['mag']} - {props['place']}",
            "timestamp": props["time"]
        })

    return results

