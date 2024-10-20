QUESTION 1- Write a code to reverse ' string ' ?

SOLUTION1 -
def reverse_string(s):
    return s[::-1]

# Example usage:
string = "hello"
reversed_string = reverse_string(string)
print(reversed_string)  # Output: "olleh"



QUESTION 2- Write ' code to count the number of vowel in ' string' ?

SOLUTION 2-
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
string = "Hello World"
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")  # Output: 3



QUESTION 3- Write ' code to check if ' given string is ' palindrome or not ?

SOLUTION 3-
def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase to ignore case sensitivity
    s = ''.join(filter(str.isalnum, s))  # Remove any non-alphanumeric characters
    return s == s[::-1]

# Example usage:
string = "A man, a plan, a canal, Panama"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



QUESTION 4- Write ' code to check if two given string 'are 'anagrams of each other ?

SOLUTION 4-
def are_anagrams(str1, str2):
    # Remove any whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")



QUESTION 5- Write ' code to find all occurrence of a given substring within another string ?

SOLUTION -5-
def find_all_occurrences(string, substring):
    occurrences = []
    start = 0

    while True:
        # Find the index of the next occurrence of the substring
        index = string.find(substring, start)
        
        if index == -1:
            break  # Exit if no more occurrences are found
        
        occurrences.append(index)
        start = index + 1  # Move start to just after the current found index

    return occurrences

# Example usage:
string = "abracadabra"
substring = "abra"
positions = find_all_occurrences(string, substring)

if positions:
    print(f"'{substring}' found at positions: {positions}")
else:
    print(f"'{substring}' not found in the string.")





QUESTION 6- Write a code to perform basic string compression using the count of repeated characters ?

SOLUTION -6-
def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    # Loop through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Increment the count if the current character is the same as the previous one
        else:
            # Append the previous character and its count to the compressed list
            compressed.append(s[i - 1] + str(count) if count > 1 else s[i - 1])
            count = 1  # Reset count

    # Append the last character and its count
    compressed.append(s[-1] + str(count) if count > 1 else s[-1])

    # Join the list into a string
    return ''.join(compressed)

# Example usage:
string = "aaabccdddde"
compressed_string = compress_string(string)
print("Compressed string:", compressed_string)




QUESTION 7-  Write a code to determine if ' string has all unique characters ?

SOLUTION 7-
def has_unique_characters(s):
    # Use a set to track characters we have seen
    seen = set()
    
    for char in s:
        if char in seen:
            return False  # If character is already seen, return False
        seen.add(char)
    
    return True  # If no duplicates, return True

# Example usage:
string = "abcdefg"
if has_unique_characters(string):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")




QUESTION 8- Write a code to convert a given string to uppercase  or lowercase ?

SOLUTION 8-
def convert_string(s, to_upper=True):
    if to_upper:
        return s.upper()  # Convert to uppercase
    else:
        return s.lower()  # Convert to lowercase

# Example usage:
string = "Hello World"

uppercase_string = convert_string(string, to_upper=True)
lowercase_string = convert_string(string, to_upper=False)

print("Uppercase:", uppercase_string)  # Output: "HELLO WORLD"
print("Lowercase:", lowercase_string)  # Output: "hello world"




QUESTION 9- Write a code to count the number of words in a string ?

SOLUTION 9-
def count_words(s):
    # Split the string by whitespace to get a list of words
    words = s.split()
    return len(words)

# Example usage:
string = "Hello, this is a sample string."
word_count = count_words(string)

print(f"Number of words: {word_count}")





QUESTION 10- Write a code to concatenate two strings without using the + operator  ?

SOLUTION 10-
def concatenate_strings(str1, str2):
    # Using the join() method
    return ''.join([str1, str2])

# Example usage:
string1 = "Hello"
string2 = "World"
result = concatenate_strings(string1, string2)

print("Concatenated String:", result)





QUESTION 11- Write a code to remove all occurence of a specific element from a list ?

SOLUTION 11-
def remove_occurrences(lst, element):
    # Create a new list with all elements except the specified element
    return [item for item in lst if item != element]

# Example usage:
original_list = [1, 2, 3, 4, 2, 5, 2, 6]
element_to_remove = 2
new_list = remove_occurrences(original_list, element_to_remove)

print("Original List:", original_list)
print("List after removing all occurrences of", element_to_remove, ":", new_list)




QUESTION 12- implement a code to find the second largest number in a given list of integer ?

SOLUTION 12-
def find_second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements for a second largest
    
    first = second = float('-inf')  # Initialize first and second largest

    for num in nums:
        if num > first:
            second = first  # Update second to be the old first
            first = num  # Update first to the new largest
        elif first > num > second:
            second = num  # Update second if num is between first and second

    return second if second != float('-inf') else None  # Return second largest or None

# Example usage:
numbers = [12, 35, 1, 10, 34, 1]
second_largest = find_second_largest(numbers)

if second_largest is not None:
    print("The second largest number is:", second_largest)
else:
    print("There is no second largest number.")




QUESTION 13- Create a code to count the occurence of each element in a list and return a dictionary
 with element as key  and their count as value ?

SOLUTION 13-
def count_occurrences(lst):
    occurrence_dict = {}
    
    for item in lst:
        if item in occurrence_dict:
            occurrence_dict[item] += 1  # Increment count if item exists
        else:
            occurrence_dict[item] = 1  # Initialize count to 1 for new item
            
    return occurrence_dict

# Example usage:
elements = [1, 2, 2, 3, 1, 4, 3, 5, 1]
occurrences = count_occurrences(elements)

print("Occurrences of each element:", occurrences)




QUESTION 14- Write a code to reverse a list in-place without using any
 built-in reverse function ?

SOLUTION 14-
def reverse_list(lst):
    left, right = 0, len(lst) - 1  # Initialize pointers

    while left < right:
        # Swap elements at left and right pointers
        lst[left], lst[right] = lst[right], lst[left]
        left += 1  # Move left pointer to the right
        right -= 1  # Move right pointer to the left

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

reverse_list(my_list)
print("Reversed List:", my_list)




QUESTION 15- implement a code to find and remove duplicate from a list while preserving the original order of elements?

SOLUTION 15-
def remove_duplicates(lst):
    seen = set()  # Set to keep track of seen elements
    unique_list = []  # List to store the result

    for item in lst:
        if item not in seen:
            seen.add(item)  # Add item to seen set
            unique_list.append(item)  # Add item to unique list

    return unique_list

# Example usage:
original_list = [1, 2, 3, 2, 4, 3, 5, 1]
result = remove_duplicates(original_list)

print("Original List:", original_list)
print("List after removing duplicates:", result)




QUESTION 16- Create a code to check if a given list is sorted (either in ascending or descending order) or not  ?


SOLUTION 16-
def is_sorted(lst):
    if len(lst) < 2:
        return True  # A list with 0 or 1 element is considered sorted

    ascending = True
    descending = True

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            ascending = False  # If we find an element that is less than the previous one
        if lst[i] > lst[i - 1]:
            descending = False  # If we find an element that is greater than the previous one

    return ascending, descending

# Example usage:
sample_list1 = [1, 2, 3, 4, 5]      # Sorted in ascending order
sample_list2 = [5, 4, 3, 2, 1]      # Sorted in descending order
sample_list3 = [1, 3, 2, 4, 5]      # Not sorted

is_sorted1 = is_sorted(sample_list1)
is_sorted2 = is_sorted(sample_list2)
is_sorted3 = is_sorted(sample_list3)

print(f"Sample List 1 is sorted (Ascending, Descending): {is_sorted1}")
print(f"Sample List 2 is sorted (Ascending, Descending): {is_sorted2}")
print(f"Sample List 3 is sorted (Ascending, Descending): {is_sorted3}")




QUESTION 17 - Write a code to merge two sorted lists into a single sorted list ?

SOLUTION 17 -
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0  # Pointers for list1 and list2

    # Traverse both lists and append smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If there are remaining elements in list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining elements in list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Example usage:
sorted_list1 = [1, 3, 5, 7]
sorted_list2 = [2, 4, 6, 8]

merged_result = merge_sorted_lists(sorted_list1, sorted_list2)
print("Merged Sorted List:", merged_result)




QUESTION 18- implement a code to find the intersection of two given list ?

SOLUTION 18-
def find_intersection(list1, list2):
    # Use a set to store elements of list1 for efficient look-up
    set1 = set(list1)
    intersection = []

    # Iterate through list2 and check if the element is in set1
    for item in list2:
        if item in set1:
            intersection.append(item)

    return intersection

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = find_intersection(list1, list2)
print("Intersection of the two lists:", result)




QUESTION 19- create a code to find the union of two list without duplicates ?

SOLUTION 19-
def find_union(list1, list2):
    # Use a set to store unique elements
    union_set = set(list1)  # Start with elements from list1
    union_set.update(list2)  # Add elements from list2

    return list(union_set)  # Convert the set back to a list

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = find_union(list1, list2)
print("Union of the two lists without duplicates:", result)




QUESTION 20- Write a code to shuffle a given list randomly without using any built-in shuffle function .

SOLUTION 20-
import random

def shuffle_list(lst):
    # Create a copy of the original list
    shuffled_list = lst[:]
    n = len(shuffled_list)

    # Shuffle using Fisher-Yates algorithm
    for i in range(n - 1, 0, -1):  # Start from the end of the list
        j = random.randint(0, i)  # Get a random index from 0 to i
        # Swap the current element with the randomly chosen element
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

    return shuffled_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)

print("Original List:", original_list)
print("Shuffled List:", shuffled_result)




QUESTION 21- Write a code that takes two tuples as input and returns a new tuple containing elements that are 
common to both input tuple ?

SOLUTION 21-
def common_elements(tuple1, tuple2):
    # Use a set to find common elements
    common_set = set(tuple1) & set(tuple2)  # Intersection of both sets

    # Convert the set back to a tuple and return
    return tuple(common_set)

# Example usage:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

result = common_elements(tuple1, tuple2)
print("Common elements in both tuples:", result)




QUESTION 22- Create a code that prompt the user to enter two sets of integer seprated by 
commas. Then print the  intersection of these two sets ?

SOLUTION 22-
def get_set_from_input(prompt):
    # Prompt the user for input and split by commas
    user_input = input(prompt)
    # Convert the input string into a set of integers
    return set(int(x.strip()) for x in user_input.split(','))

def main():
    # Get two sets from user input
    set1 = get_set_from_input("Enter the first set of integers (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of integers (separated by commas): ")

    # Find the intersection of the two sets
    intersection = set1 & set2  # or use set1.intersection(set2)

    # Print the result
    print("The intersection of the two sets is:", intersection)

# Run the program
if __name__ == "__main__":
    main()




QUESTION 23- Write a code to concatenate two tuples. The function should take two tuples as input and return a new 
tuple containing elements from both input tuples ?

SOLUTION 23-
def concatenate_tuples(tuple1, tuple2):
    # Concatenate the two tuples using the + operator
    concatenated_tuple = tuple1 + tuple2
    return concatenated_tuple

# Example usage:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = concatenate_tuples(tuple1, tuple2)
print("Concatenated Tuple:", result)




QUESTION 24- Develop a code  that prompts the user to input two sets of strings. Then print the elements that are
present in the first set but not in the second set ?

SOLUTION 24-
def get_set_from_input(prompt):
    # Prompt the user for input and split by commas
    user_input = input(prompt)
    # Convert the input string into a set of strings
    return set(x.strip() for x in user_input.split(','))

def main():
    # Get two sets from user input
    set1 = get_set_from_input("Enter the first set of strings (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of strings (separated by commas): ")

    # Find elements in the first set but not in the second set
    difference = set1 - set2  # or use set1.difference(set2)

    # Print the result
    print("Elements in the first set but not in the second set:", difference)

# Run the program
if __name__ == "__main__":
    main()




QUESTION 25- Create a code that takes a tuples and two integers as input. The function should 
return a new tuple containing elements from the original tuple within the specified range of indices.

SOLUTION 25-
def slice_tuple(original_tuple, start_index, end_index):
    # Return a new tuple containing elements within the specified range
    return original_tuple[start_index:end_index]

# Example usage:
tuple_input = (10, 20, 30, 40, 50, 60, 70)
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

# Get the sliced tuple
sliced_result = slice_tuple(tuple_input, start, end)
print("Sliced Tuple:", sliced_result)




QUESTION 26- Write a code that prompts the user to input two sets of characters. Then print the union of these two sets.

SOLUTION 26-
def get_set_from_input(prompt):
    # Prompt the user for input and split by commas
    user_input = input(prompt)
    # Convert the input string into a set of characters
    return set(x.strip() for x in user_input.split(','))

def main():
    # Get two sets from user input
    set1 = get_set_from_input("Enter the first set of characters (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of characters (separated by commas): ")

    # Find the union of the two sets
    union_set = set1 | set2  # or use set1.union(set2)

    # Print the result
    print("The union of the two sets is:", union_set)

# Run the program
if __name__ == "__main__":
    main()




QUESTION 27- Develop a code that takes a tuple of integers as input. The function should return the maximum 
and minimum values from the tuple using tuple unpacking.

SOLUTION 27-
def min_max_tuple(input_tuple):
    # Use the built-in max() and min() functions to find the maximum and minimum
    maximum = max(input_tuple)
    minimum = min(input_tuple)
    
    # Return the results as a tuple
    return maximum, minimum

# Example usage:
# Taking a tuple of integers as input
user_input = input("Enter a tuple of integers (separated by commas): ")
# Convert the input string into a tuple of integers
input_tuple = tuple(int(x.strip()) for x in user_input.split(','))

# Get the maximum and minimum values
max_value, min_value = min_max_tuple(input_tuple)

# Print the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)




QUESTION 28-Create a code that defines two sets of integers. Then print the union, 
intersection, and difference of these two sets.

SOLUTION 28-
def main():
    # Define two sets of integers
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Calculate union, intersection, and difference
    union_set = set1 | set2  # Union
    intersection_set = set1 & set2  # Intersection
    difference_set = set1 - set2  # Difference (set1 - set2)

    # Print the results
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Union of set1 and set2:", union_set)
    print("Intersection of set1 and set2:", intersection_set)
    print("Difference of set1 and set2 (set1 - set2):", difference_set)

# Run the program
if __name__ == "__main__":
    main()




QUESTION 29- Write a code that takes a tuple and an element as input. The function should return 
the count of occurrences of the given element in the tuple.

SOLUTION 29-
def count_occurrences(input_tuple, element):
    # Return the count of the specified element in the tuple
    return input_tuple.count(element)

# Example usage:
# Taking a tuple as input
user_input = input("Enter a tuple of elements (separated by commas): ")
# Convert the input string into a tuple
input_tuple = tuple(x.strip() for x in user_input.split(','))

# Taking the element to count as input
element_to_count = input("Enter the element to count its occurrences: ").strip()

# Get the count of occurrences
count = count_occurrences(input_tuple, element_to_count)

# Print the result
print(f"The count of occurrences of '{element_to_count}' in the tuple is: {count}")





QUESTION 30- Develop a code that prompts the user to input two sets of strings. Then print 
the symmetric difference of these two sets.

SOLUTION 30-
def get_set_from_input(prompt):
    # Prompt the user for input and split by commas
    user_input = input(prompt)
    # Convert the input string into a set of strings
    return set(x.strip() for x in user_input.split(','))

def main():
    # Get two sets of strings from user input
    set1 = get_set_from_input("Enter the first set of strings (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of strings (separated by commas): ")

    # Calculate the symmetric difference (items in either set1 or set2 but not both)
    sym_diff = set1 ^ set2  # or use set1.symmetric_difference(set2)

    # Print the symmetric difference
    print("Symmetric Difference of the two sets is:", sym_diff)

# Run the program
if __name__ == "__main__":
    main()





QUESTION 31- Write a code that takes a list of words as input and returns a dictionary where the keys are 
unique words and the values are the frequencies of those words in the input list.

SOLUTION 31-
def word_frequencies(word_list):
    # Initialize an empty dictionary to store word frequencies
    freq_dict = {}

    # Iterate through the list of words
    for word in word_list:
        # If the word is already in the dictionary, increment its count
        if word in freq_dict:
            freq_dict[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            freq_dict[word] = 1

    return freq_dict

# Example usage:
# Taking a list of words as input from the user
user_input = input("Enter a list of words (separated by spaces): ")
# Convert the input string into a list of words
word_list = user_input.split()

# Get the word frequencies
frequencies = word_frequencies(word_list)

# Print the resulting dictionary
print("Word Frequencies:", frequencies)




QUESTION 32-Write a code that takes two dictionaries as input and merges them into 
a single dictionary. If there are common keys, the values should be added together.

SOLUTION 32-
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add values if key exists in both
        else:
            merged_dict[key] = value  # Otherwise, add the key-value pair

    return merged_dict

# Example usage
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}

result = merge_dictionaries(dict1, dict2)
print(result)





QUESTION 33-Write a code to access a value in a nested dictionary. The function should take 
the dictionary and a list of keys as input and return the corresponding value. If any of the keys do 
not exist in the dictionary, the function should return None.

SOLUTION 33-
def get_nested_value(nested_dict, keys):
    current_value = nested_dict
    for key in keys:
        if isinstance(current_value, dict) and key in current_value:
            current_value = current_value[key]
        else:
            return None  # Return None if any key is not found
    return current_value

# Example usage
nested_dict = {
    'a': {
        'b': {
            'c': 10
        }
    },
    'x': {
        'y': 20
    }
}

keys = ['a', 'b', 'c']  # Example keys
result = get_nested_value(nested_dict, keys)
print(result)  # Output: 10

keys_not_found = ['a', 'b', 'z']  # Keys that do not exist
result_not_found = get_nested_value(nested_dict, keys_not_found)
print(result_not_found)  # Output: None






QUESTION 34- Write a code that takes a dictionary as input and returns a sorted version 
of it based on the values. You can choose whether to sort in ascending or descending order.

SOLUTION 34-
def sort_dict_by_values(input_dict, ascending=True):
    # Sort the dictionary by values
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict

# Example usage
example_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grapes': 3}

# Sort in ascending order
sorted_asc = sort_dict_by_values(example_dict, ascending=True)
print("Ascending:", sorted_asc)

# Sort in descending order
sorted_desc = sort_dict_by_values(example_dict, ascending=False)
print("Descending:", sorted_desc)

Output:
css

Ascending: {'banana': 2, 'grapes': 3, 'apple': 5, 'orange': 8}
Descending: {'orange': 8, 'apple': 5, 'grapes': 3, 'banana': 2}






QUESTION 35- Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary correctly handles 
cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary.

SOLUTION 35-
def invert_dictionary(input_dict):
    inverted_dict = {}
    
    for key, value in input_dict.items():
        if value in inverted_dict:
            # If the value already exists, append the key to the list
            inverted_dict[value].append(key)
        else:
            # Otherwise, create a new entry with the key as a list
            inverted_dict[value] = [key]
    
    return inverted_dict

# Example usage
example_dict = {
    'apple': 1,
    'banana': 2,
    'orange': 1,
    'grapes': 3,
    'pear': 2
}

inverted = invert_dictionary(example_dict)
print(inverted)

Output:
css

{1: ['apple', 'orange'], 2: ['banana', 'pear'], 3: ['grapes']}


 
 