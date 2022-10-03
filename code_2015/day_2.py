def get_input():
    with open('day_2_input.txt', 'r') as f:
        txt = f.readlines()
    return txt


def present_info(present):
    pres = present.strip().split('x')
    return [int(num) for num in pres]


def total_present_resources(presents):
    calculate_paper = lambda present: (2*present[0]*present[1] + 2*present[1]*present[2] + 2*present[0]*present[2]) + min(present[0]*present[1], present[1]*present[2], present[0]*present[2])
    calculate_ribbon = lambda present: min(2*present[0]+2*present[1], 2*present[1]+2*present[2], 2*present[0]+2*present[2]) + present[0]*present[1]*present[2]
    
    parsed_presents = [present_info(present) for present in presents]

    all_paper = [calculate_paper(present) for present in parsed_presents]
    all_ribbon = [calculate_ribbon(present) for present in parsed_presents]

    return sum(all_paper), sum(all_ribbon)


def main():
    presents = get_input()
    total_paper, total_ribbon = total_present_resources(presents)
    print(f"Total amount of paper needed is {total_paper} \nTotal amount of ribbon needed is {total_ribbon}")


if __name__ == '__main__':
    main()