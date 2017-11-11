# Michael Benos (mtb9ps)
# I referenced http://stackoverflow.com/questions/5305164/get-difference-from-two-lists-in-python to learn how to remove elements that one list has in common with another list
# I referenced https://wiki.python.org/moin/HowTo/Sorting to learn how to sort a list

import urllib.request

def instructors(department):
    url = urllib.request.urlopen("http://stardock.cs.virginia.edu/louslist/Courses/view/" + department)

    list_of_instructors = []

    for line in url:
        decoded = line.decode("UTF-8").strip().split(";")
        if decoded[4] not in list_of_instructors:
            list_of_instructors.append(decoded[4])
    list_of_instructors = sorted(list_of_instructors)
    return list_of_instructors

def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    url = urllib.request.urlopen("http://stardock.cs.virginia.edu/louslist/Courses/view/" + dept_name)

    class_set = []

    for line in url:
        decoded = line.decode("UTF-8").strip().split(";")
        class_set.append(decoded)

    list_to_remove = []

    for i in class_set:
        if has_seats_available and int(i[15]) >= int(i[16]):
            list_to_remove.append(i)
        if level is not None and (float(level) // 1000) != (float(i[1]) // 1000):
            list_to_remove.append(i)
        if not_before is not None and int(i[12]) < not_before:
            list_to_remove.append(i)
        if not_after is not None and int(i[12]) > not_after:
            list_to_remove.append(i)

    class_set = [j for j in class_set if j not in list_to_remove]

    return class_set