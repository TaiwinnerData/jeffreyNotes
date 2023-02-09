import numpy as np

def testFunct(x):
    return 3*x**2 + 2*x + 1


def testFunct2(x):
    return 3*x + 3

def testFunct3(x, y):
    return 3*x*y + x*2*y + 1


def first_diff(f_funct, f_x):
    dx = 0.001
    dy = f_funct(f_x+dx) - f_funct(f_x)
    return dy/dx

def second_diff(f_funct, f_x):
    dx = 0.001
    dy = first_diff(f_funct, f_x+dx) - first_diff(f_funct, f_x)
    return dy/dx

# second dimensional partial differnetial for x
def first_p_diff(f_funct, f_x, f_y):
    dx = 0.001
    df = f_funct(f_x+dx, f_y) - f_funct(f_x, f_y)
    return df/dx

def second_p_diff(f_funct, f_x, f_y):
    dx = 0.001
    df = first_p_diff(f_funct, f_x+dx, f_y) - first_p_diff(f_funct, f_x, f_y)
    return df/dx

def second_pxy_diff(f_funct, f_x, f_y):
    dy = 0.001
    df = first_p_diff(f_funct, f_x, f_y+dy) - first_p_diff(f_funct, f_x, f_y)
    return df/dy






# Newton's method is to find the solution of a function.
def newton_method(f_funct, n):
    x0 = 10
    xn = x0
    for i in range(n):
        xn = xn - f_funct(xn)/first_diff(f_funct, xn)
    return xn

# Newton's method for finding the solution of the dy/dx = 0
def newton_method_for_diff(f_funct, n):
    x0 = 10
    xn = x0
    for i in range(n):
        xn = xn - first_diff(f_funct, xn)/second_diff(f_funct, xn)
    return xn


# --------------------------------------------------------------------------------------
# Newton's Method for two variables problem.
# This would use Hessain matrix which is complicated to calculated. And the math behind it is unknow now to me.

# Newton's method is kinda complicated in more than two variables




# --------------------------------------------------------------------------------------
# Gradient Descent method
def GD(f_funct, n):
    xn, yn = 0, 0
    vn = np.array([xn, yn])
    for i in range(n):
        vn = vn - [first_p_diff(f_funct, vn[0], vn[1]), first_p_diff(f_funct, vn[1], vn[0])]
    return [xn, yn]





# define linear regression least action. This function only works on 2 variables problems.
# if the fit line is w1*x1 + w2*x2 = b, then x2 = (b - w1*x1)/w2
# so the y distance between fit line and the data point is Py - (b-w1*Px)/w2 , for (Px, Py) is the example data point.
# so Sigma(Py - (b-w1*Px)/w2)^2 , and we should find the w1, w2 when the Sigma is the minimum
def loss_funct(f_data, w1, w2, b):
    total_result = 0
    for i in range(len(f_data)):
        total_result = total_result + (f_data[1][i] - (b-w1*f_data[0])/w2)**2
    return total_result


def main():
    #testFunct3 = 3*x*y + x*2*y + 1
    # so the partial x differential should be 3y + 2y = 3*2 + 2*2 = 10
    print("show the partial differnetial result of testFunct3 when x = 1, y = 2")
    print(first_p_diff(testFunct3, 1, 2))
    # the answer of below code should be 0
    print("show the second order partial differential result of testFunct3 when x = 1, y=2")
    print(second_p_diff(testFunct3, 2, 1))
    # the answer of below code should 5
    print("show the second order partial differential result of testFunct3 when x = 1, y=2")
    print(second_pxy_diff(testFunct3, 1, 2))

    print("Show the Gradient Descent result of the testFunct3")
    print(GD(testFunct3, 10))






if "__main__" == __name__:
    main()


