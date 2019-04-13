import os
for filename in os.listdir("."):
    if filename.find(' - ') != -1:
        index_change = filename.find(' - ')
        new_name = filename[index_change+2:-5] + ' - ' + filename[:index_change] + '.epub'
        os.rename(filename, new_name)