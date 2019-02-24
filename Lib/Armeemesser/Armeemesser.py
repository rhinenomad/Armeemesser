import yaml
import procedure

class tester(object):
    def __init__(self,yamlName):
        self.yaml=yaml.load(open(yamlName))
        self.url=self.yaml['url']
        self.variables = self.yaml['vars']
        self.tasks = self.yaml['tasks']
        self.runner=procedure.tasks(self.url,self.variables,self.tasks)

    def run(self):
        self.runner.run()