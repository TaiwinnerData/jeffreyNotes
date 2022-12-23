# create test data 
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# test function y = wx + b and the distance square is (wx_test + b - y_test)^2 + (x - x_test)^2

#def least_action_funct(x, y):
#    w = 1
#    b = 1
#    for i in range(len(x)):


# create differential 
def f_diff(funct, x):
    dx = 0.01
    dy = funct(x+dx) - funct(x)
    return dy/dx


def s_diff(funct, x):
    dx = 0.01
    dy = f_diff(funct, x+dx) - f_diff(funct,  x)
    return dy/dx


def newton_method(funct, times):
    x = 30
    for i in range(times):
        x = x -funct(x)/f_diff(funct, x)
    return x


def newton_method_extreme(funct, times):
    x = 30
    for i in range(times):
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
    print(newton_method(test_funct, 100))
    print("Show newton method to find the extreme value of test_function")
    print(newton_method_extreme(test_funct, 100))
    print("Show newton method to find the extreme value of test_function2")
    print(newton_method_extreme(test_funct2, 100))



if __name__ == "__main__":
    main()
