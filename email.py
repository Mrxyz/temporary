import re


exp_str1 = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
exp_str2 = r'^[a-zA-Z0-9_][^@]+@[^\.]+.*?[^@\.]$'


def reTest(regularExp, test_str):
    if re.match(regularExp, test_str):
        print('ok')
    else:
        print("failed")


def is_valid_email(str):
    re_email = re.compile(r'^([\w\.]+)@(\w+.com)$')
    if re_email.match(str):
        print('ok', re_email.match(str).groups())  # group(2)为域名
    else:
        print('failed')


if __name__ == '__main__':
    reTest(exp_str1, 'bill.gates@microsoft.com')
    reTest(exp_str2, 'bill.gates@microsoft.com')
    is_valid_email('bill.gates@microsoft.com')


