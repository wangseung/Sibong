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

function ajax_get_more_news(){
	var temp = new XMLHttpRequest();
	var data = new FormData();
	data.append("length", news_view.children.length);

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_news(temp.responseText);
		}
	}

	temp.open('POST','/get_more_news/')
	temp.send(data);
}


