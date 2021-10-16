import random
from math import gcd


def generate_rand():
    # n = input("Enter random long int: ")
    # n = int(n)
    n = 1000
    # n = 10
    arr_nums = []
    for i in range(n + 1):
        arr_nums.append(i)
    arr_nums[1] = 0
    i = 2
    while i ** 2 <= n:
        if arr_nums[i] != 0:
            j = i ** 2
            while j <=n:
                arr_nums[j] = 0
                j += i
        i += 1
    arr_nums = set(arr_nums)
    arr_nums.remove(0)
    arr_nums = list(arr_nums)
    arr_nums.sort()
    first_index = random.randint(0, len(arr_nums)-1)
    second_index = random.randint(0, len(arr_nums) - 1)
    first_num = arr_nums[first_index]
    while True:
        second_num = arr_nums[second_index]
        if second_num == first_num:
            second_index = random.randint(0, len(arr_nums) - 1)
            continue
        else:
            break
    print(f"Массив простых чисел: {arr_nums}\nДлина массива: {len(arr_nums)}\n-----------------------------------"
          f"\nПервое простое число: {first_num}\nВторое простое число: {second_num}")
    return arr_nums, first_num, second_num


def coprime(a, b):
    return gcd(a, b) == 1


if __name__ == '__main__':
    arr, first, second = generate_rand()
    module = first * second
    print(f"-----------------------------------\nmodule = {module}")
    eiler_func = (first - 1) * (second - 1)
    print(f"eiler_func = {eiler_func}")
    num3 = random.choice(arr)
    print(f"num3 = {num3}")
    while True:
        if not (1 < num3 < eiler_func) or not coprime(num3, eiler_func):
            print("change num3")
            arr.remove(num3)
            num3 = random.choice(arr)
            print(f"num3 = {num3}")
        else:
            break
    for exponent in range(3, eiler_func, 2):
        if exponent * num3 % eiler_func == 1:
            break
    print(f"Экспонента = {exponent}")
    n = int(input("Введите число: "))
    cr = (n ** num3) % module
    print(f"cr = {cr}")
    decr = (cr ** exponent) % module
    print(f"decr = {decr}")
