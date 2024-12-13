class product:
    def __init__(self,p_name,p_description,p_prize,p_count):
        self.p_name=p_name
        self.p_description=p_description
        self.p_prize=p_prize
        self.p_count=p_count

class saari(product):
    def __init__(self,silk,assam_silk,p_name,p_description,p_prize,p_count):
        self.silk=silk
        self.assam_silk=assam_silk
        super().__init__(p_name,p_description,p_prize,p_count)


class indian(saari):
    def __init__(self,south,banarasi,maharashrian,silk,assam_silk, p_name, p_description, p_prize, p_count):
        self.south=south
        self.banarasi=banarasi
        self.maharashtrian=maharashrian
        super().__init__(silk, assam_silk, p_name, p_description, p_prize, p_count)

    def variety(self):
        print("varieties of indian saree with  ",{self.silk},"and the name is ",{self.maharashtrian})

        
class south(indian):
    def __init__(self, south, banarasi,maharashrian, silk, assam_silk, p_name, p_description, p_prize, p_count):
        indian.__init__(self,south,banarasi,maharashrian,silk,assam_silk, p_name, p_description, p_prize, p_count)

    def quality(self):
        print("the silk of saree is",{self.silk},"and variety is",{self.south})

obj=south("south_indian","banarasi","maharashtrian","silk","assam_silk","saari","indian",2000,20)
obj.quality()