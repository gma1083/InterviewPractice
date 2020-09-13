''' Uniform Consecutive Sub Groups '''

# Given an array of unsorted integers, and an integer W:
# Determine if you can group the integers in the array according to the following constraints:
# 1) Each group contains W elements.
# 2) Each group consists of consecutive integer elements.
# 3) Return TRUE if this is can be done, return FALSE If it can not.

def sub_groups_possible(array, group_size):
    ''' Checks for consecutive subgroup possibilities '''

    # Initial check based in array size
    if len(array) % group_size != 0:
        return False

    # Define common values from input
    sorted_array = array
    sorted_array.sort()
    array_size = len(array)
    number_of_groups = array_size / group_size

    # Iterate through the input array one time for each sub group.
    # On each iteration, remove smallest value and all consecutive values until sub group is filled.
    current_group_number = 1
    while current_group_number <= number_of_groups:
        current_group_size = 0
        while current_group_size < group_size:
            smallest_value = min(sorted_array)
            for number in range(smallest_value, smallest_value + group_size):
                try:
                    sorted_array.remove(number)
                    current_group_size += 1
                except ValueError:
                    return False
        current_group_number += 1
    return True



###### peak_finder() Tests #####
class BColors:
    ''' Color Definitions For Testing Output '''

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(BColors.OKBLUE + "-------- peak_finder().py Tests --------" + BColors.ENDC)

# Test 1 - Empty List
# Expected Return = True
grouping_possible = sub_groups_possible([], 2)
print(("Test #1 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #1 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is True])

# Test 2 - Single Element, Group Size = 1
# Expected Return = True
grouping_possible = sub_groups_possible([1], 1)
print(("Test #2 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #2 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is True])

# Test 3 - Single Element, Group Size = 2
# Expected Return = False
grouping_possible = sub_groups_possible([1], 2)
print(("Test #3 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #3 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is False])

# Test 4 - Two Elements Not Equal
# Expected Return = True
grouping_possible = sub_groups_possible([1, 2], 2)
print(("Test #4 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #4 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is True])

# Test 5 - Multiple Elements, No Duplicates
# Expected Return = True
grouping_possible = sub_groups_possible([1, 2, 3, 4], 2)
print(("Test #5 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #5 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is True])

# Test 6 - Multiple Elements, With Duplicates
# Expected Return = True
grouping_possible = sub_groups_possible([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5)
print(("Test #6 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #6 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is True])

# Test 7 - Input Size % Group Size Doesnt Equal 0
# Expected Return = True
grouping_possible = sub_groups_possible([1, 2, 3, 4, 5, 5, 5, 6, 7, 8], 5)
print(("Test #7 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #7 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is False])

# Test 8 - Input Size % Group Size Doesnt Equal 0
# Expected Return = True
grouping_possible = sub_groups_possible([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 6)
print(("Test #8 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #8 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[grouping_possible is True])
