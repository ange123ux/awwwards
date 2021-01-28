{% load static %} 
<link rel="stylesheet" href="{% static 'js/app.js' %}">

var progressBarOptions = {
	startAngle: -1.55,
	size: 100,
    value: {{caraousel.design}},
    fill: {
		color: 'Chocolate'
	}
}

$('.circle').circleProgress(progressBarOptions).on('circle-animation-progress', function(event, progress, stepValue) {
	$(this).find('strong').text(String((stepValue/10).toFixed(2)));
});

$('#circle-b').circleProgress({
	value : {{caraousel.usability}},
	fill: {
		color: 'Khaki'
	}
});

$('#circle-c').circleProgress({
	value : {{caraousel.creativity}},
	fill: {
		color: 'DarkTurquoise'
	}
});
$('#circle-d').circleProgress({
	value : {{caraousel.content}},
	fill: {
		color: 'SteelBlue'
	}
});

