const map = L.map('map').setView([39.5, -111.5], 6); // Utah center
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

const yearSelector = document.getElementById('year-selector');
let geojsonLayer;

// Event listener for year selection
yearSelector.addEventListener('change', () => {
  const selectedYear = yearSelector.value;

  if (geojsonLayer) {
    map.removeLayer(geojsonLayer);
  }

  // If nothing selected, do not fetch
  if (!selectedYear) return;

  fetch(`/tethysapp/hello_world/geojson/?year=${selectedYear}`)
    .then(res => res.json())
    .then(data => {
      geojsonLayer = L.geoJSON(data).addTo(map);
      map.fitBounds(geojsonLayer.getBounds());
    })
    .catch(err => console.error('Error loading GeoJSON:', err));
});