function ajax_get_account(){
	var temp = new XMLHttpRequest();

	temp.open("post","../js/mypage/get_account.php");

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_account(temp.responseText);
		}
	}
	temp.send();
}

function ajax_get_value(){
	var temp = new XMLHttpRequest();
	temp.open("post","../js/mypage/get_value.php");
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_value(temp.responseText);
		}
	}
	temp.send();
}
function ajax_get_earn(){
	var temp = new XMLHttpRequest();

	temp.open("post","../js/mypage/get_earn.php");

	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_earn(temp.responseText);
		}
	}
	temp.send();
}

function ajax_get_rank(){
	var temp = new XMLHttpRequest();

	temp.open("post","../js/mypage/get_rank.php");
	temp.onreadystatechange = function(){
		if(temp.readyState === 4 && temp.status === 200){
			get_rank(temp.responseText);
		}
	}
	temp.send();
}