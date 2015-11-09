function ajax_get_items(){
	var temp = new XMLHttpRequest();
    temp.open('POST', '/get_items/');
    temp.onreadystatechange = function(){
        if(temp.readyState === 4 && temp.status === 200){
            get_items(temp.responseText);
        }
    }
    temp.send();
}

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

	temp.open('POST','/get_graph_data/');
	temp.send(data);
}

function ajax_get_news(){
	var temp = new XMLHttpRequest();

	temp.open('POST','/get_news/')
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_news(temp.responseText);
		}
	}
	temp.send();
}

function ajax_get_rank(){
	var temp = new XMLHttpRequest();
	temp.open("POST","/get_rank/");
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_rank(temp.responseText);
		}
	}
	temp.send();
}