import re


def match_password():
    ret = re.match('[a-zA-Z0-9]{6}', '1234abcd')
    print(ret.group())


def split_group():
    # 匹配1-99之间的数字
    ret = re.match(r'[1-9][0-9]|[1-9]', '66')
    print(f'{ret.group()}在1-99之间')


def start_end():
    email_list = {'xiaowang@163.com', 'xiaowang@163.comheihei', '.com.xiaowang@qq.com'}
    for email in email_list:
        ret = re.match(r'[a-zA-Z0-9]{4,20}@163\.com$', email)  # 匹配的字符串出现正则符号必须转义
        if ret:
            print(f'{email}是正确的邮箱地址')
        else:
            print(f'{email}是错误的邮箱地址')


def email_match():
    email_list = {'1620623344@qq.com', '1620623344@163.com', '1620623344@126.com'}
    for email in email_list:
        ret = re.match(r'\w{4,20}@(163|126|qq).com$', email)
        if ret:
            print(f'{email}是正确的邮箱地址')
        else:
            print(f'{email}是错误的邮箱地址')


def name_match():
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h2>www.cskaoyan.com</h2></html>"]
    for label in labels:
        ret = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', lable)
        if ret:
            print(f'{label}是正确的标签')
        else:
            print(f'{label}是错误的标签')


def use_sub():
    ret = re.sub(r'\d+', lambda x: str(int(x.group()) + 2), 'python=997')
    print(ret)
    print('-' * 50)
    txt = 'apple apple apple apple'
    pattern = r'apple'
    replacement = 'orange'
    ret = re.sub(pattern, replacement, txt, count=2)
    print(ret)
    print('-' * 50)
    long_txt = """  <div class="opus-module-content">
                        <p data-v-2505e99a data-v-5b474d2a>
                            <span style="font-size:17px;" data-v-2505e99a>人的大脑，是以无安全感为基本特征的。在等待结果的过程中，你越是期盼着好消息，大脑就越是引导你反复思考坏的情形，在这个反复思考中，大脑会放大甚至扭曲坏的情况所带来的后果，从而导致焦虑。这是没法控制的。如果是长期的或者反复的出现这种折腾，焦虑就有可能成为焦虑症了。
所以，如何缩短这个等待的时间，才是关键。在算力发展如此迅速的今天，缩短这种等待时间，只要愿意做，就能在不久的明天做到。科技发展，是要为人类服务的，在前端消灭问题，才是上策。</span>
                        </p>
                    </div>
                    <div></div>"""
    ret = re.sub(r'<[^>]*>|&nbsp;|\n|\s', '', long_txt)  # 只保留文本内容
    print(ret)


def use_split():
    str1 = '123,45:6 0,789'
    ret = re.split(r',|:| ', str1)
    print(ret)


def use_greedy():
    s='This is a phone 123-456-7890'
    ret=re.match(r'.+?(\d+-\d+-\d+)',s)
    print(ret.group(1))

if __name__ == '__main__':
    # start_end()
    # split_group()
    # email_match()
    # name_match()
    # use_sub()
    # use_split()
    use_greedy()