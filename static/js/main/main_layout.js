function make(){
	make_ingre();


	ajax_get_items();
	ajax_get_graph_data();
}


var canvas;
var logout;

var some_box;

var items_list;
var item;

var sospi;
var data_term;

var graph_form;
var sospiGraph;
var table_form;
var table_row;
var table_cell;

function make_ingre(){
	logout = document.getElementById("logout");

	items_list = document.getElementsByClassName("items_list")[0];
	item = document.getElementsByClassName("item");

	some_box = document.getElementsByClassName("some_box")[0];
	sospi = document.getElementsByClassName("sospi")[0];
	term = document.getElementById("term");
	data_term = document.getElementsByClassName("data_term");


	graph_form = document.getElementsByClassName("graph_form")[0];
	sospiGraph = document.getElementById("sospiGraph");
	table_form = document.getElementById("table_form");
	table_row = document.getElementsByClassName("y_cell");
	table_cell = document.getElementsByClassName("x_cell");
	page_layout();
}
function page_layout(){
	some_box.style.lineHeight = some_box.offsetHeight + "px";
	sospiGraph.style.height = graph_form.offsetHeight / 100 * 85 - parseInt(getComputedStyle(sospiGraph,true).marginTop) + "px";
	sospiGraph.style.width = graph_form.offsetWidth / 100 * 90 - parseInt(getComputedStyle(sospiGraph,true).marginRight) + "px";
	for( var i = 0 ; i < table_row.length ; i++){
		table_row[i].style.height = table_form.offsetHeight / 6 + "px";
	}
	for( var i = 1 ; i < table_cell.length ; i++){
		table_cell[i].style.width = sospiGraph.offsetWidth / 4 + "px";
	}

	
	document.styleSheets[0].removeRule("canvas",0);
	document.styleSheets[0].addRule("canvas" , "display : inline-block !important; width:"+ sospiGraph.offsetWidth + "px ; height :"+sospiGraph.offsetHeight+ "px ;",0);

	set_event();
}

function set_event(){
	logout.addEventListener("click",do_logout);
	for( var i = 0 ; i < item.length; i++){
		item[i].addEventListener("click", link);
	}
	term.addEventListener("change",ajax_get_graph_data);
}


function start_graph(data_temp){
	var temp = JSON.parse(data_temp);

	var min_temp;
	var max_temp;
	for(var i = 0 ; i < temp.length ; i ++){
		if( i == 0){
			min_temp = temp[i];
			max_temp = temp[i];
		}
		else{
			if( temp[i] < min_temp ){
				min_temp = temp[i];
			}
			else if( temp[i] > max_temp ){
				max_temp = temp[i];
			}
		}
	}

	var max_value = parseInt( max_temp / 100 ) * 100 + 100;

	for( var i = 0 ; i < temp.length ; i ++){
		temp[i] = max_value - temp[i];
	}

	var data_length;

	if( term.value == "day") data_length = 144;
	else if(term.value == "week") data_length = 1008;

	setting_table(max_value);
	VJ.graph("sospiGraph", temp, {max:max_value, width:sospiGraph.offsetWidth, height:sospiGraph.offsetHeight, dataLength: data_length});
	make_ingre();
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

function link(){
	var form_temp = document.createElement("form");
	form_temp.action = "/link_by_code";
	form_temp.method = "POST";

	var out = "";
	out += "<input name = 'code' type = 'button' value = '"+this.children.namedItem('item_code').value+"' />";

	form_temp.innerHTML = out;

	form_temp.submit();
}


function get_items(item_array_temp){
	var temp = JSON.parse(item_array_temp);

	for(var i = 0 ; i < temp.length;i ++){

		var div_temp = document.createElement("div");
		div_temp.className = "item";
		var out = "";
		out += temp[i].item+"<input id = 'item_code' value = '"+temp[i].item+"' />";

		div_temp.innerHTML = out;

		items_list.appendChild(div_temp);
	}

	make_ingre();
}



function setting_table(max){
	var max_temp = max;

	for(var i = 0 ; i < table_row.length;i++){
		table_row[i].innerHTML = max_temp / 5 * ( 5 - i) + " -";
	}
	if( term.value == "day"){
		for(var i = 0 ; i < table_cell.length ; i++){
			table_cell[i].innerHTML = i * 6 +"h";
		}
	}
	else if( term.value == "week"){
		for(var i = 0 ; i < table_cell.length; i++){
			table_cell[i].innerHTML = i * 42 + "h";
		}
	}
}