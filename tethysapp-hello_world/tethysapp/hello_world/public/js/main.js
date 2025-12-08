const map = L.map('map').setView([39.5, -111.5], 6); // Utah center
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

const yearSelector = document.getElementById('year-selector');
const loadButton = document.getElementById('load-map');
let geojsonLayer;

// Button click triggers fetch
loadButton.addEventListener('click', () => {
  const selectedYear = yearSelector.value;

  if (!selectedYear) {
    alert('Please select a year or range first.');
    return;
  }

  if (geojsonLayer) {
    map.removeLayer(geojsonLayer);
    geojsonLayer = null;
  }

  fetch(`/tethysapp/hello_world/geojson/?year=${selectedYear}`)
    .then(res => {
      if (!res.ok) throw new Error(`HTTP error ${res.status}`);
      return res.json();
    })
    .then(data => {
      geojsonLayer = L.geoJSON(data).addTo(map);
      map.fitBounds(geojsonLayer.getBounds());
    })
    .catch(err => {
      console.error('Error loading GeoJSON:', err);
      alert('GeoJSON not found for selected year.');
    });
});