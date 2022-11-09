import hashlib
import itertools
import datetime


def smallest_number():
    word = 'ckczppom' 
    result = hashlib.md5(word.encode())
    count = 0 
    while result.hexdigest()[:5] != '00000':
        count += 1
        result = hashlib.md5(f"{word}{count}".encode()) 
    print(count)


def smallest_number_part2():
    start = datetime.datetime.timestamp(datetime.datetime.utcnow())
    word = 'ckczppom' 
    result = hashlib.md5(word.encode())
    count = 0 
    while result.hexdigest()[:6] != '000000':
        count += 1
        result = hashlib.md5(f"{word}{count}".encode())
    end = datetime.datetime.timestamp(datetime.datetime.utcnow())
    print(f"\tSmallest number found: {count}")
    print(f"\tTime to complete: {end - start}")


def smallest_number_part2_itertools():
    start = datetime.datetime.timestamp(datetime.datetime.utcnow())
    word = 'ckczppom' 
    result = hashlib.md5(word.encode())
    final = 0 
    for count in itertools.count():
        result = hashlib.md5(f"{word}{count}".encode())
        if result.hexdigest()[:6] == '000000':
            final = count
            break 
    end = datetime.datetime.timestamp(datetime.datetime.utcnow())
    print(f"\tSmallest number found {final}")
    print(f"\tTime to complete: {end - start}")


print("--- Part 2 ---")
print("While loop implementation")
smallest_number_part2()
print("Itertools implementation")
smallest_number_part2_itertools()