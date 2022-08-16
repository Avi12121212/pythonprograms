class Car:
    def __init__(self, car_model, car_price, car_company):
        self.car_model = car_model
        self.car_price = car_price
        self.car_compony = car_company

    def __str__(self):
        return "car_model={0},car_price={1},car_company={2}".format(self.car_model, self.car_price, self.car_compony)


c1 = Car("800", "50000", "maruti")
print(c1)
c2 = Car("Esteem", 1000000, "Maruti")
print(c2)
