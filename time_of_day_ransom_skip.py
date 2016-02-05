# Athors:  Ransom V and Skip A
# Written 10/1/15
# References: Google, stackoverflow.com
# Usage:  Enter 'python3 time_of_day_ransom_skip.py'.
# Program will output the number of commits by hour of day.

from emails_ransom_skip import get_filename
from collections import Counter, OrderedDict


def line_scan(f):
    """
    Function scans through the file one line at a time and returns only the lines that start with 'From '

    Arguments - f is the location of a file to read of type _io.TextIOWrapper
    Returns - A list containing commit hour field from all lines that start with 'From' (not 'From:')
    """

    commit_hour = []

    for line in f:
        if "From " in line:
            split_line = line.split()
            if split_line[0] != 'From':  # insures we only include lines that BEGIN with 'From'
                pass
            else:
                b = split_line[5]
                commit_hour.append(b[:2])
    return commit_hour


def counted_hours(hours_with_commits):
    """
    Function checks a list of all commit hours and returns a sorted dictionary that lists
    the number of commits per hour.

    Arguments - hours_with_commits - A list containing the hour each commit was made
    Returns - sorted_dict - A tuple containing the hour and the number of commits that occured during that hour

    This function works by counting the number of times a given hour appears in the input arguments
    commits_by_hour.  It uses methods Counter and OrderedDict from the collections library.
    """
    local_dict = Counter(hours_with_commits)
    sorted_dict = OrderedDict(sorted(local_dict.items()))
    return sorted_dict


def assert_line_scan():
    """ Function to perform assertion on line_scan using a local test files 'one_good_line.txt'
    and one_good_one_bad.  These files must be in the same directory as this script.  Script will
    fail with an assertion error if lin_scan() function isn't working or test files aren't present.

    Arguments - None
    Returns - None
    """

    file1 = 'one_good_line.txt'
    file2 = 'one_good_one_bad.txt'
    f = open(file1)
    a = line_scan(f)
    assert a == ['09']
    f.close()

    f = open(file2)
    a = line_scan(f)
    assert a == ['08']
    f.close()


##### End of non-main() functions #####


def main():
    """Takes a user specified file and returns the number of total commits per
    hour in the day.  Hours are sorted ascending.

    Usage:  python3 time_of_day_ransom_skip.py

    """

    f = get_filename()

    assert_line_scan()     # Assertions for line_scan()

    output1 = line_scan(f)

    sorted_dict = counted_hours(['09'])             # Part of assertion for counted_hours()
    assert sorted_dict == OrderedDict([('09', 1)])  # Assertion for counted_hours()
    sorted_dict = counted_hours(output1)
    for k, v in sorted_dict.items():  # Printing items in sorted_dict neatly
        print(k, v)


main()
