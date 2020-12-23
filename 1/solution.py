def main():
    data = set(load_data())

    for n in data:
        compliment = 2020 - n
        if compliment in data:
            print(f'Answer: {n*compliment}')
            break


def load_data():
    with open('input') as f:
        data = f.read()
    return [int(l.strip()) for l in data.splitlines()]


if __name__ == '__main__':
    main()
