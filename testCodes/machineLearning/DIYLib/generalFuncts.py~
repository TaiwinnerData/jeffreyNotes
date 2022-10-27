# create differential 
def f_diff(funct, x):
    dx = 0.01
    dy = funct(x+dx) - funct(x)
    return dy/dx


def s_diff(funct, x):
    dx = 0.01
    dy = f_diff(funct, x+dx) - f_diff(funct,  x)
    return dy/dx


def newton_method(funct):
    x = 30
    for i in range(100):
        x = x -funct(x)/f_diff(funct, x)
    return x


def newton_method_extreme(funct):
    x = 30
    for i in range(100):
        x = x - f_diff(funct, x)/s_diff(funct, x)

    return x



def test_funct(x):
    return x**2+2*x+1  


def test_funct2(x):
    return 3*x**2+3*x+1


def main():
    print("Show first order differential results of test_function")
    print(f_diff(test_funct, 3))
    print("Show second order differential reulst of test_function")
    print(s_diff(test_funct, 3))
    print("Show newtom method to find the solution of the test_function")
    print(newton_method(test_funct))
    print("Show newton method to find the extreme value of test_function")
    print(newton_method_extreme(test_funct))
    print("Show newton method to find the extreme value of test_function2")
    print(newton_method_extreme(test_funct2))



if __name__ == "__main__":
    main()
