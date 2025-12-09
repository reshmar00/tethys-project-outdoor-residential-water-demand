// tethysapp/hello_world/public/js/main.js

document.addEventListener("DOMContentLoaded", () => {
    // Leaflet map
    const map = L.map('map').setView([39.5, -111.5], 6);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    // Chart.js plot
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Apples', 'Oranges', 'Bananas'],
            datasets: [{
                label: 'Fruit Count',
                data: [12, 19, 7],
                backgroundColor: ['red','orange','yellow']
            }]
        }
    });

    // Button to update map
    const yearSelector = document.getElementById('year-selector');
    const loadButton = document.getElementById('load-map');

    loadButton.addEventListener('click', () => {
        const year = yearSelector.value;
        alert("You selected year: " + year);

        // Example marker
        L.marker([39.5, -111.5]).addTo(map)
            .bindPopup(`Year: ${year}`)
            .openPopup();
    });
});