def divisor (a,b):
    """I divide a by b and return the result"""
    print "Im a function my name is {}".format(divisor.__name__)
    print "im about to divide {} by {}\n\n".format(a,b)
    return a/b #i output a value by using the return statement
    
if __name__ == "__main__":
    divisor (6,2)
    