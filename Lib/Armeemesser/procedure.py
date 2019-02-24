import yaml
import worker
import jinja2

#单个Task
class task(object):
    def __init__(self,url,args,processer):
        self.vars=vars
        self.url=url
        self.args=args
        self.processer=processer

#variables，存储着目前全部变量的Dict
#tasks,
class tasks(object):
    def __init__(self,url,variables,tasks):
        self.variables=variables
        self.url=url
        self.tasks=tasks