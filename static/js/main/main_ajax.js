function ajax_get_items(){
	var temp = new XMLHttpRequest();
    temp.open('POST', '../js/main/get_items.php');
    temp.onreadystatechange = function(){
        if(temp.readyState === 4 && temp.status === 200){
            get_items(temp.responseText);
        }
    }
    temp.send();
}


function ajax_get_graph_data(){
	var temp = new XMLHttpRequest();
    var data = new FormData();
    data.append("data", term.value);

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			start_graph(temp.responseText);
		}
	}

	temp.open('POST','../js/main/get_graph_data.php');
	temp.send(data);
}