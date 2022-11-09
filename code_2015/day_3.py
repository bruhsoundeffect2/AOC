def get_input() -> str:
    with open('day_3_input.txt', 'r') as f:
        txt = f.readlines()
    return txt[0]


def get_direction(dirc: str) -> tuple:
    if dirc == '^': 
        return (0,1)
    elif dirc == '>':
        return (1,0)
    elif dirc == 'v':
        return (0,-1)
    elif dirc == '<':
        return (-1,0)


def give_present(hit_houses: dict, directions: str, place: tuple) -> dict:
    for dirc in directions:
        place = tuple(map(sum,zip(place,get_direction(dirc))))
        if place in hit_houses:
            hit_houses[place] += 1
        else:
            hit_houses[place] = 1
    return hit_houses


def part_1() -> int:
    hit_houses = dict()
    directions = get_input()
    place = (0,0)
    hit_houses[place] = 1 
    give_present(hit_houses, directions, place)
    return len(hit_houses)


def part_2() -> int:
    hit_houses = dict()
    directions = get_input()
    place = (0,0)
    first_dir = directions[1::2]
    second_dir = directions[::2]
    hit_houses[place] = 2
    first_hit_houses = give_present(hit_houses, first_dir, place)
    second_hit_houses = give_present(hit_houses, second_dir, place)
    combined = {**first_hit_houses, **second_hit_houses}
    return len(combined)


print(f"--- Part1 --- \nTotal number of houses that got at least one present: {part_1()}")
print(f"--- Part 2 --- \nTotal number of houses that got at least one present: {part_1()}")
