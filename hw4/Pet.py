# Dallin Moore
# https://chat.openai.com/share/6ea8ab16-d29e-470f-9ae1-f114c5cd0cc1

class Pet:
    # make species a class variable
    species = "Unknown"
    
    species_info = {
        'dog': {'average_lifespan': 10, 'multiplier': 7},
        'cat': {'average_lifespan': 15, 'multiplier': 5},
        'rabbit': {'average_lifespan': 8, 'multiplier': 6},
    }
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def calculate_human_years(self):
        if self.species in Pet.species_info:
            lifespan_info = Pet.species_info[self.species]
            human_years = self.age * lifespan_info['multiplier']
            return human_years
        else:
            return "Species information not available."
    
    # get_ave_lifespan must be a classmethod because species must be a class variable
    @classmethod
    def get_ave_lifespan(cls, species):
        species = species.lower()
        if species in cls.species_info:
            return cls.species_info[species]['average_lifespan']
        else:
            return "Species information not available."
        

pet1 = Pet("Donald",5)
pet1.species = 'dog'
print(f"{pet1.name} is {pet1.calculate_human_years()} human years old.")
print(f"The average lifespan of a dog is {Pet.get_ave_lifespan(pet1.species)} years.")

pet2 = Pet("Fiona",12)
pet2.species = 'cat'
print(f"{pet2.name} is {pet2.calculate_human_years()} human years old.")
print(f"The average lifespan of a {pet2.species} is {Pet.get_ave_lifespan(pet2.species)} years.")

pet3 = Pet("Hopper",2)
pet3.species = 'rabbit'
print(f"{pet3.name} is {pet3.calculate_human_years()} human years old.")
print(f"The average lifespan of a {pet3.species} is {Pet.get_ave_lifespan(pet3.species)} years.")
