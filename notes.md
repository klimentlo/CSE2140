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