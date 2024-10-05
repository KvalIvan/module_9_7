def is_prime(func):
    def wrapper(*args):
        result_ = func(*args)
        if result_ <= 1:
            print('Составное')
        for i in range(len(args), int(result_**0.5) + 1):
            if result_ % i == 0:
                print('Составное')
            else:
                print('Простое')
        return result_
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_


result = sum_three(2, 3, 6)
print(result)