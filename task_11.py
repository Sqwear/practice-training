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
            raise ValueError("Calories must be a number.")

    def is_delicious(self):
        return True

    def is_healthy(self):
        return self.calories < 200

# Проверка
if __name__ == "__main__":
    dessert = Dessert()
    dessert.name = "Cake"
    print(dessert.name) # Cake
    dessert.calories = 150
    print(dessert.calories) # 150
    print(dessert.is_delicious()) # True
    print(dessert.is_healthy()) # True
