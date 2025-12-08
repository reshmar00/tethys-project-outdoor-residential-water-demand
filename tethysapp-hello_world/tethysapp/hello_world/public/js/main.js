let map;
let geojsonLayer;

document.addEventListener("DOMContentLoaded", () => {
  // Initialize map once
  if (!map) {
    map = L.map('map').setView([39.5, -111.5], 6); // Utah center
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  }

  const yearSelector = document.getElementById('year-selector');
  const loadButton = document.getElementById('load-map');

  if (!yearSelector || !loadButton) {
    console.error("Year selector or Load button not found!");
    return;
  }

  loadButton.addEventListener('click', () => {
    const selectedYear = yearSelector.value;

    if (!selectedYear) {
      alert("Please select a year or range first.");
      return;
    }

    // Remove old layer if present
    if (geojsonLayer) {
      map.removeLayer(geojsonLayer);
    }

    // Fetch GeoJSON from server
    fetch(`${GEOJSON_URL}?year=${selectedYear}`)
      .then(res => {
        if (!res.ok) {
          throw new Error(`GeoJSON fetch failed: ${res.status}`);
        }
        return res.json();
      })
      .then(data => {
        geojsonLayer = L.geoJSON(data).addTo(map);
        map.fitBounds(geojsonLayer.getBounds());
      })
      .catch(err => console.error('Error loading GeoJSON:', err));
  });
});