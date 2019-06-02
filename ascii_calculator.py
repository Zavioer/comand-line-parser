import cmd

def file_calculation(name):
    with open(name, 'r') as f:
        w = f.read()
        sum = 0 
        for letter in w:
            if letter != " ":
                sum += ord(letter)
    return sum

def user_input_calculation(value):
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

# def f(x):
#     return {
#         '-h': help_module.display(),
#         '-r': reverse(),
#         '-o': file_calculation(name),
#     }[x]

# Set up basic information
help_module = cmd.Help()
help_module.set_name("ascii calculator - adding up all ASCII values of given string")
help_module.set_author("Piotr Bator")
help_module.set_contact("piotr.bator@zse.krakow.pl")
help_module.add_parameter("--open","take input for given file")
help_module.add_parameter("-o","same as \"--open\"")
help_module.add_parameter("-r","display reversed sum of ASCII values")
help_module.add_parameter("--direct","take input direct from this flag")
help_module.add_parameter("--hex","display output in hexadecimal value")
help_module.add_parameter("--help","display program reference and informations")
help_module.add_parameter("-h","same as \"--help\"")

# Set up arguments
arg_ini = cmd.Arguments()
arg_ini.get()

arg_list = arg_ini.flags()


for x in arg_list:
    if x == '-o' or x == '--open':
        flag_and_input = arg_ini.flags_with_input()
        for y in flag_and_input:
            for j in y:
                if j == '-o' or j == '--open':
                    print(j[1])
