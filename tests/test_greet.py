from lib.greet import greet

def greet_ret_name ():
    result = greet("Ryan")
    assert result == "Hello, Ryan!"