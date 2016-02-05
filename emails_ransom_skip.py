# Authors:  Ransom V and Skip A
# Written 9/25/15
# References: Google, StackOverFlow
# Program to read in an email file and output the user with the most number of commits
# Program does not include commits per hour


def get_filename():
    """
    Prompts user for a filename and opens local file in pwd.  There is no checking for presence of file.

    Arguments - none
    returns - f - The location of a file to read of type _io.TextIOWrapper
    """

    filename = input("Input filename:  ")
    f = open(filename, 'r')
    return f


def read_file(file_pointer):
    """
    Reads file one line at a time and creates lst2 which is a list of files containing
    lines starting with 'From '.

    Arguments - file_pointer - The Address of a file to read of type _io.TextIOWrapper
    Returns - a list of lists containing all the from lines from the file
    """

    lst2 = []

    for line in file_pointer:
        lst1 = line.split()
        if lst1 == []:
            continue
        else:
            #for words in lst1:
            if lst1[0] == "From":
                lst2.append(lst1[1:])
    # print("lst2 in read_file function is:  ", lst2)
    return lst2


def remove_unique_address(lst):
    """
    Takes a list of addresses with duplicates and extracts to another list.

    Arguments - lst - A list of lists from read_file()
    Returns - addresses - A list type of unique address
    """

    addresses = []
    for x in range(len(lst)):
        if lst[x][0] in addresses:
            continue
        else:
            addresses.append(lst[x][0])

    return addresses


def count_(lst, unique):
    """
    Takes in a list of unique names and a list of all commit lines and returns a list of commits per user.

    Arguments -
    lst - A list of lists.  Each list contains address as first element
    unique - A list of unique names

    Returns - commits_user - A list of tuples with elements count and email address
    """

    commits_user = list()  # list variable for storing a list of tuples

    for name in unique:
        count = 0  # re-init the counter to 0 for each element of the unique list
        for index, elem in enumerate(lst):
            if name == elem[0]:
                count += 1
        commits_user.append((count, name))
    return(commits_user)


def sort_reverse(lst_of_tups):
    """
    Takes in an unsorted list of tuples and returns a list sorted by number of commits

    Arguments - list of tuples from count function

    Returns - sorted list  of tuples keying on the # of commits value
    list sorted from most to least commits
    """

    reversed_tups = sorted(lst_of_tups, reverse=True)
    return reversed_tups

# End of non-main functions


def main():
    # get_filename() assertions will go here
    f = get_filename()

    raw_commits = read_file(f)

    unique_list = remove_unique_address(raw_commits)

    commits_per_user = count_(raw_commits, unique_list)

    reversed = sort_reverse(commits_per_user)
    print("Most commits is: {} - {} ".format(reversed[0][0], reversed[0][1]))

if __name__ == '__main__':
    main()
