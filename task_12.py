class Dessert:
    def __init__(self):
        self._name = ""
        self._calories = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if isinstance(value, (int, float)):
            self._calories = value
        else:
            raise ValueError("Calories must be a number")

    def is_delicious(self):
        return True

    def is_healthy(self):
        return self._calories < 200


class JellyBean(Dessert):
    def __init__(self):
        super().__init__()
        self._flavor = ""

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_healthy(self):
        return super().is_healthy() and "sugar" not in self._flavor.lower()


# Проверка
if __name__ == "__main__":
    dessert = JellyBean()
    dessert.calories = 150
    print(dessert.calories) #50
    print(dessert.is_delicious()) #True
    print(dessert.is_healthy()) #True
    dessert.flavor = "strawberry"
    print(dessert.flavor) #strawberry
    dessert.calories = 250
    print(dessert.is_healthy()) #False
