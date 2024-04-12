# Tech 258 Python

## Sub heading

### Small Heading

#### Smallest Heading

Normal Text

* Bullet 1
* Bullet 2

- Bullet 1
- Bullet 2

Press tab to do indents within bullets <br>
Shift tab to take away those indents

*Italics*<br>
**Bold**

## Code

Code Snippet `this is code`

Code Block
``` python
this is a block of code
This is still code
Still Code

print("Hello World!")
```

# Tech 258
## Python

<img alt="Python_logo" height="200" src="https://banner2.cleanpng.com/20180806/fv/kisspng-python-scalable-vector-graphics-logo-javascript-cl-coderpete-game-development-5b6819307ca155.2506144815335488485105.jpg" width="200"/>

### **What is Python?**
Python is a computer programming language often used to build websites and software, automate tasks, and analyze data.
<br> It was created by Guido van Rossum in 1991 and developed by Python Software Foundation.

#### *Why is Python so popular?*
This is because: <br>
* It is a very flexible, powerful and accessible language
* The syntax is considered to be very easy to read and understand

#### *But why is it particularly popular for DevOps engineers?*
* Python allows for quick automation of tasks
* Python has extensive libraries
* Python has a large community, so it becomes easier to find solutions

### **What is a venv (Virtual Environment)?**
It is an isolated environment for python projects, so each project can have its own dependencies.
<br> It also allows for consistancy across machines.

### **What is "pip"?**
Pip is the standard package manager for Python. <br> It allows you to install and manage additional packages that are not part of the Python standard library.
<br> **Examples of packages are:**
* PyTorch
* TensorFlow

## **What is scripting?**
Scripting is code used to automate processes. Scripting is used on existing programs, such as Terraform, Cloud Providers, etc.
#### *But what's the difference between programs and scripting?*
Scripts usually complete a simple task, while programs have a much wider scope.

### **What are some of the base python libraries?**
* os: Provides operating system interfaces for file operations, directory manipulations and process management.
* sys: Contains system-specific parameters and functions, such as access to command-line arguments, Python interpreter settings, and standard I/O streams.
* math: Offers mathematical functions and constants for numerical calculations, including trigonometric functions, logarithms, and constants like Pi and e.

<img alt="NumPy_logo" height="200" src="https://user-images.githubusercontent.com/50221806/86498201-a8bd8680-bd39-11ea-9d08-66b610a8dc01.png" width="200"/>

## Task 1: If Statements

### Create a program that checks if a user can watch a movie based on the users age.

Possible film ratings are "universal", "pg", "12", "12a", "15", "18"
<br> `film_rating = "12a"`

Use an if statement to check for "universal" rating
<br> `if film_rating == "universal":`
<br>`print("all age groups can watch this film")`

Checks if the film rating is "pg"
<br>`elif film_rating == "pg":`
<br>`print("General viewing, but some scenes may be unsuitable for young children.")`

Checks if the film rating is "12" or "12a"
<br>`elif film_rating == "12" or film_rating == "12a":`
<br>`print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")`

Checks if the film rating is "15"
<br>`elif film_rating == "15":`
<br>`print("No one younger than 15 may see a 15 film in a cinema.")`

Checks if the film rating is "18"
<br>`elif film_rating == "18":`
<br>`print("No one younger than 18 may see an 18 film in a cinema.")`

Else statement if none of the above conditions are met
<br>`else:`
<br>`print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")`

## Task 2: Loops

Loops allow you to execute a block of code repeatedly based on a certain condition or for a specified number of times. 
They are essential for automating repetitive tasks and iterating over collections of data. 
There are primarily two types of loops:
* **For Loop**: A for loop is used to iterate over a sequence (such as a list, tuple, or range) or perform a task a specific number of times. It consists of an initialization, a condition, and an increment or decrement operation.
* **While Loop**: A while loop repeats a block of code as long as a specified condition is true. Unlike a for loop, a while loop does not require a predetermined number of iterations and is useful when the number of iterations is unknown or determined by a condition.

### What we can do with loops:

* Iterate over elements in a collection (like lists, arrays, etc.).
* Perform a task a specific number of times.
* Implement algorithms that require repetitive execution.
* Keep a program running until a certain condition is met (in the case of while loops).
* Streamline and automate repetitive tasks.

#### Example of a for loop iterating over a list of numbers
`numbers = [1, 2, 3, 4, 5]`

`for num in numbers:`
<br>`print(num)`

### While Loops

While Loops are useful when the total number of iterations isn't predetermined or when you require executing a block of code repeatedly until a specific condition is fulfilled. 
For instance, they're suitable for scenarios like awaiting user input for a particular value or processing data until a specific condition is met.

#### While Loop Example:

Example of a while loop counting from 1 to 5

`count = 1`

`while count <= 5:`
    <br>`print(count)`
    <br>`count += 1`

This while loop prints numbers from 1 to 5 to the console. 
It continues to execute the block of code as long as the count variable is less than or equal to 5.

#### Risks and Tips with Loops

* **Infinite Loops**: Ensure exit conditions are reachable.
* **Performance**: Be cautious with many iterations or complex operations.
* **Off-by-One Errors**: Check loop boundaries carefully.
* **Readability**: Keep loops simple for easier understanding.
* **Resource Management**: Manage resources properly within loops.
* **Optimization**: Prioritize clarity over premature optimization.










