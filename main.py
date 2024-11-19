#Use config parser to sync variables from matlab



import configparser


# create a config
config = configparser.ConfigParser()

# crate sample ini file
config['DEFAULT'] = {'var1': '45',
                     'var2': '2',
                     'var3': '9'}

with open('example.ini', 'w') as configfile:
  config.write(configfile)



def autoFormat(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
