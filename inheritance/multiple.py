class phone:
    def __init__(self,calling,picture,video):
        self.calling=calling
        self.picture=picture
        self.video=video
        

class smart_phone:
    def __init__(self,storage,camera,picture_quality,internet):
        self.storage=storage
        self.camera=camera
        self.picture_quality=picture_quality
        self.internet=internet


class iphone(phone,smart_phone):
    def __init__(self,storage,camera,picture_quality,internet,calling,picture,video):
        phone.__init__(self,calling,picture,video)
        smart_phone.__init__(self,storage,camera,picture_quality,internet)

    def quality(self):
        print("iphone has best",{self.picture_quality},"and",{self.video})
        print("iphone has",{self.calling},"and the",{self.picture})
        print("storege",{self.storage},"and",{self.camera},"and",{self.internet})

obj=iphone("storage","camera","picture_quality","intrnet","calling","picture","video")
obj.quality()