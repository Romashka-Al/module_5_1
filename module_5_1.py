class House:
    def __init__(self, name, numb):
        self.name = name
        self.numbers_of_floors = numb


    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)

house1 = House("ЖК Эльбрус", 30)
house2 = House("ЖК Воробьёвы горы", 8)
house1.go_to(4)
house2.go_to(10)
