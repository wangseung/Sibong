
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
	name = document.location.href.split('/')[4]
	temp.open('POST','/stock_item/get_graph_data/' + name);
	temp.send(data);
}

function ajax_get_price_data(){
	var temp = new XMLHttpRequest();
	temp.open("post","/get_price_data/");
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_price_data(temp.responseText);
		}
	}
	temp.send();
}

function ajax_get_news(){
	var temp = new XMLHttpRequest();
	temp.open("post","/stock_item_get_news/");
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_news(temp.responseText);
		}
	}
	temp.send();
}