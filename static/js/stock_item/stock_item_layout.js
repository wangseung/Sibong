function make(){
	make_ingre();
	ajax_get_graph_data();
	ajax_get_price_data();
	ajax_get_news();
}


var canvas;
var header;
var wrap;

var logout;

var name_bar;
var some_box;

var sospi;
var data_term;

var graph_form;
var stock_item_graphGraph;
var stock_item_graphGraph_1;
var table_form;
var table_row;
var table_cell;

var lists;

function make_ingre(){
	logout = document.getElementById("logout");

	header = document.getElementsByTagName("header")[0];
	wrap = document.getElementsByTagName("wrap")[0];


	name_bar = document.getElementsByClassName("name_bar")[0];

	some_box = document.getElementsByClassName("some_box")[0];
	sospi = document.getElementsByClassName("sospi")[0];
	term = document.getElementById("term");
	data_term = document.getElementsByClassName("data_term");


	graph_form = document.getElementsByClassName("graph_form")[0];
	stock_item_graphGraph = document.getElementById("stock_item_graphGraph");
	stock_item_graphGraph_1 = document.getElementById("stock_item_graphGraph_1");
	table_form = document.getElementById("table_form");
	table_row = document.getElementsByClassName("y_cell");
	table_cell = document.getElementsByClassName("x_cell");

	lists = document.getElementsByClassName("lists")[0];

	page_layout();
}
function page_layout(){
	some_box.style.lineHeight = some_box.offsetHeight + "px";
	name_bar.style.lineHeight = name_bar.offsetHeight + "px";
	
	stock_item_graphGraph.style.height = graph_form.offsetHeight / 100 * 85 - parseInt(getComputedStyle(stock_item_graphGraph,true).marginTop) + "px";
	stock_item_graphGraph.style.width = graph_form.offsetWidth / 100 * 90 - parseInt(getComputedStyle(stock_item_graphGraph,true).marginRight) + "px";
	stock_item_graphGraph_1.style.width = stock_item_graphGraph.offsetWidth + "px";
	stock_item_graphGraph_1.style.height = stock_item_graphGraph.offsetHeight + "px";
	for( var i = 0 ; i < table_row.length ; i++){
		table_row[i].style.height = table_form.offsetHeight / 6 + "px";
	}
	for( var i = 1 ; i < table_cell.length ; i++){
		table_cell[i].style.width = stock_item_graphGraph.offsetWidth / 4 + "px";
	}

	
	document.styleSheets[0].removeRule("canvas",0);
	document.styleSheets[0].addRule("canvas" , "display : inline-block !important; width:"+ stock_item_graphGraph.offsetWidth + "px ; height :"+stock_item_graphGraph.offsetHeight+ "px ;",0);

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

	var max_value = parseInt( max_temp / 100 ) * 100 + 100;

	for( var i = 0 ; i < temp.length ; i ++){
		temp[i] = max_value - temp[i];
	}

	var data_length;

	if( term.value == "day"){
		stock_item_graphGraph.style.zIndex = "10";
		stock_item_graphGraph_1.style.zIndex = "-1";
		VJ.graph("stock_item_graphGraph").options.max = max_value;
		for (var i = 0 ; i < temp.length ; i++){
			VJ.graph("stock_item_graphGraph").appendData([temp[i]]);
		}
	}
	else if(term.value == "week"){
		stock_item_graphGraph_1.style.zIndex = "10";
		stock_item_graphGraph.style.zIndex = "-1";
		VJ.graph("stock_item_graphGraph_1").options.max = max_value;
		for (var i = 0 ; i < temp.length ; i++){
			VJ.graph("stock_item_graphGraph_1").appendData([temp[i]]);
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

	var max_value = parseInt( max_temp / 100 ) * 100 + 100;

	for( var i = 0 ; i < temp.length ; i ++){
		temp[i] = max_value - temp[i];
	}

	var data_length;

	VJ.graph("stock_item_graphGraph", [0,0,0], {max:max_value, width:stock_item_graphGraph.offsetWidth, height:stock_item_graphGraph.offsetHeight, dataLength:48 });
	VJ.graph("stock_item_graphGraph_1", [0,0,0], {max:max_value, width:stock_item_graphGraph.offsetWidth, height:stock_item_graphGraph.offsetHeight, dataLength:336 });

	if( term.value == "day"){
		stock_item_graphGraph.style.zIndex = "10";
		stock_item_graphGraph_1.style.zIndex = "-1";
	}
	else if(term.value == "week"){
		stock_item_graphGraph_1.style.zIndex = "10";
		stock_item_graphGraph.style.zIndex = "-1";
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


function get_price_data(price_data_temp){
	var temp = JSON.parse(price_data_temp);

	var out = "";

	if(temp.up_down == 1){
		out += "<img src = '/static/images/stock_item/"+temp.img+"_sibong.png' alt = '전일 대비 상승'/>";
	}
	else if(temp.up_down == 0){
		out += "<img src = '/static/images/stock_item/"+temp.img+"_sibong.png' alt = '전일과 동일'/>";
	}
	else if(temp.up_down == -1){
		out += "<img src = '/static/images/stock_item/"+temp.img+"_sibong.png'' alt = '전일 대비 하락'/>";
	}

	out += "<span class = 'value' >"+temp.value+"</span>";

	if(temp.up_down == 1){
		out += "<span class = 'up_down'><span style = color:blue>+</span>"+temp.percent+"%</span>";
	}
	else if(temp.up_down == 0){
		out += "<span class = 'up_down'>"+temp.percent+"%</span>";
	}
	else if(temp.up_down == -1){
		out += "<span class = 'up_down'><span style = color:red>-</span>"+temp.percent+"%</span>";
	}

	document.getElementsByClassName("price_data")[0].innerHTML = out;
}

function get_news(news_array_temp){
	var temp = JSON.parse(news_array_temp);
	
	for(var i = 0 ; i < temp.length;i++){
		var div_temp = document.createElement("div");
		div_temp.className = "list";

		var out = "";
		out += "<span>"+temp[i].content+"</span>";
		out += "<img src = '/static/images/stock_item/newsbutton.png' alt = '최근 뉴스' />";

		div_temp.innerHTML = out;

		lists.appendChild(div_temp);
	}
}