import random
class Birthday:
    def __init__(self, people, trials = 10000):
        self.set_people(people)
        self.set_trials(trials)
        self.matches = 0
        self.probability = 0.0
        self.run()

    def set_people(self, people):
        if not isinstance(people, int) or people <= 0:
            raise ValueError("The number of people should only be positive.")
        self.people = people

    def set_trials(self, trials):
        if not isinstance(trials, int) or trials <= 0:
            raise ValueError("The number of trials should only be positive.")
        
        self.trials = trials

    def get_people(self):
        return self.people
    
    def get_trials(self):
        return self.trials
    

    def run(self):
        self.matches = 0
        for _ in range(self.trials):
            birthdays = [random.randint(1, 365) for _ in range(self.people)]
            if len(birthdays) != len(set(birthdays)):
               self.matches += 1 
        self.probability = self.matches / self.trials

    def __str__(self):
        return f"Within {self.people} people, the probaility of getting the same birthdays is {self.probability:.4f}"

def birthday_tester():
    people = int(input("Enter the number of people: "))
    trials = int(input("Enter the number of trials: "))
    
    simulation = Birthday(people, trials)
    print(simulation)

if __name__ == "__main__":
    birthday_tester()
    
