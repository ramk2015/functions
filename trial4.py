def subtractor(a,b): 
    """I subtract b from a and return the result"""  
    return a-b  # i output a value by using the return statement

def divisor (a,b):
    """I divide a by b and return the result"""
    return a/b #i output a value by using the return statement
    
def print_function3(a,b):
    total1 = subtractor(a,b)
    total2 = divisor(a,b)
    print total1, total2
    
if __name__ == "__main__":
    print_function3(a=155,b=5)
    