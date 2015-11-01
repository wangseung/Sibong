
var check = 1;

function ajax_get_graph_data(){
	var temp = new XMLHttpRequest();
    var data = new FormData();
    data.append("data", term.value);
	temp.open('GET','/get_graph_data/');


	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			if( check == 1){
				first_start_graph(temp.responseText);
			}
			start_graph(temp.responseText);
		}
	}

	temp.send(data);
}
function ajax_get_daily_data(){
	var temp = new XMLHttpRequest();
	temp.open('GET','/get_daily_data/');

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_daily_data(temp.responseText);
		}
	}
	temp.send();
}