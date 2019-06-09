# Command line parser
This program helps handling arguments passing directly to Python 3 script, when calling.  
## Motivation
Simple command line parser implementation for learing OOP in Python purpose.
## Code Example

## Installation
Just download cmd.py module and add to Your probram by `import` keyword.
## API Reference
### Class Arguments
**get()**
Take all given arguments to list.
**display()**
Display list of given arguments.
**flags()**
Search thru arg\_list for flags starting with one "\-", return list with only this flags.
**long\_flags()**
Search thru arg\_list for flags starting with two "\-", return list with only this flags.
**flags\_with\_input()**
Search thru arg\_list for flags starting with two "\-" and having input after "=", return list with only this flags and inputed values. Like [flag, value]
### Class Help
**display()**
Display help statemeny, with all added informations and flags definitons.
**set_name(value)**
Set up name of the program given as `value` argument with short description.
**set_author(value)**
Set up author of the program given to `value` argument.
**set_contact(value)**
Set up contact e-mail given to `value` argument.
**add_parameter(flag, value)**
Add a flag `flag` and definition what this flag doing `value` to list whith is next sorted.
## How to use?
Start with declareting the Help class object, then fill with basci information *name, author, contact* then using add_parameter() function add flags description You want. Then create Agrumens class object, next init arguments list with **get()** method. Final step is get falgs from list and code what program do if flag is given. 
## License
GPLv3 [Zavioer](https://github.com/Zavioer)


