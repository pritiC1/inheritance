class laptop:
    def __init__(self,company_name):
        self.company_name=company_name
    
        
class ASUS(laptop):
    def __init__(self,company_name):
        super().__init__(company_name)
    
    def quality(self):
        print("the trusted laptop company name is",{self.company_name})
               
class Thinkpad(laptop):
    def __init__(self,company_name,quality):
        self.quality=quality
        super().__init__(company_name)
    
    def details(self):
        
        print("most of the company use",{self.company_name},"and good",{self.quality})



obj=Thinkpad("thinkpad"," high quality")
obj.details()
