var selected = [];
var results = [];
$('input[type="checkbox"]').bind('click', function() {
    selected = [];
    $('#selectedTransformations').html('');
    $('input:checked').each(function() {
        selected.push($(this).attr('value'));
    });
    for (var i = selected.length - 1; i >= 0; i--) {
        var li = $('<li>');
        li.text(selected[i]).appendTo('#selectedTransformations');
    }
});
$("#process-button").click(function() {
    console.log(selected);
    post('/pipeline/' + $('#original').val(), {
        list_transformations: selected
    });
});

function post(path, params, method) {
    method = method || "post";
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);
    for (var key in params) {
        if (params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);
            form.appendChild(hiddenField);
        }
    }
    document.body.appendChild(form);
    form.submit();
}
$("#ocr-button").click(function() {
    request = $.ajax({
        url: "/ocr/" + $('#original').val(),
        type: "post",
        data: {
            'text': $('#text').val()
        }
    });
    request.done(function(response, textStatus, jqXHR) {
        console.log(response);
        ocr_table(response);
    });
});

$("#ocr-button-steps").click(function() {
    request = $.ajax({
        url: "/ocr-steps/" + $('#original').val() + "/" + $('#folder').val(),
        type: "post",
        data: {
            'text': $('#text').val()
        }
    });
    request.done(function(response, textStatus, jqXHR) {
        console.log(response);
        ocr_table_steps(response);
    });
});

$("#ocr-button-transformations").click(function() {
    request = $.ajax({
        url: "/ocr-transformations/" + $('#original').val(),
        type: "post",
        data: {
            'text': $('#text').val()
        }
    });
    request.done(function(response, textStatus, jqXHR) {
        console.log(response);
        ocr_table_transformations(response);
    });
});

function ocr_table_steps(results) {
    var container = $('#ocr-table-steps');
    container.html('');
    table = $('<table class="table table-bordered"><thead class="thead-dark"><tr><th>#</th><th>Texto original</th><th>Texto resultado</th><th>%</th></tr></thead>');
    results.forEach(function(result) {
        var tr = $('<tr>');
        ['step', 'original', 'result', 'percentage'].forEach(function(attr) {
            tr.append('<td>' + result[attr] + '</td>');
        });
        table.append(tr);
    });
    container.append(table);
}

function ocr_table(results) {
    var container = $('#ocr-table');
    container.html('');
    table = $('<table class="table table-bordered"><thead class="thead-dark"><tr><th>#</th><th>Texto original</th><th>Texto resultado</th><th>%</th></tr></thead>');
    results.forEach(function(result) {
        var tr = $('<tr>');
        ['pipeline', 'original', 'result', 'percentage'].forEach(function(attr) {
            tr.append('<td>' + result[attr] + '</td>');
        });
        table.append(tr);
    });
    container.append(table);
}


function ocr_table_transformations(results) {
    var container = $('#ocr-table-transformations');
    container.html('');
    table = $('<table class="table table-bordered"><thead class="thead-dark"><tr><th>#</th><th>Texto original</th><th>Texto resultado</th><th>%</th></tr></thead>');
    results.forEach(function(result) {
        var tr = $('<tr>');
        ['transformation', 'original', 'result', 'percentage'].forEach(function(attr) {
            tr.append('<td>' + result[attr] + '</td>');
        });
        table.append(tr);
    });
    container.append(table);
}