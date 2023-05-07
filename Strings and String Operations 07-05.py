# %%
# 1-Write a Python script to calculate the length of a string
my_input = input("write your text to calculate the lenght!")
input_lenght = len(my_input)
print(input_lenght)


# %%
# 2-Write a Python script that takes a string and prints it 3 times
input_1 = input("i'll treblicate your input! ")
for i in range(3):
    print(input_1)

# %%
# 3-Write a Python script that takes two strings, compares them and prints the result of the comparison
string_1 = input("write your first string")
string_2 = input("write your second string")
if string_1 == string_2:
    print (True)
else:
    print(False)
# %%
#4. Write a Python script that takes a string and prints the longest word of the string and its length

def longest_word(my_string):
    # Split the string into words
    words = my_string.split()
    
    # Find the longest word
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    # Return the longest word and its length
    return longest + " - " + str(len(longest))
# Enter the String
my_string = input("input your text here! ")
longest = longest_word(my_string)
print(longest)
# %%
# 5. Write a Python script that replaces the word 'bad' with the word 'good' and removes the word 'not' in a string
def transform_string(my_text):
    # Split the string into words
    words = my_text.split()

    # Iterate over each word and apply the transformations
    for i in range(len(words)):
        if words[i] == 'bad':
            words[i] = 'good'
        elif words[i] == 'not':
            words[i] = ''

    # Join the transformed words back into a string
    transformed_string = ' '.join(words)
    return transformed_string

# Test the function with an example string
my_text = "This is not a bad condetions"
transformed_string = transform_string(my_text)
print(transformed_string)