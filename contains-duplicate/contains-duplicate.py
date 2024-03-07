# https://www.youtube.com/watch?v=3OamzN90kPg&list=PLPe9IkX86X3y5m_MvtNu2ughxsvkqUNKr

# Using Hashset, uses more memory but is more efficient.
# Checks the hashset if value has the same value on the hashset
# Time complexity Time: O(n) Space: O(n)

class solution:
    def containsDuplicate(self, nums: list([int]))-> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    

solution_instance = solution()

# Creating an empty list
list_of_numbers = []

# Adding integers to the list
list_of_numbers.append(1)
list_of_numbers.append(2)
list_of_numbers.append(3)
list_of_numbers.append(4)
list_of_numbers.append(5)

containsDuplicate = solution_instance.containsDuplicate(list_of_numbers)

print(containsDuplicate)
