#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/694

first_line = input()
number_elements = list(first_line)
number_elements_ordered_by_desc = sorted(number_elements, reverse=True)

#print(number_elements)
#print(number_elements_ordered_by_desc)
print(''.join(number_elements_ordered_by_desc))
