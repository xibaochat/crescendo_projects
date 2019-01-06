class kitten(object):
    """
    Create a kitten object
    """

    number_of_paws = 4
    is_cute = True
    have_tail = True
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_infos(self):
        print("{0} is a {1} kitten".format(self.name,
                                           self.color))

meilv = kitten('Meilv', 'brown')
xinxin = kitten('Baobe', 'white')
xibao = kitten('nyny', 'pink')

kittens_list = [meilv, xinxin, xibao]

for instance in kittens_list:
    instance.print_infos()

