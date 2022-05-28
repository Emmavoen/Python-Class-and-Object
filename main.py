class Student(object):
    
    # Constructor
    def __init__(self, name, age, tracks,score):
        self.name = name
        self.age = age
        self.score = score 
        self.tracks= []
    # Method to change name
    def change_name(self, n):
        self.name = n
        return self.name
    # Method to change age
    def change_age(self, a):
        self.age = a
        return self.age
    # Method to add track
    def add_track(self, t):
        return self.tracks.append(t)
    # Method to get score
    def get_score(self):
        return self.score

# Create a Student called Bob
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Examples

Bob.change_name('Peter')

Bob.change_age(30)

Bob.add_track("UI/UX")

Bob.add_track("GJ")

Bob.tracks

Bob.get_score()
