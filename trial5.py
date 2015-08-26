def side_effect_test(value):
    # Do something to modify the value
    value [0] = [("buffet",135)] #here if value = ... value gets assigned internally seperate from outside function
        print "Inside the function, the value becomes {}".format(value)

if __name__ == "__main__":
    # Create the value
    value = [("sec.analysis",76)]

    print "Outside the function, the value starts as {}".format(value)

    side_effect_test(value)

    print "Outside the function, the value is now {}".format(value)
#Can you identify a pattern which will allow you to work out whether a variable passed into a function can be modified by that function?
#only if you call the variable as an existing list and not as an assignment