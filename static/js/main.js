$(document).ready(function(){

    var ws = new WebSocket('ws://' + window.location.host + '/info');

    ws.onmessage = function(e){
        if(e.data == 'done'){
            $('.loadding').hide();
        }else {
            jsonObj = JSON.parse(e.data);
            $('<div class="result"><a href="'+jsonObj.url+'" target="_blank"><h1>'+jsonObj.title+'</h1></a></div>').appendTo('.row');
        }
    }

	// halfObject
	var halfObject = function(){
		var brandWidth = ($('#container .brand h1').width() / 2);
		var brandHeight = ($('#container .brand h1').height() / 2);
		$('#container .brand h1').css({
			'margin-left': -brandWidth + "px",
			'margin-top': -brandHeight + "px"
		});
	}
	halfObject();

    $('body').on('click', '#subscribebtn', function(){
        value = $(this).parent().find('input[name="email"]').val();
        $('.row').html('');
        ws.send(JSON.stringify({'target': value}));
        $('.loadding').show();
    });
});