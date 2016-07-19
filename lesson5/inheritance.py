class Dad:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print("%s %s" % (self.first_name, self.last_name))


class Son(Dad):
    def __init__(self, first_name, last_name, toy):
        Dad.__init__(self, first_name, last_name)
        self.toy = toy

johnny = Son(first_name="Johnny", last_name="Brown", toy="Tractor")
johnny.full_name()


class OtherKid():
    def __init__(self, first_name, last_name, toy):
        self.first_name = first_name
        self.last_name = last_name
        self.toy = toy

other_kid = OtherKid(first_name="Jimmy", last_name ="White", toy="Pony")
other_kid.full_name()  # ERROR! This kid does not inherit this function form the Dad class.
