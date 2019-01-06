class Kitten(object):
    number_of_paws = 4
    is_cute = True
    like_to _fight = False
    so_gourmand = True

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_infos(self):
        print('{0} is a {1} kitten'.format(self.name, self.color))


meilv = Kitten('xiaolv', 'brown')
maomao = Kitten('baobe', 'white')
nini = Kitten('xibao', 'pink')

meilv.print_infos
