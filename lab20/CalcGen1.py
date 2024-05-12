# Создать ф-цию генератор
# Ф-ция-генератор должна возвращать последвательность Фиббоначи


# parameters: lenght sequence, previos num (default 0), next num (default 1)
def gen_func_Fibb_seq(seq_len : int, prev : int, next : int):

    yield 0 # first num
    if seq_len > 0:
        for it in range(0, seq_len):
            yield next
            tmp = next
            next += prev
            prev = tmp


def main():
    for num in gen_func_Fibb_seq(20, 0, 1):
        print(num)


if __name__ == "__main__":
    main()
