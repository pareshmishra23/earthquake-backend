*** Test data
in command line - curl -X POST https://overflowing-intuition-production.up.railway.app/upload \
  -H "Content-Type: application/json" \
  -d '[
    {
      "lat": 31.2304,
      "lon": 121.4737,
      "label": "mainshock",
      "timestamp": "2025-07-07T08:45:00"
    },
    {
      "lat": 35.6762,
      "lon": 139.6503,
      "label": "aftershock",
      "timestamp": "2025-07-07T09:20:00"
    },
    {
      "lat": 1.3521,
      "lon": 103.8198,
      "label": "seismic_event",
      "timestamp": "2025-07-07T10:05:00"
    },
    {
      "lat": 21.0278,
      "lon": 105.8342,
      "label": "foreshock",
      "timestamp": "2025-07-07T11:30:00"
    }
  ]' 