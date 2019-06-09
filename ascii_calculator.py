import cmd


# TODO
# 1. Open file only with long flags (minus)
# 2. 
def file_calculation(name):
    with open(name, 'r') as f:
        w = f.read()
        sum = 0 
        for letter in w:
            if letter != " ":
                sum += ord(letter)
    return sum

def user_input_calculation(value):
    # Add space handling by quotes ""
    sum = 0
    for letter in value:
        if letter != ' ':
                sum += ord(letter)
    return sum

def to_hex(value):
    return hex(value)

def reverse(value):
    str_val = str(value)
    i = len(str_val) - 1
    reversed_list = ''

    while i >= 0 :
        reversed_list += str_val[i]
        i -= 1
    return reversed_list

# Set up basic information
help_module = cmd.Help()
help_module.set_name("ascii calculator - adding up all ASCII values of given string")
help_module.set_author("Jan Kowalski")
help_module.set_contact("jkowalski@google.com")
help_module.add_parameter("--open","take input for given file")
help_module.add_parameter("-r","display reversed sum of ASCII values")
help_module.add_parameter("--direct","take input direct from this flag")
help_module.add_parameter("--hex","display output in hexadecimal value")
help_module.add_parameter("--help","display program reference and informations")
help_module.add_parameter("-h","same as \"--help\"")

# Set up arguments
arg_ini = cmd.Arguments()
arg_ini.get()

flag_list = arg_ini.flags()
long_flags = arg_ini.long_flags()
flags_with_input = arg_ini.flags_with_input()
arg_list = flag_list + long_flags
flag_with_input = arg_ini.flags_with_input()

if arg_list == []:
    help_module.display()
else:
    for x in flags_with_input:
        if x[0] == '--open':
            gray = file_calculation(x[1])
        elif x[0] == '--direct':
            gray = user_input_calculation(x[1])

    print("+========== ASCII CALCULATOR v0.1 ==========+")            
    print("ASCII value of inputed file: ", gray)          

    for x in arg_list:
        if x == '-r':
            print("Reversed value:",reverse(gray))
        elif x == '-h' or x == '--help':
            help_module.display()
        elif x == '--hex':
            print("Value converted to hexadecimal:", to_hex(gray))
    
    print("+===========================================+")