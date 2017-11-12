import sys
import os

file_dir = sys.argv[-1]

file_list = os.listdir(file_dir)
old_format = raw_input("Enter the format you want to change: ")
new_format = raw_input("Enter the new format: ")
converted = 0
for names in file_list:
    splitted = names.split('.')
    if splitted[-1] == old_format:
        splitted.remove(old_format)
        splitted.append(new_format)
        new_name = '.'.join(splitted)
        old_name = os.path.join(file_dir, names)
        newest = os.path.join(file_dir, new_name)
        os.rename(old_name, newest)
        converted += 1
print('%s files converted from %s to %s' %(converted, old_format, new_format))

# total = len(sys.argv)
# cmdargs = str(sys.argv)
# print("The total number of system arguments is %d" %total)
# print("Args list: %s" % cmdargs)
