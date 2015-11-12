function make(){
	make_ingre();
	ajax_get_more_news();
}


var canvas;
var header;
var wrap;

var logout;

var some_box;

var links;

var news;
var news_view;


function make_ingre(){
	logout = document.getElementById("logout");

	header = document.getElementsByTagName("header")[0];
	wrap = document.getElementsByTagName("wrap")[0];

	links = document.getElementById("links");
	some_box = document.getElementsByClassName("some_box")[0];
	news = document.getElementsByClassName("news")[0];
	news_view = document.getElementsByClassName("news_view")[0];

	page_layout();
}
function page_layout(){
	some_box.style.lineHeight = some_box.offsetHeight + "px";

	links.style.height= wrap.offsetHeight - header.offsetHeight + "px"; 
	
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

function get_news(news_array_temp){
	var temp = JSON.parse(news_array_temp);
	for(var i = 0 ; i < temp.length; i++){
		alert(temp[i]);
		if(temp[i].end != 'true'){
			var div_temp = document.createElement("div");
			div_temp.className = "news_box"

			var out = "";
			out += "\
				<span class = 'megaphone_img'>\
					<img src = '/static/images/main/megaphone.png' alt = '뉴스'/>\
				</span>\
				<span class = 'news_text'>\
					<font title = '"+temp[i].content+"'><p>\"\
					"+temp[i].content+"\
					\"</p></font>\
				</span>\
			";
			div_temp.innerHTML = out;

			news_view.appendChild(div_temp);
		}
		else{
			news_view.removeEventListener("scroll",require_list);

			var div_temp = document.createElement("div");
			div_temp.className = "news_end";
			var out = "";
			out += "\
				<span class = 'news_text'>\
					<font title = 'end'><span>End</span></font>\
				</span>\
			";

			div_temp.innerHTML = out;
			news_view.appendChild(div_temp);
		}
	}	

}


var scroll_height;
var scroll_view_height;
var scroll_top;

function require_list(){
	scroll_height = news_view.scrollHeight;
	scroll_view_height = news_view.offsetHeight;
	scroll_top = news_view.scrollTop;

	if(( scroll_height - scroll_top ) <= ( scroll_view_height + 1 ) ){
		news_view.removeEventListener("scroll",require_list);
		 ajax_get_more_news();
	}
	news_view.addEventListener("scroll", require_list);
}

