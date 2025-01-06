class Car:
    def send_to_crusher(self):
        print("Sending car to crusher")

class Refrigerator:
    def remove_doors(self):
        print("removing doors from refrigerator")

class ACUnit:
    def drain_freon(self):
        print("Draining freon from AC Unit")

class Bicycle:
    def remove_parts(self):
        print("removing parts from Bicycle")

def destroy(junk: Car | Refrigerator | ACUnit) -> None:
    if isinstance(junk, Car):
        junk.send_to_crusher()
    elif isinstance(junk, Refrigerator):
        junk.remove_doors()
    elif isinstance(junk, ACUnit):
        junk.drain_freon()

r = Refrigerator()
destroy(r)

c = Car()
destroy(c)

a = ACUnit()
destroy(a)

b = Bicycle()
destroy(b)

destroy("Bicycle")
