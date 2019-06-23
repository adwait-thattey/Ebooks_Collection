import os
for filename in os.listdir("."):
    if filename.find('.') != -1:
        
        new_name = filename.title()
        new_name = new_name[:-4] + 'epub'
        new_name = new_name.replace('(Bookos-Z1.Org)', '')
        print(filename,new_name)
        # os.rename(filename, new_name)