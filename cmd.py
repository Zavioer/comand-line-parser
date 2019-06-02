import sys
import re
from sys import argv


# TODO
# 1. Napisanie specyfikacji całej "biblioteki"
<<<<<<< HEAD
# 5. Wrzucić kod na GitHub
=======
>>>>>>> 8459f5c896bb0bc29f19ec2e6a37ca153dfd816c

class Arguments:
    """ """
    def __init__(self):
        self.arg_list = []
        self.flags_list = []
        self.long_flags_list = []
<<<<<<< HEAD
        self.flag_input = []
=======
>>>>>>> 8459f5c896bb0bc29f19ec2e6a37ca153dfd816c

    def get(self):
        if not argv:
            print("Arguments list is empty!")
        else:
            self.arg_list = argv[1:] 

    def display(self):
        return self.arg_list

    def len(self):
        return len(self.arg_list)

    def flags(self):
<<<<<<< HEAD
        pattern = re.compile(r"\-[a-zA-Z0-9]")
=======
        pattern = re.compile(r"\-[a-z]")
>>>>>>> 8459f5c896bb0bc29f19ec2e6a37ca153dfd816c
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

<<<<<<< HEAD
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
    


=======
class Help:
    """ User help display and configuration """
    # TODO
    # 1. Dodawanie znaczenia parametru
    # 2. Stalenie formatu wyświetlania pomocy
    # 3. Usuwanie parametru 
    # 4. Wypróbowanie możliwości konfigurowania każdej sekcji poprzez osobną metode
    # 5. Wrzucić kod na GitHub

    def __init__(self):
        self.help_list ={'NAME':[],'DESCRIPTION':[],'AUTHOR':[],'CONTACT':[]}

    def display(self):
        print("NAME:\n", '\t', self.help_list['NAME'][0])
        print('DESCRIPTION:')
        for x in self.help_list['DESCRIPTION']:
            print('\t', x)
        print("AUTHOR:\n", self.help_list['AUTHOR'][0])
        print("CONTACT:\n", self.help_list['CONTACT'][0])

    # OLD VERSION 1.0
    # def add_parameter(self, section_name, value):
    #     position = self.help_list.index(section_name)
    #     self.help_list.insert(position + 1, value)

    def add_parameter(self, section_name, value, flag=None):
        if(flag != None):
            self.help_list[section_name].append(flag + '    ' + value)
            self.help_list[section_name].sort()
        else:
            self.help_list[section_name].append(value)

        return

    def del_parameter(self, section_name, number):
        # TODO
        # Poprawić w taki sposób, aby nie używać numeru indexu tylko tekstu
            self.help_list[section_name].pop(number)



    
test = Arguments()
test.get()
value = test.display()
print("Arguments list: ", value)
print("Single char flags list: ", test.flags())
print("Long flags list: ", test.long_flags())


help = Help()
print("Initial help parameters list: ", help.help_list)
help.add_parameter('DESCRIPTION', 'odwraca kolejnosc sortowania', '-r')
help.add_parameter('AUTHOR', 'jan(dot)kowalski.com')
help.add_parameter('DESCRIPTION', 'skanowanie w poszukiwaniu bledu', '-a')
help.add_parameter('NAME', 'Program do wyszukiwani powtarzajacych sie liter w wyrazie.')
help.add_parameter('CONTACT', 'www.beznadzieja.pl')
print("Modified help parameters list: ", help.help_list)

print("\n >>>>>>><<<<<<<<<<")
help.display()
>>>>>>> 8459f5c896bb0bc29f19ec2e6a37ca153dfd816c
