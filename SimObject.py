from random


class SimObject:
    def __init__(self, id, position):
        self.id = id
        self.position_at_start = position
        self.position = position

    def go(self, **kwargs):
        if 'method' in kwargs.keys():
            if kwargs['method'] == 'random':
                actions = [self.forward, self.backward, self.left, self.right]
                choices = random.shuffle(actions)
                for i in choices:
                    try:
                        i()
                        break
                    except:
                        pass


    def forward(self, map):
        pass

    def backward(self, map):
        pass

    def left(self, map):
        pass

    def right(self, map):
        pass



    def step(self):
        self.go(method='random')


