import os
from runners import *
from runners.runnerBase import RunnerBase

class LocalRunner(RunnerBase):

    def __init__(self, params : dict):
        super().__init__(params)

    @classmethod
    def name(cls) -> str:
        """ Name used in the config """
        return 'localRunner'

    def run(self, user_input: dict, user_params: dict):
        """ Runs the command updated """
        print('name=' + self.__class__.__name__ + ', user_params=' + str(user_params) + ', params=' + str(self.params))
   

if __name__ == '__main__':

    params = { 'params0' : 't' }
    user_params = { 'mydict' : 0 }
    user_input = { 'myinput' : 3}

    runners = []

    try:
        runners.append(RunnerBase.create('localRunner', params))
        runners.append(RunnerBase.create('superRunner', params))
    except NotImplementedError as e:
        print(e)

    for runner in runners:
        runner.run(user_input,user_params)


