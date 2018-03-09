var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(document).ready(function() {
	// Remove an alert
	$(".remove-button").click(function() {
		let id = $(this).attr("alert-id");
		// Send the post request
		$.ajax({
			'url': 'remove',
			'type': 'post',
			'data': {
				'id': id
			},
			'headers': {
				'X-CSRFToken': csrftoken
			},
			'dataType': 'json',
			success: function (data) {
				location.reload();
			}
		});
	});

	// Add an alert
	$("#save-button").click(function() {
		$("#error").text("");
		$("#message").text("Loading...");

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
				$("#message").text("");

				let error = data.error;

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