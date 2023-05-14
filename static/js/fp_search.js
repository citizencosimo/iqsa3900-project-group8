var searchTimeout = null;

function getSummary(id) {
    $.ajax({
        type: 'GET',
        url: '/data/getsummary/',
        data: {'id': id},
        dataType: 'json',
        success: function(response) {
            $('#summary-panel').empty()
            console.log(response.publisher)
        },
        error: function (response) {
            console.log('Error:', response);
        }
    })
}
$(document).ready(function() {

    $('#search-input').on('keyup', function() {
        var query = $(this).val().trim();
        var url = '/data/fpsearch/'
        console.log(url)

        if (searchTimeout) {
            clearTimeout(searchTimeout);
        }

        searchTimeout = setTimeout(function() {
            $.ajax({
                type: 'GET',
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
        }, 100);
    });
});
