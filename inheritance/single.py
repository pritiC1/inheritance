class farmer:
    def __init__(self,f_name,l_name,address,product,quantity):
        self.f_name=f_name
        self.l_name=l_name
        self.address=address
        self.product=product
        self.quantity=quantity

class seller(farmer):
    def __init__(self,prize,market,f_name,l_name,address,product,quantity):
        self.prize=prize
        self.market=market
        farmer.__init__(self,f_name,l_name,address,product,quantity)

    def details(self):
        print("first name:",{self.f_name})
        print("last name:",{self.l_name})
        print("address:",{self.address})
        print("product name:",{self.product})
        print("product quantity:",{self.quantity})
        print("product prize:",{self.prize})
        print("product market:",{self.market})



obj=seller("dilip","chaugule","mahim","tomato",20,2000,"pandharpur")
obj.details()
       
