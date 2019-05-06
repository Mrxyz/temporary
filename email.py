import re


def is_valid_email(address):
    re_email = re.compile(r'^[\w-]+[\.[\w-]+]*@([\w-]+\.[\w-]+)$')
    obj = re_email.match(address)
    if obj:
        print("账号：%s\n域名：%s" % (obj.group(0), obj.group(1)))  # group(1)为域名
    else:
        print('failed')


test_str = '1661426042@qq.com'
if __name__ == '__main__':
    is_valid_email(test_str)


