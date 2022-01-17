"""
The direction I choose to take with this exercise was to use classes.
By creating classes, I can make:
    Worker, with a Parent/Child type relationship, once has preference, if they do not need letters, child takes
    Conveyor belt class that can move the belt by creating a new randomized source instance whilst deleting the end one.
    Source that provides the A,B,'' but also randomises which one
    Reporter class that reports all the P's and missed Letters and prints out the final count at the end
    Stage class to know what stage the process is at. 

There is a fair bit I am working out and will need to research to make this work.
"""


import random


# need to have name, componants_needed, time_needed, cache, time_interval, child
class Worker():
    def __init__(self, name, componants_needed, time_needed, child=None):
        self.name = name
        self.comps_needed = componants_needed
        self.time_needed = time_needed
        self.child = child
        self.cache = []
        self.time_interval = time_needed

# Need to create a run function, if all components required are in the cache, 
# Then print 'ready' and if stage value is "" clear cache, time needed and print
# if not all there, pick up what ever is needed and print, time interval should be reduced by 1
# Child to run as else statment

    def run(self, stage):
        if all([x in self.cache for x in self.comps_needed]):
            if self.time_interval <= 0:
                print(f'{self.name} P Ready')
                if stage.value == '':
                    self.cache = []
                    self.time_interval = self.time_needed
                    print(f'{self.name} Is Putting P On ConveyorBelt Belt')
                    stage.value = f'P (by{self.name}'
                else:
                    if self.child: self.child.run(stage)
            else:
                self.time_interval -= 1
                if self.child: self.child.run(stage)
        else:
            if stage.value not in self.cache and stage.value in self.comps_needed:
                print(f'{self.name} Picked Up {stage.value}')
                self.cache.append(stage.value)
                stage.value = ''
            else:
                if self.child: self.child.run(stage)


class Stage():
    def __init__(self, value):
        self.value = value


# Create a source class that pumps out the A,B or "". It needs to be randomised
# so will import random and use the random.choice function

class Source():
    def __init__(self, parts):
        self.parts = parts

    def new(self):
        return random.choice(self.parts)

# This part will analyse the output information from the production line conveyor belt

class Analyse():
    def __init__(self):
        self.data = {'A': 0, 'B': 0, 'P': 0}


# Create a run function for this as well

    def run(self, output):
        if len(output.value) > 0:
            key = output.value[0]
            self.data[key] += 1

# Combine the data to provide correct info

    def report(self):
        data_A = self.data['A']
        data_B = self.data['B']
        data_P = self.data['P']
        print(f'Total Products Created: {data_P}')
        print(f'Total Components Missed: {data_A + data_B}')


'''
By far the tickiest part of all, took a while to work some of this out!
'''
class ConveyorBelt():
    def __init__(self, source, analyse, stages):
        self.source = source
        self.analyse = analyse
        self.stages = [Stage('')] * stages
        self.workers = ConveyorBelt.factory_workers(self.stages)

# This part I am setting up the Parent and Child. two new things I have learnt through this process are 
# @staticmethod and enumerate
    @staticmethod
    def factory_workers(stages):
        workers = {}
        for i, _ in enumerate(stages):
            workers[i] = Worker(f'Parent: {i}',
                                ['A', 'B'], 
                                4, 
                                Worker(f'Child: {i}', 
                                    ['A', 'B'], 
                                    4))
        return workers

    def print_movement(self, x):
        join_values = ' | '.join([s.value for s in self.stages])
        print( f'{x}: ->  {join_values}  -> ')

# This is a run function for the conveyor belt

    def run(self, steps=100):
        for x in range(steps):
            print( '\n' + '--------' * len(self.stages))
            self.stages = [Stage(self.source.new())] + self.stages[:-1]
            self.print_movement(x)
            print('--------' * len(self.stages))
            for i, t in enumerate(self.stages):
                self.workers[i].run(t)
            self.analyse.run(self.stages[-1])
        print('\n' + 'REPORT:')
        self.analyse.report()
        print('\n')
            


def main():
    ConveyorBelt(Source(
                    ['A', 'B', '']), 
                    Analyse(), 
                    stages=3).run()


if __name__ == "__main__":
    main()