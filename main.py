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


# create config file and write sample parser
def ini_config():
    config = configparser.ConfigParser()

    config['DEFAULT'] = {'var1': '45',
                         'var2': '2',
                         'var3': '9'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# read config
def read_config(filename, section, key, verbose=False):
    """read config file, with input filename, section and key, outputs a value from config file"""
    config = configparser.ConfigParser()
    config.read(filename)
    value = config[section][key]
    return value


# autoformat the values with comma inserted
def autoFormat(description, var):

    # define variables
    var_new = "" # create temp var to store

    # add comma after every variable except last one
    for elements in range(len(var)):
        if elements == len(var)-1:
            var_new = var_new + str(var[elements])
        else:
            var_new += str(var[elements])
            var_new += ", "

    output = description + var_new
    return output



# main function
if __name__ == '__main__':
    print("Start")
    desc1 = "sample = "
    var1 = 1
    var2 = 2
    var3 = 5
    var = [var1]
    test1 = autoFormat(desc1, var)
    print(test1)

    # ini_config()

    # define variables
    filename = 'config.ini'
    section = 'DEFAULT'
    key = 'var1'

    # add variables
    value = read_config(filename, section, key, verbose=False)
    print(autoFormat(desc1, [value]))

