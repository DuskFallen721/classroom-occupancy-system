// JavaScript for classroom occupancy monitoring and schedule interaction

document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            const section = document.getElementById('availability');
            section.innerHTML = `
                <h2>Backend Status</h2>
                <p><strong>Status:</strong> ${data.status}</p>
                <p><strong>Message:</strong> ${data.message}</p>
            `;
        })
        .catch(error => {
            const section = document.getElementById('availability');
            section.innerHTML = `
                <h2>Backend Status</h2>
                <p>Unable to connect to the backend.</p>
                <p>${error}</p>
            `;
        });
});
