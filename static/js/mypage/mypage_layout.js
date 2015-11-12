function make(){
	make_ingre();

	ajax_get_account();
	ajax_get_value();
	ajax_get_earn();
	ajax_get_rank();
}


var canvas;
var header;
var wrap;

var logout;

var some_box;
var name_bar;

var first_row;
var more_row;


var lists;

function make_ingre(){
	logout = document.getElementById("logout");

	header = document.getElementsByTagName("header")[0];
	wrap = document.getElementsByTagName("wrap")[0];
	some_box = document.getElementsByClassName("some_box")[0];
	name_bar = document.getElementsByClassName("name_bar")[0];

	first_row = document.getElementsByClassName("first_row")[0];
	more_row = document.getElementsByClassName("more_row")[0];
	lists = document.getElementsByClassName("lists")[0];

	page_layout();
}
function page_layout(){
	some_box.style.lineHeight = some_box.offsetHeight + "px";
	name_bar.style.lineHeight = name_bar.offsetHeight + "px";
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




function get_account(accout_array_temp){
	var temp = JSON.parse(accout_array_temp);

	for(var i = 0 ; i < temp.length ; i ++){
		var tr_temp = document.createElement("tr");
		var out = "";
		out += "<td>"+temp[i].item+"</td>";
		out += "<td>"+temp[i].past+"</td>";
		out += "<td>"+temp[i].profit+"</td>";
		out += "<td>"+temp[i].now+"</td>";
		out += "<td>"+temp[i].have+"</td>";

		tr_temp.innerHTML = out;

		more_row.appendChild(tr_temp);
	}
}


function get_value(value_data_temp){
	var temp = JSON.parse(value_data_temp);

	var out = "<strong>"+ temp[0].value + "원</strong> 입니다.";

	document.getElementsByClassName("value")[0].innerHTML = out;
}

function get_earn(earn_data_temp){
	var temp = JSON.parse(earn_data_temp);
	var out = "";
	if( temp[0].plus_minus == 1 ){
		out += "<strong class = 'earn_data' style = 'color:blue;'>" + temp[0].earn + "% 상승</strong>했습니다.";
	}
	else if(temp[0].plus_minus == 0){
		out += "<strong class = 'earn_data'>" + temp[0].earn + "%</strong> 변동이 없습니다.";
	}
	else if(temp[0].plus_minus == -1){
		out += "<strong class = 'earn_data' style = 'color:red;'>" + temp[0].earn + "% 하락</strong> 했습니다.";
	}


	document.getElementsByClassName("earn")[0].innerHTML  = out;
}

function get_rank(rank_data_temp){
	var temp = JSON.parse(rank_data_temp);

	for(var i = 0 ; i < temp.length; i++){
		var div_temp = document.createElement("div");
		div_temp.className = "list"

		var out = "";
		out += "<span class = 'grade'>"+(i+1)+".</span>";
		out += "<span class = 'name'><strong>'"+temp[i].name+"'</strong> 님</span>";
		out += "<span class = 'asset'>"+temp[i].asset+" 원</span>";
		
		div_temp.innerHTML = out;

		lists.appendChild(div_temp);

	}
}

