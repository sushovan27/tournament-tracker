document.addEventListener('DOMContentLoaded', function() {
    const loader = document.getElementById('loader');
    const form = document.getElementById('donationForm');

    // Show loader on page load briefly
    loader.classList.add('active');
    setTimeout(() => {
        loader.classList.remove('active');
    }, 1000); // Hide after 1 second (simulates load time)

    // Show loader on form submission
    if (form) {
        form.addEventListener('submit', function() {
            loader.classList.add('active');
        });
    }

    // Show loader on link clicks
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function() {
            loader.classList.add('active');
        });
    });
});