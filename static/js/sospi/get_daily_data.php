<?php
	$a = array(
		array("date" => "10/13", "price" => "35,000" , "percent" => "3" , "plus_minus" => "1"),
		array("date" => "10/12", "price" => "35,000" , "percent" => "33" , "plus_minus" => "-1"),
		array("date" => "10/11", "price" => "40,000" , "percent" => "3" , "plus_minus" => "1"),
		array("date" => "10/10", "price" => "35,000" , "percent" => "3" , "plus_minus" => "1"),
		array("date" => "10/9", "price" => "14,000" , "percent" => "0" , "plus_minus" => "0"),
		array("date" => "10/8", "price" => "35,000" , "percent" => "2" , "plus_minus" => "1"),
		array("date" => "10/7", "price" => "25,000" , "percent" => "3" , "plus_minus" => "-1"),
		array("date" => "10/6", "price" => "35,000" , "percent" => "3" , "plus_minus" => "1"),
		array("date" => "10/5", "price" => "2,000" , "percent" => "0" , "plus_minus" => "0"),
		array("date" => "10/4", "price" => "35,000" , "percent" => "2" , "plus_minus" => "1"),
		array("date" => "10/3", "price" => "145,000" , "percent" => "1" , "plus_minus" => "-1"),
		array("date" => "10/2", "price" => "100,000" , "percent" => "4" , "plus_minus" => "1"),
		array("date" => "10/1", "price" => "23,000" , "percent" => "6" , "plus_minus" => "-1")
	);

	echo json_encode($a);
?>