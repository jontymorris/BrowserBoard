var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(document).ready(function() {
	$("#save-button").click(function() {
		// Clear any previous error messages
		$("#error").text("");

		let url = $("#url").val();

		// Send the post request
		$.ajax({
			'url': 'add',
			'type': 'post',
			'data': {
				'url': url
			},
			'headers': {
				'X-CSRFToken': csrftoken
			},
			'dataType': 'json',
			success: function (data) {
				let error = data.error;

				// It worked
				if (!error) {
					location.reload();
				}

				// Something went wrong
				else {
					$("#error").text(error);
				}
			}
		});

	});
});