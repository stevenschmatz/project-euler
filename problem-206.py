from math import sqrt

raw_number = '1_2_3_4_5_6_7_8_9_0'


def is_answer(n):
    n_str = str(n)
    for i in range(0, len(raw_number), 2):
        if raw_number[i] != n_str[i]:
            return False
    else:
        return True


def main():
    max_number = int(raw_number.replace('_','9'))
    min_number = int(raw_number.replace('_','0'))

    for i in range(int(sqrt(min_number)), int(sqrt(max_number))):
        if is_answer(i ** 2):
            print(i)
            return


if __name__ == "__main__":
    main()
