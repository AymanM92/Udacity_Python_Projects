class Parent():
    def __init__(self,last_name="Name",eye_color='Brown'):
        print("Parent Constructor Called")
        self.LastName = last_name
        self.EyeColor = eye_color

    def ShowInfo(self):
        print("last name is "+self.LastName,"And Eye color is "+self.EyeColor)

class Child(Parent):
    def __init__(self,last_name="Name",eye_color='Brown',toys_number = 0):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.ToysNumber = toys_number

    def ShowInfo(self):
        print("last name is "+self.LastName,"And Eye color is "+self.EyeColor,"With "+str(self.ToysNumber),"Toys")


Younis = Child("Ayman","Black",10)
Younis.ShowInfo()