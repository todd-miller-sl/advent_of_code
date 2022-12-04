import os


def main():
    data = read_file()
    elf_totals = sorted(parse_input(data), reverse=True)
    print(f'Max Calories being carried: {max(elf_totals)}')
    print(f'Calories carried by top 3 elves: {sum(elf_totals[:3])}')


def read_file():
    with open('./day_01/input.txt', 'r') as inputFile:
        data = inputFile.readlines()
    return data


def parse_input(data):
    # approaches
    # 1. list of list approaches
    # 2. two lists - 1 of calories, 1 of indices
    # 3. maximum between two indices
    # 4. run a counter until a break, then reset the counter

    elf_totals = []
    calories = 0
    for line in data:
        val = line.split('\n')[0]
        if val:
            calories += int(val)
        else:
            elf_totals.append(calories)
            calories = 0

    return elf_totals


if __name__ == "__main__":
    print(os.getcwd())
    main()
