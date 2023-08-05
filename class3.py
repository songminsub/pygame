class God():
    def __init__(self, name, age, country, height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f'저는 {self.name}이고, {self.age}살이며, {self.country}에서 왔고, 키는 {self.height}입니다.')
    
a = God("송민섭", 15, "한국", 165)
b = God("음바페", 23, '프랑스', 180)
c = God("케인", 29, "잉글랜드", 188)
d = God("뮐러", 29, "독일", 185)
e = God("홀란", 22, "노르웨이", 193)
e.introduce()