#2. Write a Python function `reverse_string(s: str) -> str` that takes a string and returns its reverse.

def reverse_string(word):
    print(word[::-1])  #here i used list slicing methode to reverse string useing neagetive step indexing

    new_one = list(word)
    new_one.reverse()
    print("".join(new_one)) #another method by usein list inbuilt function revese, first i converted into list then applied reverse function 
                            #after by using join fucntion the reversed word created

word = input()
reverse_string(word=word)