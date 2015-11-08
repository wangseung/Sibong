
var check = 1;

function ajax_get_graph_data(){
	var temp = new XMLHttpRequest();
    var data = new FormData();
    data.append("data", term.value);

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			if( check == 1){
				first_start_graph(temp.responseText);
			}
			start_graph(temp.responseText);
		}
	}

	temp.open('POST','../js/main/get_graph_data.php');
	temp.send(data);
}
function ajax_get_daily_data(){
	var temp = new XMLHttpRequest();
	temp.open('POST','../js/sospi/get_daily_data.php');

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_daily_data(temp.responseText);
		}
	}
	temp.send();
}