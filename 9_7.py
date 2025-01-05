def is_prime(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)

        if result_func > 1:
            for i in range(2, int(result_func ** 0.5) + 1):
                if result_func % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result_func
    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three

result = sum_three(2, 3, 6)
print(result)