function Validator(cases){
    var valid = true, after = 0,
		to_seconds = [3600, 60, 1];
    var alarm = 0;
	cases.forEach(function(data){
			// Using the validity property in HTML5-enabled browsers:
		after += to_seconds[cases.indexOf(data)] * data;

	});
	alarm = after;
	return alarm;
}

var cases = [0, 3, 4];
console.log(Validator(cases));
var play = "deactive";
var class_alarm = "deactive";
var alarm_counter = 10;
(function Validator2(){



    
        var digit_to_name = 'zero one two three four five six seven eight nine'.split(' ');

	// This object will hold the digit elements
	    var digits = {};

	// Positions for the hours, minutes, and seconds
	    var positions = [
		'h1', 'h2', ':', 'm1', 'm2', ':', 's1', 's2'
	    ];
    	var weekday_names = 'MON TUE WED THU FRI SAT SUN'.split(' ');
		var now = moment().format("hhmmssdA");

		digits.h1 = digit_to_name[now[0]];
		digits.h2 = digit_to_name[now[1]];
		digits.m1 = digit_to_name[now[2]];
		digits.m2 = digit_to_name[now[3]];
		digits.s1 = digit_to_name[now[4]];
		digits.s2 = digit_to_name[now[5]];

		// The library returns Sunday as the first day of the week.
		// Stupid, I know. Lets shift all the days one position down, 
		// and make Sunday last

		var dow = now[6];
		dow--;
		
		// Sunday!
		if(dow < 0){
			// Make it last
			dow = 6;
		}

		// Mark the active day of the week
		var weekdays_active = weekday_names[dow];

		// Set the am/pm text:
		var ampm = now[7]+now[8];


		// Is there an alarm set?

		if(alarm_counter > 0){
			
			// Decrement the counter with one second
			alarm_counter--;

			// Activate the alarm icon
			class_alarm = 'active';
		}
		else if(alarm_counter == 0){

			play = "active";
			alarm_counter--;
			class_alarm = 'deactive';
		}
		else{
			// The alarm has been cleared
			class_alarm = 'deactive';
		}

		// Schedule this function to be run again in 1 sec
		setTimeout(Validator2, 1000);
		console.log(digits);
        console.log(weekdays_active);
        console.log(alarm_counter);
        console.log(class_alarm, play)

})();

;
