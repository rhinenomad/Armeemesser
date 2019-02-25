import yaml
import argparse
import string
import config

class Statistic(object):
    success_task = []
    success_num = 0
    failed_num = 0
    failed_task=[]
    def success(self,name):
        self.success_num += 1
        self.success_task.append(name)
    def fail(self,name):
        self.failed_num += 1
        self.failed_task.append(name)
    def show_result(self):
        print(self.success_task)
        print(self.failed_task)
        pass

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
    TaskStatistic.success(task['name'])
    TaskStatistic.fail(task['name'])
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
    test_script = yaml.load(open(config.file))
    variable = test_script['vars']
    tasks=test_script['tasks']
    for task in tasks:
        task_runner(task,variable,config.url)
    pass
    TaskStatistic.show_result()

TaskStatistic = Statistic()
if __name__ == '__main__':
    main()