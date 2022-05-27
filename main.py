class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name:str, age:int, tracks:list, score:float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name (self, new_name:str):
        self.name = new_name
    
    def change_age (self, new_age:int):
        self.age = new_age

    def add_tracks (self, new_tracks):
        self.tracks = new_tracks
    
    def get_score (self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
