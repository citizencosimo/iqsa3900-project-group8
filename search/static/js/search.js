

let searchBox = document.getElementById('searchbox');

searchBox.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the form from submitting normally
        const query = searchBox.value;
        const url = new URL(window.location.href);
        url.searchParams.set('q', query);
        window.location.href = url.toString();
    }
});