from multiprocessing import Pool
import time

def f(x):
    for i in range(1000000):
        # write loop data into test txt file
        with open("test"+str(x)+".txt", "a") as file:
            file.write(str(i)+"\n"+"file_code:"+str(x)+"\n")


if __name__ == "__main__":
    start_time = time.time()
    with Pool(2) as p:
        print("show f(x) return in Pool")
        p.map(f, [1, 2])


    end_time = time.time()
    delta_t2 = end_time - start_time
    print("show delta_t2")
    print(delta_t2)
