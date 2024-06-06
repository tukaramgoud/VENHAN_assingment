'''4. Write a Python program to count the frequency of each character in a given string and
return a dictionary with characters as keys and their frequencies as values.
'''

string = "bbbb cccc dd ee f"
original_string = list(string) #to count the letters in string i'm creating a list with elements of string

new_string = sorted(list(set(list(string.replace(" ", ''))))) #here i'm creatin another list without having the any duplicates and i'm removing spaces from string
 

result_dict = {}

for i in new_string:
    count_is = original_string.count(i) #by using for loop taking i as a key for dict, and count as a value of the key i created the result dictionary
    result_dict[i] = count_is
print(result_dict)