#!/usr/bin/env python
# Author: Ashutosh Narayan
# Email: aashutoshnarayan@gmail.com

# Create subdirectory under app/ directory

def main():
 import os,sys,glob,time

 dirName1 = '../app/handlers'
 dirName2 = '../app/utils'
 dirName3 = '../app/data'
 file1 = '../app/japanese_name_location_dict.txt'
 file2 = '../app/chinese_family_name_dict.txt'
 file3 = '../app/utils/utils.py'

 #Create subdirectories if they don't exist
 if not os.path.exists(dirName1):
     os.mkdir(dirName1, 0755);
     print ("Directory", dirName1, "is created")
 else:
     print ("Directory", dirName1, "already exists")

 if not os.path.exists(dirName2):
     os.mkdir(dirName2,0755)
     print ("Directory", dirName2, "is created")
 else:
     print ("Directory", dirName2, "already exists")

 if not os.path.exists(dirName3):
     os.mkdir(dirName3,0755)
     print ("Directory", dirName3, "is created")
 else:
     print ("Directory", dirName3, "already exists")

 # Move all the BaseHandlers to handlers subdirectory
 
 os.system('grep -Ril "BaseHandler" ../app/ | xargs mv -t ../app/handlers/')
 os.system('grep -Ril --exclude-dir=../app/handlers/ "utils.BaseHandler" ../app/ | xargs mv -t ../app/utils/')

 # Move all files to handlers except few from utils directory 

 os.system('find ../app/utils/* ! -name utils.py -exec mv -t ../app/handlers/ {} +')
 
 # Move all remaining files under app/ to utils/
 os.system('find ../app/*.py -type f ! -name main.py ! -name model.py -exec mv -t ../app/utils/ {} +')
 os.system('mv ../app/handlers/*.yaml ../app/')

 if os.path.exists(file1):
     os.system('mv ../app/japanese_name_location_dict.txt ../app/data/')
 else:
     print ("File is moved")
 if os.path.exists(file2):
     os.system('mv ../app/chinese_family_name_dict.txt ../app/data/')
 else:
     print ("File is moved")

if __name__ == '__main__':
    main()
