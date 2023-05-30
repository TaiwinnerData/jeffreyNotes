from multiprocessing import Process
import time


def write_to_file(x):
    for i in range(100000):
        with open("test"+str(x)+".txt", 'a') as file:
            file.write("file_code: "+str(x)+"\n"+str(i)+"\n")


# Mutliple processes executes
#processes = []
#for i in range(4):
#    p = Process(target=write_to_file, args=(i))
#    p.start()


if __name__ == "__main__":
    processes = []
    start_time = time.time()
    for i in range(4):
        p = Process(target=write_to_file, args=(str(i)))
        p.start()
        process.append(p)
    for  process in processes:
        process.join()

    end_time = time.time()
    delta_time = end_time - start_time
    print("show delta_time:")
    print(delta_time)

