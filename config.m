import iniConfig.* 


% start iniconfig and read config file
ini = IniConfig();
ini.ReadFile('config.ini');

% define variables. Section, key and value
section = 'DEFAULT';
keys = 'var1';
new_values = '6';

% rewrite new value to config file
ini.SetValues(section, keys, new_values, '%.3f');
ini.WriteFile('config.ini');
fprintf('job done \n');


% run python file
pyrunfile("main.py");