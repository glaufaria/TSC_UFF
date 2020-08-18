<?php
Function add_extra($string) {
 return "DEF";
}
$str = "ABC"; 
$str.=add_extra($str); 
echo $str;
?>