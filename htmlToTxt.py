import re


def filter_tags(htmlstr):
    re_cdata = re.compile("//<!CDATA\[[>]∗//\]>", re.I)   # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    re_semicolon = re.compile('[^\n]*;[^\n]*\n')  # ';'所在行
    re_head = re.compile('<!DOCTYPE[^>]*>')

    tmp = re_head.sub('', htmlstr)
    tmp = re_cdata.sub('', tmp)  # 去掉CDATA
    tmp = re_script.sub('', tmp)  # 去掉SCRIPT
    tmp = re_style.sub('', tmp)  # 去掉style
    tmp = re_br.sub('\n', tmp)  # 将br转换为换行
    tmp = re_h.sub('', tmp)  # 去掉HTML 标签
    tmp = re_comment.sub('', tmp)  # 去掉HTML注释
    # tmp = re_semicolon.sub('', tmp)

    # 去掉多余的空行
    blank_line = re.compile('\n+')
    tmp = blank_line.sub('\n', tmp)
    return tmp


if __name__ == '__main__':
    html_file = open('test.html', 'r', encoding='UTF-8').read()
    txt = filter_tags(html_file)
    print(txt)
