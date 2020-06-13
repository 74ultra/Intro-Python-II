# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, inventory=[]):
        self.name = name
        self.description = description
        self.inventory = inventory

    def desc(self):
        return f'\n{self.name}: {self.description}'
    # def __str__(self):
    #     return f'{self.name}: {self.description}'

    def make_inv(self):
        y = []
        for x in self.inventory:
            y.append(x.name)
        return y

    def room_inv(self):
        if len(self.inventory) == 0:
            return "There are no items you can carry with you in this room\n"
        output = f'\n{self.name} contains:\n'
        item_number = 1
        for i in self.inventory:
            output += f'{item_number}. {i}\n'
            item_number += 1
        return output
