# CSE2140 Notes

## Version control Systems
Version control systems are a category of software tools that helps record changes to files by keeping track of modifications done to the code. There are many types of version control systems including Git, Subversion, Mercurial, Microsoft Team Foundation Version Control

Version control systems provide a framework for _external documentation_, where each commit documents that changed were made from a previous version of code. In addition, it provides documentation such as README files within the project folder.

Version control contributes to _change management_ as data is not lost when personnel leave the project and additionally, new recruits have documentation about what already happened

When a project is ready for publishing, the version control system can package the current project and release it. Release schedules vary depending on the project. They can either be time-based (such as Microsoft's "Update Tuesday") orr feature-based (such as video games being released with the "core" game and/or lots of bugs then requiring patches on/after release to fix bugs and release more content that the user has to buy)

### Git and Git Repositories
Git is a version control system that tracks changes to your source code. Git Repositories are online storage of the project code, versioned in Git.

Cloning a repository takes a copy of the git repository and places it onto a local computer. The clone has all versions and branches of the repository.S

To create a new version of the source code in git, the new changes must be __committed__ to git to save a local version of the changes

To synchronize the local changes to the online repository, the local committed versions must be pushed to the online repository.

## CCS10 Review

### Variables 
Variables are tools to store data and call that data at a later part of the program. When making variables, there are different formats to write variable names such as snake_case, kebab-case, camelCase, PascalCase, lowercase, UPPERCASE.

When naming variables,

1. The name of the variable should be descriptive of the content that is being stored
2. The name of the variable can only have letters, numbers, _, and - (no spaces!) 
3. The name of the variable cannot START with number (xPosition2 is okay, 2xPosition is not)

### Primitive Data Types
Data is stored in various types/formats so that the programs can interact with them based on the data type.

1. _Strings (of characters)_ - used to store text characters (numbers can be in a string, but you can't do math to them)
2. _Integers_ - used to store non-decimal numbers (and you CAN do math to them)
3. _Float(ing point  number)_ - used to store decimal numbers
4. _Booleans (logic)_ - used to store True or False

### Comparing Numbers
* ">" - Greater than
* "<" - Less than
* ">=" - Greater or equal to
* "<=" - Less than or equal to
* "==" - Equals (= changes the value of something, == is for comparing)
* "!=" - Not equals
### Mathematical operators
All programming languages include basic arithmetic. Common calculations inside addition (+), subtraction (-), multiplication (*), division (/), floor/integer division (//), and modules (%)
* When dividing, 13 / 5 = 2.6
* With floor division, 13 // 5 = 3 (whole number quotient without the remainder)
* With modulus, 13 % 5 = 3 (just the remainder, not the quotient)

## Contractions
In Python, there are two common contractions used for decisions and accumulation (counting)

### Decision
```python
AVERAGE = float(input("Enter your average: "))

if AVERAGE > 79.9:
    GRADE = "A"
else:
    if AVERAGE > 64.9 
        GRADE = "B"
    else: 
     if ...........

if AVERAGE > 79.9:
    GRADE = "A"
elif AVERAGE > 64.9:
    GRADE = "B"
elif AVERAGE > 49.9:
    GRADE = "C"
else:
    GRADE = "D"
```

### Accumulation

```python
NUMBER = 0
# NUMBER = NUMBER + 1
NUMBER += 1

# This contraction works or all operations
NUMBER -= 1
NUMBER *= 2
NUMBER /= 2
NUMBER //= 2
NUMBER %= 2
```


## For and While loops
Loops provide repetition to parts of a program without the need to copy and paste sections of code. 

s
For loops will repeat until a number of iterations are met; While loops will continue to repeat until a specific condition is met. 

```python
# for loop
for i in range(5):
    print("Hello World")
# prints the text string 5 times

#while loop
NUMBER = 5
while NUMBER > 0:
    print("Hello World")
    NUMBER -= 1
#print the text string 5 times
```
* To immediately exit a loop, use the ```break``` statement
* To skip the rest of a loop and start the next iteration, used the ```Continue``` statement

## Libraries
Programming languages divide the commands capable within the programming language into separate files so that only a core set of commands make up the default language. This process allows programs to run with only the set of commands required for the program to function. Therefore, the program can function more smoothly without the bloat of other commands not relevant to the program (for example, most programs don't need network management tools so commands relevant to those tools would be stores in a library and not in the core language). Programming languages have a __standard library__ that is maintained as part of the language. There are also third party libraries that can be installed separately and imported into the language

```python
# to add an entire library
import libraryname
# to use "exit" from library name
libraryname.exit

# to add only one command from a library
from libraryname import exit 
# to use exit after import just the command
exit()

# import a library and rename the library
import librarywithalongnamethatdoesntneedtobelongname as ln 

ln.exit 

# import all values within a library
from libraryname import *

exit()
```

When importing entire libraries, it is possible to list multiple libraries in a single import; however, this increases the complexity of debugging and can reduce readability 

import library name, math, anotherrandomname

When importing individual commands from a library, multiple commands can be imported at the same time by listening them in a single statement
