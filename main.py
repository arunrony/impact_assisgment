missed_grad_count = 0


def find_miss_ceremony(length,
                       miss_left,
                       continue_absent_allow,
                       path):
    global missed_grad_count

    if length == 0:
        print(path)
        if path[-1] == 0:
            missed_grad_count += 1
        return 1

    if miss_left > 0:
        miss_path = find_miss_ceremony(length - 1, miss_left - 1, continue_absent_allow, path + [0])
    else:
        miss_path = 0

    no_miss_path = find_miss_ceremony(length - 1, continue_absent_allow, continue_absent_allow, path + [1])

    print(f'{length = } {miss_left = } {miss_path = } {no_miss_path = }')

    return miss_path + no_miss_path


length = 5
continue_absent_allow = 3

data = find_miss_ceremony(length,
                          continue_absent_allow,
                          continue_absent_allow,
                          [])

print(data, missed_grad_count)
