from runners.runnerBase import RunnerBase

class SuperRunner(RunnerBase):

    def __init__(self, params : dict):
        super().__init__(params)

    @classmethod
    def name(cls) -> str:
        return 'superRunner'

    def run(self, user_input: dict, user_params: dict):
        """ Runs the given command using subprocess """
        print('SUPER name=' + self.__class__.__name__ + ', user_params=' + str(user_params) + ', params=' + str(self.params))
 