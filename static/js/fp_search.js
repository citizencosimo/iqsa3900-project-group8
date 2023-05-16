var searchTimeout = null;

/* Prevents the enter key from navigating to the raw JSON string when using live search. */
const searchbar = document.getElementById('search-input');
searchbar.addEventListener("keydown", function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
    }
});

/* Displays the game information when a search result is clicked. */
function getSummary(id) {
    $.ajax({
        type: 'POST',
        url: '/data/getsummary/',
        data: {'id': id},
        dataType: 'json',
        success: function(response) {
            $('#title-card').empty();
            $('#title-card').append(
                response.title + '<span class="title-card-rating">Rating: ' + response.rating + '</span>'
            );
            document.getElementById('toggled-game-view').style.display = 'inline'
            $('#dev-data').empty();
            $('#dev-data').append(
                response.developer
            );
            $('#publisher-data').empty();
            $('#publisher-data').append(
                response.publisher
            );
            $('#summary-data').empty();
            $('#summary-data').append(
                response.gamesum
            );
            const form_review = document.getElementById('review_link');
            form_review.action = `/data/view_game/${response.gameid}`;
            const form_edit = document.getElementById('edit_link');
            form_edit.action = `/data/update_game/${response.gameid}`;
            const form_write = document.getElementById('write_link');
            form_write.action = `/data/review/write_review/${response.gameid}`;
        },
        error: function (response) {
            console.log('Error:', response);
        }
    })
}

/* Function to perform a live search when entering a string into the input. Debouncer employed
* to prevent excessive db calls. */

const debounce_timer = 100 /* ms */
$(document).ready(function() {

    $('#search-input').on('keyup', function() {
        var query = $(this).val().trim();
        var url = '/data/fpsearch/'
        console.log(url)

        if (searchTimeout) {
            clearTimeout(searchTimeout);
        }

        if (query.length >= 3) { // check if input length is at least 3. Prevents search for single letters.
            searchTimeout = setTimeout(function() {
                $.ajax({
                    type: 'POST',
                    url: url,
                    data: {'query': query},
                    dataType: 'json',
                    success: function (response) {
                        $('#search-results').empty();
                        var results = response.results;
                        console.log(results)
                        for (var i = 0; i < results.length; i++) {
                            $('#search-results').append(
                            '<p><a href="#" onclick="getSummary(' + response.string[i][1] + ')">' + response.string[i][0] + '</a></p>'
                            );
                        }
                    },
                    error: function (response) {
                        console.log('Error:', response);
                    }
                });
            }, debounce_timer);
        } else {
            $('#search-results').empty();
        }
    });
});
