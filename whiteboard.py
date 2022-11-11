# Write a function that will check whether ANY permutation of the characters of the input string is a palindrome.
# Bonus points for a solution that is efficient and/or that uses only built-in language functions.
# Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.
# Example
#   madam -> True
#  adamm -> True
#  junk -> False
# Hint
# The brute force approach would be to generate all the permutations of the string
# and check each one of them whether it is a palindrome.
# However, an optimized approach will not require this at all.

def is_palindrome(string):
    chars, count = {}, 0

    for char in string:
        # .get checks if key exists and if it doesn't it creates a new one with a default value
        chars[char] = chars.get(char, 0)+1

    for char in chars:
        if chars[char] % 2 == 1:
            count += 1
            if count > 1:
                return False

    return True


print(is_palindrome('aabaaa'))


def permute_a_palindrome(astring):
    hash_map, count = {}, 0
    for letter in astring:
        hash_map[letter] = hash_map.get(letter, 0)+1
    for letter in hash_map:
        if hash_map[letter] % 2 == 1:
            count += 1
            if count > 1:
                return False
    return True
# convert the string in to a list, and see if the count of each character in list is either 1 or even

# function accepts a str
# make a copy of it
# reverse the copy
# check if the input string reversed is equal to the reversed copy

# slice the last half of the string
# reverse that
# if that is equal to the first half its a palindrome
