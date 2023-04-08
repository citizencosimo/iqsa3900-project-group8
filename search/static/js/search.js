let searchForm = document.getElementById('search-form');
let searchBox = document.getElementById('searchbox');

let url = new URL(window.location.origin + window.location.pathname);
console.log(url.pathname)

function search() {
    let query = searchBox.value;
    let url = new URL(window.location.origin + window.location.pathname);
    if (url.pathname !== '/search') {
        url.pathname = '/search';
        url.searchParams.set('q', query);
        window.location.href = url.toString();
    } else {
        url.searchParams.set('q', query);
        window.location.href = url.toString();
    }
}

searchForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    search();
});

searchBox.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the form from submitting normally
        search();
    }
});
