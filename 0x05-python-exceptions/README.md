#  Python - Exceptions
## Read More 
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)(starting at minute 7)
## Requirement of Task
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
## List of Task
- [0-safe_print_list.py](0-safe_print_list.py) **Write a function that prints x elements of a list.**
  - Prototype: def safe_print_list(my_list=[], x=0):
  - my_list can contain any type (integer, string, etc.)
  - All elements must be printed on the same line followed by a new line.
  - x represents the number of elements to print
  - x can be bigger than the length of my_list
  - Returns the real number of elements printed
  - You have to use try: / except:
  - You are not allowed to import any module
  - You are not allowed to use len()
- [1-safe_print_integer.py](1-safe_print_integer.py) **Write a function that prints an integer with "{:d}".format().**
  - Prototype: def safe_print_integer(value):
  - value can be any type (integer, string, etc.)
  - The integer should be printed followed by a new line
  - Returns True if value has been correctly printed (it means the value is an integer)
  - Otherwise, returns False
  - You have to use try: / except:
  - You have to use "{:d}".format() to print as integer
  - You are not allowed to import any module
  - You are not allowed to use type()
- [2-safe_print_list_integers.py](2-safe_print_list_integers.py) **Write a function that prints the first x elements of a list and only integers.**
  - Prototype: def safe_print_list_integers(my_list=[], x=0):
  - my_list can contain any type (integer, string, etc.)
  - All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
  - x represents the number of elements to access in my_list
  - x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
  - Returns the real number of integers printed
  - You have to use try: / except:
  - You have to use "{:d}".format() to print an integer
  - You are not allowed to import any module
  - You are not allowed to use len()
- [3-safe_print_division.py](3-safe_print_division.py) **Write a function that divides 2 integers and prints the result.**
  - Prototype: def safe_print_division(a, b):
  - You can assume that a and b are integers
  - The result of the division should print on the finally: section preceded by Inside result:
  - Returns the value of the division, otherwise: None
  - You have to use try: / except: / finally:
  - You have to use "{}".format() to print the result
  - You are not allowed to import any module
- [4-list_division.py](4-list_division.py) **Write a function that divides element by element 2 lists.**
  - Prototype: def list_division(my_list_1, my_list_2, list_length):
  - my_list_1 and my_list_2 can contain any type (integer, string, etc.)
  - list_length can be bigger than the length of both lists
  - Returns a new list (length = list_length) with all divisions
  - If 2 elements can’t be divided, the division result should be equal to 0
  - If an element is not an integer or float:
    - print: wrong type
  - If the division can’t be done (/0):
    - print: division by 0
  - If my_list_1 or my_list_2 is too short
    - print: out of range
  - You have to use try: / except: / finally:
  - You are not allowed to import any module
- [5-raise_exception.py](5-raise_exception.py) **Write a function that raises a type exception.**
  - Prototype: def raise_exception():
  - You are not allowed to import any module
- [6-raise_exception_msg.py](6-raise_exception_msg.py) **Write a function that raises a name exception with a message.**
  - Prototype: def raise_exception_msg(message=""):
  - You are not allowed to import any module
- [100-safe_print_integer_err.py](100-safe_print_integer_err.py) **Write a function that prints an integer.**
  - Prototype: def safe_print_integer_err(value):
  - value can be any type (integer, string, etc.)
  - The integer should be printed followed by a new line
  - Returns True if value has been correctly printed (it means the value is an integer)
  - Otherwise, returns False and prints in stderr the error precede by Exception:
  - You have to use try: / except:
  - You have to use "{:d}".format() to print as integer
  - You are not allowed to use type()
- [101-safe_function.py](101-safe_function.py) **Write a function that executes a function safely.**
  - Prototype: def safe_function(fct, *args):
  - You can assume fct will be always a pointer to a function
  - Returns the result of the function,
  - Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
  - You have to use try: / except:
- [103-python.c](103-python.c) **Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.**
  - Python lists:
    - Prototype: void print_python_list(PyObject *p);
    - Format: see example
    - If p is not a valid PyListObject, print an error message (see example)
  - Python bytes:
    - Prototype: void print_python_bytes(PyObject *p);
    - Format: see example
    - Line “first X bytes”: print a maximum of 10 bytes
    - If p is not a valid PyBytesObject, print an error message (see example)
  - Python float:
    - Prototype: void print_python_float(PyObject *p);
    - Format: see example
    - If p is not a valid PyFloatObject, print an error message (see example)
    - Read /usr/include/python3.4/floatobject.h
  - About:
    - Python version: 3.4
    - You are allowed to use the C standard library
    - Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
    - You are not allowed to use the following macros/functions:
      - Py_SIZE
      - Py_TYPE
      - PyList_Size
      - PyList_GetItem
      - PyBytes_AS_STRING
      - PyBytes_GET_SIZE
      - PyBytes_AsString
      - PyBytes_AsStringAndSize
      - PyFloat_AS_DOUBLE
      - PySequence_GetItem
      - PySequence_Fast_GET_SIZE
      - PySequence_Fast_GET_ITEM
      - PySequence_ITEM
      - PySequence_Fast_ITEMS
  - NOTE:
    - The python script will be launched using the -u option (Force stdout to be unbuffered).
    - It is strongly advised to either use setbuf(stdout, NULL); or fflush(stdout) in your C functions IF you choose to use printf. The reason to that is that Pythonsprintand libCs printf don’t share the same buffer, and the output can appear disordered.
