import os
import datetime as dt
import sys

hours_txt_path = '/Users/Bharat_Srirangam/Desktop/HoursDocumentation/hours.txt'

args = sys.argv
exists = os.path.isfile(hours_txt_path)
if exists:
    print('exists')
else:
	print('does not exist')
	file = open(hours_txt_path,'w')
	file.write('Current Hours: \n0.0\n======================')
	file.close()


file = open(hours_txt_path, 'r')
temp = file.read()
split = temp.split('\n')
count = float(split[1])
file.close()

content = ''

if args[1] == 'clear':
	split[1] = '0.0'
	content = '\n'.join(split)
	content = content + '\n' + '=================================' + '\n'
	
else:
	count = count + float(args[1])
	split[1] = str(count)
	content = '\n'.join(split)
	content = content + '\n' + str(dt.date.today()) + ': ' + str(args[1])
	
file = open(hours_txt_path, 'w')
file.write(content)
file.close()
print('complete')