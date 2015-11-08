<?php
	$a = array();
	if($_POST["data"] == "day"){
		for( $i=0 ; $i < 48; $i++){
			$a[$i] = mt_rand(1,10000);
		}
	}
	else{
		for( $i=0 ; $i< 336; $i++){
			$a[$i] = mt_rand(1,10000);
		}
	}

	echo json_encode($a);
?>