function ajax_get_items(){
	var temp = new XMLHttpRequest();
	temp.open("post","../js/deal/get_items.php");
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_items(temp.responseText);
		}
	}
	temp.send();
}