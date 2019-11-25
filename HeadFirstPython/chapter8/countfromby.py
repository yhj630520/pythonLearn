class CountFromBy:
    def increase(self) -> None:
        self.val += self.incr

    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def __repr__(self) -> str:
        return str(self.val)


c = CountFromBy(100, 100)
print("val=", c.val, "incr=", c.incr)
c.increase()
c.increase()
c.increase()
print("val=", c.val, "incr=", c.incr)
print(c)
