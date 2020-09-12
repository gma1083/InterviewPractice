""" Peak Finder """

# Given an input array, return an array containing the indices of all peaks from the original array.
# Peak element is the element which is greater than or equal to its neighbors.

def find_peaks(array):
    ''' Given an array, find its peaks '''

    array_size = len(array)
    peaks = []

    # If array is empty, there is no peak
    if array_size == 0:
        return None

    # If array has only one element, that element is a peak
    elif array_size == 1:
        peaks.append(0)

    # If array has only two elements, the greater element is a peak
    elif array_size == 2:
        if array[0] > array[1]:
            peaks.append(0)
        elif array[1] > array[0]:
            peaks.append(1)
        else:
            peaks.extend((0, 1))

    # If array has more than two elements, loop through array and find peaks
    else:
        if array[0] >= array[1]:
            peaks.append(0)
        if array[-1] >= array[-2]:
            peaks.append(array_size-1)
        for index in range(1, array_size - 1):
            if array[index-1] <= array[index] >= array[index+1]:
                peaks.append(index)

    peaks.sort()
    return peaks

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
peaks_found = find_peaks([])
print(("Test #1 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #1 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found is None])

# Test 2 - Single Element
peaks_found = find_peaks([1])
print(("Test #2 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #2 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [0]])

# Test 3 - Two Elements Not Equal
peaks_found = find_peaks([1, 2])
print(("Test #3 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #3 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [1]])

# Test 4 - Two Elements Equal
peaks_found = find_peaks([2, 2])
print(("Test #4 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #4 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [0, 1]])

# Test 5 - Multiple Elements Equal
peaks_found = find_peaks([2, 2, 2, 2, 2, 2])
print(("Test #5 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #5 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [0, 1, 2, 3, 4, 5]])

#Test 6 - Multiple Elements Not Equal, Sorted
peaks_found = find_peaks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(("Test #6 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #6 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [9]])

# Test 7 - Multiple Elements Not Equal, Reverse Sorted
peaks_found = find_peaks([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(("Test #7 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #7 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [0]])

# Test 8 - Multiple Elements Not Equal, Random
peaks_found = find_peaks([1, 2, 4, 3, 2, 2, 2, 8, 0, 10])
print(("Test #8 - " + BColors.FAIL + "Fail" + BColors.ENDC, \
    "Test #8 - " + BColors.OKGREEN + "Pass" + BColors.ENDC)[peaks_found == [2, 5, 7, 9]])
