# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name}: {self.current_room}'

    def player_inv(self):
        if len(self.inventory) == 0:
            return 'You are not carrying any items'
        else:
            invent = f'{self.name}, you are carrying the following items: '
            for i in self.inventory:
                invent += f'\n {i.name}: {i.description}'
            return invent
