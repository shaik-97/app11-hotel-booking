class User:
    def __init__(self, name):
        self.name = name

    @property
    def the_customer_name(self,):
        name = self.name.strip()
        name = name.title()
        return name

user = User(name="  john Doe  ")
# below prop is a method but behaves like variable, so we can access it like a variable without parentheses
print(user.the_customer_name)  # Output: "John Doe"
