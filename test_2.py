class Car(object):
    def __init__(self,cardata):
        self.cardata=cardata

    def CarData(self):
        if self.cardata['hp'] >=500:
            print(self.cardata['model']+" is supercar")

class SuperCar(Car):
    def __init__(self,cardata,price):
        super(SuperCar,self).__init__(cardata)
        self.price=price

    def price_com(self):
        if self.price>=1000:
            print(self.cardata['model']+' is expensive')

Car1={"brand":"Lamborghini","model":"LP750","hp":750}
Car2={"brand":"Buggati","model":"Chrion","hp":1500}
Lam=Car(Car1)
Lam.CarData()
Bug=SuperCar(Car2,2000)
Bug.CarData()
Bug.price_com()