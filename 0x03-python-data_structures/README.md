# Python - Data Structures: Lists, Tuples
## Read More
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until 5.3. Tuples and Sequences included)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)
## Task Requriement
- Python Scripts

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	- All your files should end with a new line
	- The first line of all your files should be exactly #!/usr/bin/python3
	- A README.md file, at the root of the folder of the project, is mandatory
	- Your code should use the pycodestyle (version 2.8.*)
	- All your files must be executable
	- The length of your files will be tested using wc
- C

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	- All your files should end with a new line
	- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
	- You are not allowed to use global variables
	- No more than 5 functions per file
	- The prototypes of all your functions should be included in your header file called lists.h
	- Don’t forget to push your header file
	- All your header files should be include guarded
## Task List
- [0-print_list_integer.py](0-print_list_integer.py) Write a function that prints all integers of a list.
	- Prototype: def print_list_integer(my_list=[]):
	- Format: one integer per line. See example
	- You are not allowed to import any module
	- You can assume that the list only contains integers
	- You are not allowed to cast integers into strings
	- You have to use str.format() to print integers
- [1-element_at.py](1-element_at.py) Write a function that retrieves an element from a list like in C.
	- Prototype: def element_at(my_list, idx):
	- If idx is negative, the function should return None
	- If idx is out of range (> of number of element in my_list), the function should return None
	- You are not allowed to import any module
	- You are not allowed to use try/except
- [2-replace_in_list.py](2-replace_in_list.py) Write a function that replaces an element of a list at a specific position (like in C).
	- Prototype: def replace_in_list(my_list, idx, element):
	- If idx is negative, the function should not modify anything, and returns the original list
	- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
	- You are not allowed to import any module
	- You are not allowed to use try/except
