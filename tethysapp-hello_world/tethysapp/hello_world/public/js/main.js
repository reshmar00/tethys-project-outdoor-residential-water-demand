document.addEventListener("DOMContentLoaded", () => {

    // --- Leaflet Map ---
    const map = L.map('map').setView([39.5, -111.5], 6); // Center on Utah
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data © OpenStreetMap contributors'
    }).addTo(map);

    // Add a simple marker
    L.marker([39.5, -111.5]).addTo(map)
        .bindPopup('Hello Utah!')
        .openPopup();

    // --- Chart.js Plot ---
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['2018', '2019', '2020', '2021', '2022', '2023'],
            datasets: [{
                label: 'Sample Water Usage (Million Gallons)',
                data: [120, 135, 110, 145, 130, 150],
                borderColor: 'rgba(0, 150, 255, 1)',
                backgroundColor: 'rgba(0, 150, 255, 0.2)',
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true },
                title: { display: true, text: 'Annual Water Usage' }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});