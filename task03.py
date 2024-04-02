
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

    def lost(self):
        """
        Function restarts count
        :return: None
        """
        self.sheep_count = 0

    def get_count_sheeps(self):
        """
        Function returns sheeps count
        :return: sheep_count
        """
        return self.sheep_count


me = NotSleeping(10)
me.add_sheep()
me.lost()
me.add_sheep(5)
print(me.get_count_sheeps())
