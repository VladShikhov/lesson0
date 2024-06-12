class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


house_1 = Building(5, 'residential')
house_2 = Building(5, 'residential')
house_3 = Building(1, 'commercial')
print(house_1 == house_2)
print(house_1 == house_3)