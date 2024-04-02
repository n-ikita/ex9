
class Game:
    def __init__(self, info):
        self.command1 = info['command1']
        self.command2 = info['command2']
        self.score = [0, 0]

    def ball_thrown(self, command, points):
        if command in (1, '1', 'command1', self.command1):
            self.score[0] += points
        else:
            self.score[1] += points

    def get_score(self):
        return tuple(self.score)

    def get_winner(self):
        if self.score[0] > self.score[1]:
            return self.command1
        if self.score[0] < self.score[1]:
            return self.command2
        return 'Ничья'


world_championship = Game({'command1': 'Russia', 'command2': 'France'})

print(world_championship.get_score(), world_championship.get_winner())
world_championship.ball_thrown('Russia', 3)
print(world_championship.get_score(), world_championship.get_winner())

