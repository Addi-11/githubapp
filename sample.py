def mean_of_numbers3(num_list):
    numbers_sum = 0
    numbers_count = 0

    for num_str in num_list:
        try:
            num = float(num_str)
            numbers_sum += num
            numbers_count += 1
        except ValueError:
            pass

    if numbers_count > 0:
        return numbers_sum / numbers_count
    else:
        return 0 
