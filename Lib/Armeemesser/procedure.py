import jinja2

class task(object):
    def __init__(self,url,variables,task):
        self.variabless=variables
        self.url=url
        self.task=task
    def run(self):
        pass

class tasks(object):
    def __init__(self,url,variables,tasks):
        self.variables=variables
        self.url=url
        self.tasks=tasks

    def run(self):
        for task in self.tasks:
            self.runner=task(self.url,self.variables,task)
            self.runner.run()