if 0.1+0.2 ==0.3:
    print("yes")
else:
    print("no") 
    print(0.1+0.2)
    print(0.3)

# 1. Define the decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()  # Calls the original function
        print("Something is happening AFTER the function is called.")
    return wrapper  # Returns the inner function

# 2. Apply the decorator using the @ symbol
@my_decorator
def say_hello():
    print("Hello, World!")

# 3. Call the decorated function
say_hello()
