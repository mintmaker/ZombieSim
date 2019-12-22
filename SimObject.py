class SimObject:
    def __init__(self, id, position):
        self.id = id
        self.position_at_start = position
        self.position = position

    def go(self, **kwargs):
        if 'method' in kwargs.keys():
            if kwargs['method'] == 'random':
                actions = [self.forward, self.backward, self.left, self.right]

    def forward(self):
        pass

    def backward(self):
        pass

    def left(self):
        pass

    def right(self):
        pass



    def step(self):
        self.go(method='random')


