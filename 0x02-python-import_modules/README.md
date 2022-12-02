# Import Modules
## Read More 
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
## Task Requirement 
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
## Tasks
- **0. Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3**
  - You have to use print function with string format to display integers
  - You have to assign:
  - the value 1 to a variable called a
    - the value 2 to a variable called b
    - and use those two variables as arguments when calling the functions add and print
    - a and b must be defined in 2 different lines: a = 1 and another b = 2
  - Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
  - You can only use the word add_0 once in your code
  - You are not allowed to use \* for importing or \__import\__
  - Your code should not be executed when imported - by using \__import\__, like the example below
