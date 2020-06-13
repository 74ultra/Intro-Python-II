class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def read_out(self):
        return f'{self.name}: {self.description}'


rake = Item('rake', 'A rusty garden rake')
knife = Item('knife', 'A dull kitchen knife')
hammer = Item('hammer', 'A ball peen hammer')
book = Item('book', 'A book of recipes involving jello from 1954')
flashlight = Item(
    'flashlight', 'A large aluminum flashlight that takes D batteries')
rat = Item('rat', 'The mostly decomposed body of a rat')
