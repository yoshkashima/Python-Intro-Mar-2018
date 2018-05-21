class Circle(object):
    COUNT = 0
    PI = 3.14  # class attribute

    def __init__(self, radius):
        self.radius = radius  # instance attribute
        Circle.COUNT += 1

    def __del__(self):
        Circle.COUNT -= 1

    def area(self):
        return Circle.PI * self.radius * self.radius

    def circumference(self):
        return 2 * Circle.PI * self.radius

    @classmethod
    def display_pi_value(cls):
        print cls.PI


if __name__ == "__main__":
    print "Count: ", Circle.COUNT
    small = Circle(10)
    Circle.display_pi_value()
    print small.area()
    print small.circumference()
    Circle.display_pi_value()

    print "Count: ", Circle.COUNT

    big = Circle(20)
    print "Count: ", Circle.COUNT

    del big
    print "Count: ", Circle.COUNT
