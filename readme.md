# File Encoding Check Plugin
The File Encoding Check plugin is a OneAgent plugin for Dynatrace. 
This plugin will check all files with a specific file extension in a directory and return a problem if any of those files do not match the desired encoding. 

The values of encoding that this plugin can check are anything that can be checked by the python "chardet" library.
https://readthedocs.org/projects/chardet/

## Configuration
The plugin must be configured with values for: 
filepath: the directory in which files should be checked
file_extension: the file extension of files to be checked (e.g. txt, dat, csv, etc...)
encoding_type: the encoding we want to check for (should match the values returned by chardet) (e.g. ascii, UTF-8-SIG, ETC) 

## Encoding_type
Being able to check the encoding is not always 100% guaranteed, as it is essentially a best guess based on how the file appears (e.g. is there a Byte Order Mark at the start of the file or not? etc...) 

for that reason you can check how chardet will detect your desired file format using "test.py" in the testing folder of this repository. 
E.g. Windows ANSI CP-1252 often shows us as "ascii" etc.

# Using the plugin
1. Download "custom.python.encoding_check.zip" (or alternatively download the files from src and build the plugin yourself :) )
2. Upload the zip file to Dynatrace (`Settings -> Monitoring -> Monitoring Overview -> Custom Plugins`)
3. On each host where you want the plugin to run, extract the zip into the plugin deployment directory
e.g. `C:\Program Files (x86)\dynatrace\oneagent\plugin_deployment\custom.python.encoding_check`
4. Configure the plugin properties within the Dynatrace UI, as in the above section, configuration
(`Settings -> Monitoring -> Monitoring Overview -> Custom Plugins -> custom.python.encoding_check`)