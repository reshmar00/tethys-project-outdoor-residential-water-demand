document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([39.5, -111.5], 6); // Utah center
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    const yearSelector = document.getElementById('year-selector');
    const loadButton = document.getElementById('load-map');
    let geojsonLayer;

    loadButton.addEventListener('click', () => {
        const selectedYear = yearSelector.value;

        if (geojsonLayer) {
            map.removeLayer(geojsonLayer);
        }

        if (!selectedYear) return;

        fetch(`${GEOJSON_URL}?year=${selectedYear}`)
        .then(res => res.json())
        .then(data => {
          if (geojsonLayer) map.removeLayer(geojsonLayer);
          geojsonLayer = L.geoJSON(data).addTo(map);
          map.fitBounds(geojsonLayer.getBounds());
        })
        .catch(err => console.error('Error loading GeoJSON:', err));
    });
});