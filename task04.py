
class User:
    def __init__(self, id, nick_name, first_name,
                 last_name='', middle_name='', gender=''):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __repr__(self):
        return f'№{self.id} {self.nick_name} {self.last_name} {self.first_name} {self.middle_name} {self.gender}'



    def update(self, *args, **kwargs):
        self.id = kwargs.get('id', self.id)
        self.nick_name = kwargs.get('nick_name', self.nick_name)
        self.first_name = kwargs.get('first_name', self.first_name)
        self.last_name = kwargs.get('last_name', self.last_name)
        self.middle_name = kwargs.get('middle_name', self.middle_name)
        self.gender = kwargs.get('gender', self.gender)



user1 = User(1, 'qweqwe', 'Nikita', 'Kuznetsov', gender='Male')

print(user1)
user1.update(id=12)
print(user1)
user1.update(id=1234, gender='Helicopter')
print(user1)
