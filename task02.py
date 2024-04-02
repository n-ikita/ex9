
class NotSleeping:
    """
    Class inits a person counting sheeps
    """
    def __init__(self, sheep_count=0):
        self.sheep_count = sheep_count

    def add_sheep(self, sheep_num=1):
        """
        Function adds sheeps to count
        :param sheep_num: number of sheeps
        :return: None
        """
        self.sheep_count += sheep_num


me = NotSleeping(10)
me.add_sheep()
me.add_sheep(5)
print(me.sheep_count)
