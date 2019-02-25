import yaml
import argparse
import string
import config


def plog(str,level=0):
    if level==0:
        print(str)
    elif level==1:
        print('\033[1;32;44m %s \033[0m' % str)
    else:
        print('\033[1;31;44m %s \033[0m' % str)

def task_runner(task,variable,url):
    plog(task)
    plog(variable)
    plog(url)
    pass

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-f','--file',help='')
    parser.add_argument('-u','--url',help='')
    args=parser.parse_args()
    if args.file:
        config.file = args.file
    if args.url:
        config.url = args.url
    plog(config.file)
    test_script = yaml.load(open(config.file))
    variable = test_script['vars']
    tasks=test_script['tasks']
    for task in tasks:
        task_runner(task,variable,config.url)
    pass

if __name__ == '__main__':
    main()