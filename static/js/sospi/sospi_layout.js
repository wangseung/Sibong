function make(){
	make_ingre();
	ajax_get_graph_data();
	ajax_get_daily_data();
}


var canvas;
var header;
var wrap;

var logout;

var some_box;


var sospi;
var data_term;

var graph_form;
var sospiGraph;
var sospiGraph_1;
var table_form;
var table_row;
var table_cell;


var lists;

function make_ingre(){
	logout = document.getElementById("logout");

	header = document.getElementsByTagName("header")[0];
	wrap = document.getElementsByTagName("wrap")[0];


	some_box = document.getElementsByClassName("some_box")[0];
	sospi = document.getElementsByClassName("sospi")[0];
	term = document.getElementById("term");
	data_term = document.getElementsByClassName("data_term");


	graph_form = document.getElementsByClassName("graph_form")[0];
	sospiGraph = document.getElementById("sospiGraph");
	sospiGraph_1 = document.getElementById("sospiGraph_1");
	table_form = document.getElementById("table_form");
	table_row = document.getElementsByClassName("y_cell");
	table_cell = document.getElementsByClassName("x_cell");

	lists = document.getElementsByClassName("lists")[0];

	page_layout();
}
function page_layout(){
	some_box.style.lineHeight = some_box.offsetHeight + "px";

	table_row[0].style.maxWidth = table_form.offsetWidth / 4 + "px";
	table_row[0].style.marginTop = "0.1rem";
	for( var i = 0 ; i < table_row.length ; i++){
		if( i == 0){
			table_row[i].style.height = table_form.offsetHeight / 5 +"px";
		}
		else{
			table_row[i].style.height = table_form.offsetHeight / 5 + "px";
		}
		table_row[table_row.length - 1].style.height = "0px";
		table_row[i].style.verticalAlign = "top";
		table_row[i].style.minWidth = table_row[0].offsetWidth + "px";
	}
	sospiGraph.style.height = graph_form.offsetHeight / 100 * 85 - parseInt(getComputedStyle(sospiGraph,true).marginTop) + "px";
	//sospiGraph.style.width = graph_form.offsetWidth / 100 * 90 - parseInt(getComputedStyle(sospiGraph,true).marginRight) + "px";
	sospiGraph.style.width = table_form.offsetWidth - table_row[0].offsetWidth- parseInt(getComputedStyle(sospiGraph,true).marginRight)+ "px";
	sospiGraph_1.style.width = sospiGraph.offsetWidth + "px";
	sospiGraph_1.style.height = sospiGraph.offsetHeight + "px";

	for( var i = 1 ; i < table_cell.length ; i++){
		table_cell[i].style.width = sospiGraph.offsetWidth / 4 + "px";
	}

	
	document.styleSheets[0].removeRule("canvas",0);
	document.styleSheets[0].addRule("canvas" , "display : inline-block !important; width:"+ sospiGraph.offsetWidth + "px ; height :"+sospiGraph.offsetHeight+ "px ;",0);

	set_event();
}

function set_event(){
	logout.addEventListener("click",do_logout);
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
	var max_value = (parseInt( max_temp ) * 1.3).toFixed(0);

	for( var i = 0 ; i < temp.length ; i ++){
		temp[i] = max_value - temp[i];
	}

	var data_length;

	if( term.value == "day"){
		sospiGraph.style.zIndex = "10";
		sospiGraph_1.style.zIndex = "-1";
		VJ.graph("sospiGraph").options.max = max_value;
		for (var i = 0 ; i < temp.length ; i++){
			VJ.graph("sospiGraph").appendData([temp[i]]);
		}
	}
	else if(term.value == "week"){
		sospiGraph_1.style.zIndex = "10";
		sospiGraph.style.zIndex = "-1";
		VJ.graph("sospiGraph_1").options.max = max_value;
		for (var i = 0 ; i < temp.length ; i++){
			VJ.graph("sospiGraph_1").appendData([temp[i]]);
		}
	}


	setting_table(max_value);
	make_ingre();
}


function first_start_graph(temp_array){
	var temp = JSON.parse(temp_array);
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
	var max_value = (parseInt( max_temp ) * 1.3).toFixed(0);

	for( var i = 0 ; i < temp.length ; i ++){
		temp[i] = max_value - temp[i];
	}

	var data_length;

	VJ.graph("sospiGraph", [0,0,0], {max:max_value, width:sospiGraph.offsetWidth, height:sospiGraph.offsetHeight, dataLength:48 });
	VJ.graph("sospiGraph_1", [0,0,0], {max:max_value, width:sospiGraph.offsetWidth, height:sospiGraph.offsetHeight, dataLength:336 });

	if( term.value == "day"){
		sospiGraph.style.zIndex = "10";
		sospiGraph_1.style.zIndex = "-1";
	}
	else if(term.value == "week"){
		sospiGraph_1.style.zIndex = "10";
		sospiGraph.style.zIndex = "-1";
	}
	check = 0;
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

function setting_table(max){
	var max_temp = max;

	for(var i = 0 ; i < table_row.length;i++){
		var temp = Math.round(max_temp /4 * ( 4-i )/100 )* 100;
		table_row[i].innerHTML = commify(temp) + " -&nbsp&nbsp";
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

function get_daily_data(daily_data_temp){
	var temp = JSON.parse(daily_data_temp);

	for(var i = 0 ; i < temp.length ; i++){
		var div_temp = document.createElement("div");
		div_temp.className = "list";

		var out = "";
		out += "<span class = 'date'>"+temp[i].date+"</span>";
		out += "<span class = 'price'>"+temp[i].price+"</span>";
		if(temp[i].plus_minus == 1){

			out += "<span class = 'fluctuation_rate'><span class = 'plus_minus' style = 'color: red;'>"+"+"+"</span>"+temp[i].percent+"%</span>";
		}
		else if(temp[i].plus_minus == 0){
			out += "<span class = 'fluctuation_rate'><span class = 'plus_minus'>"+"&nbsp"+"</span>"+temp[i].percent+"%</span>";
		}
		else if(temp[i].plus_minus == -1){
			out += "<span class = 'fluctuation_rate'><span class = 'plus_minus' style = 'color: blue;'>"+"-"+"</span>"+temp[i].percent+"%</span>";
		}

		div_temp.innerHTML = out;

		lists.appendChild(div_temp);
	}
}

function commify(n) {
  var reg = /(^[+-]?\d+)(\d{3})/;
  n += '';

  while (reg.test(n))
    n = n.replace(reg, '$1' + ',' + '$2');

  return n;
}