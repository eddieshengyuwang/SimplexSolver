$("form").submit(function(e){
	e.preventDefault(); //prevent refresh
	var rows = $('#rows').val();
	var cols = $('#columns').val();
	
	$.ajax({
		type:'POST',
		url: '/simplex/process-dimensions/',
		data: {
			rows: rows,
			cols: cols,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
		},
		success: function(response) {
			$("#second").html(response);
			var matrixHeight = $('#matrix').height();
			var xHeight = $('#x_var').height();

			var difference = (xHeight - matrixHeight)/2;
			$('#x_var').css('top', difference + 'px');
			}
		});
    // alert("Submitted");
});
