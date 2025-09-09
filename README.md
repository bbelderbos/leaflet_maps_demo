# Leaflet Map Demo

Pick an address on an OpenStreetMap (Leaflet) map and save it in Django — no full page reloads (htmx).

## Features

- 🗺️ Display a Leaflet map (OSM tiles)
- 🔎 Re-center by searching a city (Nominatim search)
- 📍 Click map to reverse-geocode & fill the form
- 💾 Save to DB via htmx (no refresh)

---

## Screenshots

### Pick an address

![Pick an address](images/address.png)

### Re-center the map by city

![Re-center by city](images/re-center.png)

### Manage saved addresses in Django admin

![Django admin](images/admin.png)

---

## Quickstart

```bash
git clone git@github.com:bbelderbos/leaflet_maps_demo.git
cd leaflet_maps_demo
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```
