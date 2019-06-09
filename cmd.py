import sys
import re
from sys import argv


# TODO
# 1. Napisanie specyfikacji całej "biblioteki"
# 2. Pomyśleć nad zredukowanie osobnej listy do krótki i długi flag do 
#    jednej wspólnej
# 3. 
class Arguments:
    """ """
    def __init__(self):
        self.arg_list = []
        self.flags_list = []
        self.long_flags_list = []
        self.flag_input = []

    def get(self):
        if not argv:
            print("Arguments list is empty!")
        else:
            self.arg_list = argv[1:] 

    def display(self):
        return self.arg_list

    def flags(self):
        pattern = re.compile(r"\-[a-zA-Z0-9]")
        for x in self.arg_list:
            if(re.match(pattern, x) != None):
                self.flags_list.append(x)

        return self.flags_list

    def long_flags(self):
        pattern = re.compile(r"\-\-.")
        for x in self.arg_list:
            if(re.match(pattern, x) != None):
                self.long_flags_list.append(x)
                
        return self.long_flags_list

    def flags_with_input(self):
        pattern = re.compile(r'\=')
        for x in self.arg_list:
            if re.search(pattern, x):
                self.flag_input.append(re.split(pattern, x))

        return self.flag_input


class Help:
    """ User help display and configuration """
    def __init__(self):
        self.help_list ={'NAME':"",'DESCRIPTION':[],'AUTHOR':[],'CONTACT':[]}

    def display(self):
        print("NAME:\n", '\t', self.help_list['NAME'])
        print('DESCRIPTION:')
        for x in self.help_list['DESCRIPTION']:
            print('\t', x)
        print("AUTHOR:\n", '\t', self.help_list['AUTHOR'][0])
        print("CONTACT:\n", '\t', self.help_list['CONTACT'][0])
    
    def set_name(self, value):
        self.help_list['NAME'] = value

    def set_author(self, value):
        self.help_list['AUTHOR'].append(value)

    def set_contact(self, value):   
        pattern = re.compile(r'.*@.*\...') 
        if re.match(pattern, value) != None:
            self.help_list['CONTACT'].append(value)
        else:
            sys.stderr.write("You enterned invalid e-mail!\n")
            sys.exit()

    def add_parameter(self, flag, value):
        self.help_list['DESCRIPTION'].append(flag + '\t' + value)
        self.help_list['DESCRIPTION'].sort()
    

