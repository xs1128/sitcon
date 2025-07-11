from add import add


def main():
    print(add(1,4))


if __name__ == "__main__":
    main()

# Sol 3
# def perfect_num(inp: int)->bool:
#     divisors = [n for n in range(1, inp) if inp % n == 0]
#     return (sum(divisors) == inp)


# for i in range(1, 191561942608236107294793378084303638130997321548169216):
#     print(i) if perfect_num(i) else None


# Sol 2
# def odd_sum(*args):
#     return sum(list(filter(lambda x : x % 2 == 1, args)))


# print(odd_sum(1))


# Sol 1
# def add(a: int=0, b: int=0)->int:
#     return a + b


# print(add(1, 2))