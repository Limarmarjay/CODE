class Human():
    HANDS = 4   # Class Variable.
    
    def __init__(self, name_, gender_, occupation_):  # Constructor. Python's special function used for setting initial values to the variables.
        self.name = name_      # self.name is an instance variable
        self.gender = gender_  # self.gender is an instance variable
        self.occupation = occupation_  # self.occupation is an instance variable
        
# Python non-static functions must have the conventional keyword "self" inside the parameters list before any other parameter is added.
    def doWork(self):           # Non-Static method
        if self.gender == "Homme":
            print(self.name, "Est un Homme")
        elif self.gender == "Femme":
            print(self.name, "Est un Femme")
        if self.occupation == "etudiante en informatique":
            print(self.name, "Est toujours a l'ecole")
        elif self.occupation == "Ingénieur-conseil m en informatique.":
            print(self.name, "Est un employe a temps plein")
    def speak_(self): 
        print(self.name, "Dit comment allez_vouz aujourd'hui?")
# Python static/class functions do not include the conventional keyword "self" in the parameters list. the decorator "@staticmethod" must be used to declare non-static functions.
    @staticmethod
    def faceShape():
        faceshape = "Oblong"
        print(faceshape)

Aalicia = Human("Aalicia Jay", "Femme", "etudiante en info")    #Aalicia is an instantiated object of the class-Human
Rodney = Human("Rodney Gaines", "Homme", "Ingénieur-conseil m en informatique.")    #Rodney is an instantiated object of the class-Human

Aalicia.doWork()
print(Aalicia.name)
Aalicia.speak_()
print(Human.HANDS)

Rodney.doWork()
print(Rodney.name)
Rodney.speak_()

Human.faceShape()