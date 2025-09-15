class Weapon():
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

    def get_details(self):
        print("name of sword :",self.name)
        print("damage of sword :",self.damage,"%")

sword = Weapon("katana",65)
sword.get_details()