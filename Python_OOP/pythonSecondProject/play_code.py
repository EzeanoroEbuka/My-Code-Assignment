class MyStonyStack:

    def __init__(self):
        self.stony = []
        self.queue = []

    def adding_to_stony(self, item):
        self.stony.append(item)

    def pop(self):
        del(self.stony[-1])

    def adding_to_queue(self, item):
        self.queue.append(item)

    def remove(self):
        del(self.queue[0])

