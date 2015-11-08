function make(){
	make_ingre();
}


var canvas;
var header;
var wrap;

var logout;

var some_box;

function make_ingre(){
	logout = document.getElementById("logout");

	header = document.getElementsByTagName("header")[0];
	wrap = document.getElementsByTagName("wrap")[0];

	some_box = document.getElementsByClassName("some_box")[0];
	
	page_layout();
}
function page_layout(){
	some_box.style.lineHeight = some_box.offsetHeight + "px";

	set_event();
}

function set_event(){
	logout.addEventListener("click",do_logout);
}



function do_logout(){
	var form_temp = document.createElement("form");
	form_temp.action = "/logout/";
	form_temp.method = "POST";
	form_temp.style.display = "none";

	document.body.appendChild(form_temp);
	if(confirm("정말 로그아웃 하시겠습니까? \n\n") ){
		form_temp.submit();
	}
}
