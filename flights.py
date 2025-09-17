from serpapi import GoogleSearch

params = {
    "api_key": "3d04359109074907ef88e7fa280690ea23e42a440fb1c68859a9fe8b430f4942",
  "engine": "google_flights",
  "departure_id": "YYZ",
  "arrival_id": "IAH",
  "type": 1,
  "outbound_date": "2025-12-17",
 "return_date": "2026-01-07",
  "currency": "CAD",
  "hl": "en",
  "gl": "ca",
  "travel_class": 1,
  "show_hidden": "true",
  "deep_search": "true",
  "sort_by": 2,
  "stops": 2
}

search = GoogleSearch(params)
results = search.get_dict()

print(results)
