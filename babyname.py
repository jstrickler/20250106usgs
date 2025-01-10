class BabyName:
    def __init__(self, baby_name):
        self._baby_name = baby_name

    @property
    def baby_name(self):
        return self._baby_name

    def __add__(self, other):
        return BabyName(" ".join([self.baby_name, other.baby_name]))

if __name__ == "__main__":    
    b1 = BabyName("Billie")
    b2 = BabyName("Jean")
    b3 = b1 +  b2
    print(f"{b3.baby_name = }")
    