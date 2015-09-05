$(document).ready(function(){
	var processingString = '<h3 class="red height500">Error in Installation. Please Call at this number</h3>';


	$('#submit').click(function(){
		var userfirstname = $('#userfirstname').val();
		var userlastname = $('#userlastname').val();
		var useremailid = $('#useremailid').val();

		$("#mainContent").empty();
		$("#mainContent").toggleClass('loading');

		setTimeout(function(){
			$("#mainContent").toggleClass('loading');
			$("#mainContent").append(processingString);
		},3000);

	});
});