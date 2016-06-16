# function with no return value but parameter, void function
def sign_output(n):
    if n < 0:
        print "negative number"
    elif n == 0:
        print "zero number"
    else:
        print "positive number"

sign_output(-11)
sign_output(0)
sign_output(2222)

# function with return value and parameter, return-type function
def sign(n):
    if n < 0:
        return -1;
    elif n == 0:
        return 0;
    else:
        return 1;

print sign(-10) * sign(-20) # output  1
print sign(-10) * sign( 20) # output -1
print sign( 10) * sign(-20) # output -1
print sign( 10) * sign( 20) # output  1
