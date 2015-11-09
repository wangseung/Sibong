window.onload = function(){
	make();

	window.onresize = page_layout;

	news_view.addEventListener("scroll", require_list);
}

