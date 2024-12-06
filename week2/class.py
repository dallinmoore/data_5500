class Dog():
    def __init__(self, name, age, owner, breed):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed
        
    def __str__(self):
        return self.name
        
buddy_dog = Dog("buddy", 14, "carol", "golder retriever")

print(buddy_dog)