$("form").submit(function(e){
	e.preventDefault(); //prevent refresh
	var rows = $('#rows').val();
	var cols = $('#columns').val();

	$.ajax({
		type:'POST',
		url: '/simplex/insert-values/',
		data: {
			rows: rows,
			cols: cols,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
		},
		success: function(data) {

			alert("Submitted");
		}

	});
    // alert("Submitted");
});
