function make(){
	make_ingre();

	ajax_get_items();
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
	form_temp.action = "/logout";
	form_temp.method = "POST";
	form_temp.style.display = "none";

	document.body.appendChild(form_temp);
	if(confirm("정말 로그아웃 하시겠습니까? \n\n") ){
		form_temp.submit();
	}
}


function submit_check(){
	var form_temp = document.getElementsByTagName("form")[0];
	var select_temp = document.getElementById("items");
	var input_temp = document.getElementById("many");
	form_temp.action = "/deal/buy_stock/";
	form_temp.method = "POST";
	if( items.value == ""){
		alert("종목을 선택해주십시오\n\n");
	}
	else if( many.value == ""){
		alert("주를 선택해주세요\n\n");
	}
	else  if( isNaN(parseInt(many.value))){
		alert("주 선택 창은 숫자만 입력할 수 있습니다.\n\n");
	}
	else if( confirm("정말 진행하시겠습니까? \n\n")){
		form_temp.submit();
	}
}

function get_items(item_array_temp){
	var temp = JSON.parse(item_array_temp);
	var select_temp = document.getElementById("items");

	for(var i = 0 ; i < temp.length ; i++){
		var option_temp = document.createElement("option");
		option_temp.className = "item";
		option_temp.value = temp[i].item;
		option_temp.innerHTML = temp[i].item;

		items.appendChild(option_temp);
	}
}