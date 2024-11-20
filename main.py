#Use config parser to sync variables from matlab

import syncFunc

# main function
if __name__ == '__main__':
    desc1 = "sample = "
    var1 = 1
    var2 = 2
    var3 = 5
    var = [var1]
    test1 = syncFunc.autoFormat(desc1, var)
    print(test1)

    # ini_config()

    # define variables
    filename = 'config.ini'
    section = 'DEFAULT'
    key = 'var1'

    # add variables
    value = syncFunc.read_config(filename, section, key, verbose=False)
    print(syncFunc.autoFormat(desc1, [value]))

