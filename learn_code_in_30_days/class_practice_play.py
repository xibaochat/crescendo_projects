class Cosmetics(object):

    def __init__(self, brand, product, price, promotion):
        self.brand = brand
        self.product = product
        self.price_discount = price - (price * promotion) / 100
        self.promotion = promotion


    def crazy_promotion_season(self):
        print('{0} {1} is now {2} with {3}% promotion'.format(self.brand,
                                                             self.product,
                                                             self.price_discount,
                                                             self.promotion))
        



chanel = Cosmetics('chanel', 'mousse', 50, 25)
dior = Cosmetics('dior', 'parfum', 100, 30)
ysl = Cosmetics('ysl','lipstick', 35, 35)
miaomiao = Cosmetics('miaomiao', 'cream', 50, 20)
international_cosmetics = [chanel, dior, ysl, miaomiao]

for great_brand  in international_cosmetics:
        great_brand.crazy_promotion_season()

        
    
        
        
