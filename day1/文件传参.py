import sys


def write_hello(file_path):
    file = open(file_path, 'w', encoding='utf-8')
    file.write('hello')
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1])#传参txt1
