import time


def fun(i):
    res = lambda i: i ** i
    return res(i)


start_time = time.time()
fun(fun(5))
end_time = time.time()
timetaken = end_time - start_time
print("Время выполнения: ", timetaken)
# Вывод:
Время выполнения:  0.0009870529174804688