class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_name(self):
        longname=str(self.year)+" "+self.make+" "+self.model
        return longname.title()
mynewcar =car("audi","a4",2016)
print(mynewcar.get_name())






	