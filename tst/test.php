<?php
    error_reporting(E_ALL); ini_set('display_errors', '1'); 
    $con = mysqli_connect("localhost","root","root");
    mysqli_select_db($con,"idea");
    $EducationLevel = $_POST['EducationLevel'];
    $Subject = $_POST['Subject'];
    $YourIdea = $_POST['YourIdea'];

    $sql = "INSERT INTO `result` (`id`, `Education_Level`, `Subject`, `Your_Idea`) VALUES (NULL,'$EducationLevel', '$Subject','$YourIdea')";
    mysqli_query($con,$sql);
    mysqli_close($con);
?>