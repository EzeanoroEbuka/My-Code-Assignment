import random


def create_a_list_of_ten_numbers():
    random.seed(10)
    list_of_ten = []
    for number in range(10):
        generated_number = random.randrange(1, 50)
        list_of_ten.append(generated_number)

    return list_of_ten


def get_length_of_list(collection):
    length_increment = 0
    for _ in collection:
        length_increment += 1

    return length_increment


def sum_of_even_index(collection):
    sum_of_even = 0
    for number in range(0, get_length_of_list(collection), 2):
        sum_of_even += collection[number]

    return sum_of_even


def sum_of_odd_index(collection):
    sum_of_odd = 0
    for number in range(1, get_length_of_list(collection), 2):
        sum_of_odd += collection[number]

    return sum_of_odd


def product_of_every_third_positions(collection):
    product_of_third_position = 1
    for number in range(3, get_length_of_list(collection), 3):
        product_of_third_position *= collection[number]

    return product_of_third_position


def average_of_element_in_collection(collection):
    sum_up = 0
    average = 0
    for number in range(get_length_of_list(collection)):
        sum_up += collection[number]
        average = sum_up / get_length_of_list(collection)

    return average


def largest_of_the_list(collection):
    largest = 0
    for number in collection:
        if number > largest:
            largest = number
    return largest


def smallest_of_the_list(collection):
    smallest = collection[0]
    for number in collection:
        if number < smallest:
            smallest = number
    return smallest


def count_strings(collection):
    for string in collection:
        for _ in string:
            if get_length_of_list(string) >= 2 and string[0] == string[-1]:
                return string


def sequential_list_one_to_fifteen():
    list_of_fifteen = []
    for number in range(1, 16):
        list_of_fifteen.append(number)

    return list_of_fifteen


def duplicate_of_sequential_list_one_to_fifteen():
    new_list = sequential_list_one_to_fifteen()
    for number in range(1, 16):
        new_list.append(number)

    return new_list


def eliminate_duplicated_element():
    old_list = duplicate_of_sequential_list_one_to_fifteen()
    new_numbers = set(old_list)

    return new_numbers


def add_third_element_in_a_designated_list(collection):
    sum_up = 0
    for number in range(2, get_length_of_list(collection), 3):
        sum_up += collection[number]
    return sum_up


def add_first_middle_and_last_element(collection):
    EVEN = 2
    length = get_length_of_list(collection)
    if get_length_of_list(collection) % 2 == 1:
        middle_index = length // EVEN
        sum_up = collection[0] + collection[-1] + collection[middle_index]
    else:
        index = collection[(length // EVEN)]
        middle_index_half = collection[(length // EVEN) - 1]
        middle_element = (index + middle_index_half) / EVEN
        sum_up = collection[0] + collection[-1] + middle_element

    return sum_up


def collect_and_store_without_duplicates(collection):
    new_collection = set(collection)

    return new_collection


def sum_of_element_in_collection(collection):
    sum = 0
    for number in collection:
        sum += number
    return sum


def remove_item(collection, item):
    for number in collection:
        if number == item:
            collection.remove(number)
            return number
    if item not in collection:
        return None


def find_intersection(collection_1, collection_2):
    new_collection = set()
    for number in collection_1:
        for number2 in collection_2:
            if number == number2:
                new_collection.add(number)
    return new_collection


def create_union(first_collection, second_collection):
    union = first_collection | second_collection
    return union


def check_for_subset(first_collection, second_collection):
    count = 0
    for number in first_collection:
        if number in second_collection:
            count += 1
    if count == get_length_of_list(first_collection):
        return True
    else:
        return False


def remove_element_in_set(collection):
    collection.clear()
    return collection


def maximum_and_minimum(collection):
    maximum = 0
    minimum = min(collection)
    for number in collection:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return maximum, minimum


def length_of_set(collection):
    length = 0
    for number in collection:
        length += 1
    return length


def create_empty_tuple():
    new_tuple = ()
    return new_tuple


def add_number_into_tuple():
    new_tuple = ()
    for number in range(1, 21):
        new_tuple += (number,)
    return new_tuple


def sum_of_odd_index_of_tuple(collection):
    sum_of_odd = 0
    for number in range(1, get_length_of_list(collection), 2):
        sum_of_odd += collection[number]

    return sum_of_odd


def sum_of_even_index_of_tuple(collection):
    sum_of_even = 0
    for number in range(0, get_length_of_list(collection), 2):
        sum_of_even += collection[number]

    return sum_of_even


def sum_up_smallest_and_largest(collection):
    largest = 0
    smallest = min(collection)
    sum_up = 0
    for number in collection:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    sum_up = smallest + largest

    return sum_up


def unpack_first_five_element_of_tuple(collection):
    element_one, element_two, element_three, element_four, element_five, *others = collection

    return element_one, element_two, element_three, element_four, element_five


def create_a_dictionary():
    new_dictionary = {}
    return new_dictionary


student_names = ["MUSA", "ADE", "KIM", "JANET", "JOSHUA", "ENIOLA", "WALE", "TIMMY", "REX", "LEX"]
student_age = [22, 33, 11, 14, 21, 16, 19, 24, 18, 13]


def populate_dictionary(names, age):
    dictionary = create_a_dictionary()
    for item in range(get_length_of_list(names)):
        dictionary.update({names[item]: age[item]})

    return dictionary


def sort_and_display_dictionary_by_key(key, value):
    dictionary = populate_dictionary(key, value)
    sorted_dictionary = {}
    sorted_dictionary = dict(sorted(dictionary.items()))

    return sorted_dictionary

print(sort_and_display_dictionary_by_key(student_names, student_age))


def sort_and_display_dictionary_by_values(key, value):
    dictionary = populate_dictionary(key, value)
    sorted_dictionary = {}
    sorted_dictionary = dict(sorted(dictionary.items()value))

    return sorted_dictionary