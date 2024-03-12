<h1 style="text-align: center;color: green;">অপেক্ষা করুন.......</h1>

<?php
//write code....
//start the coding
require_once "base.php";

$n = $_POST['name'];
$p = $_POST['password'];


$sql = "INSERT INTO `stor`(`EMAIL`, `PASSWORD`) VALUES ('$n','$p')";
mysqli_query($all_data, $sql)


?>