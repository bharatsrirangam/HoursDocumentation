import os
import datetime as dt
import sys

money_txt_path = '/Users/Bharat_Srirangam/Desktop/HoursDocumentation/money.txt'

args = sys.argv
def check_exists():
	exists = os.path.isfile(money_txt_path)
	if not exists:
		print('Does not exist')
		file = open(money_txt_path,'w')
		file.write('Current Account: \n0.0\n=================================\n')
		file.close()

def main():
	check_exists()
	stringdate = str(dt.date.today())
	file = open(money_txt_path, 'r')
	temp = file.read()
	split_unclean = temp.split('\n')
	split = []
	for line in split_unclean:
		if len(line) > 1:
			split.append(line)
	count = float(split[1])
	file.close()

	content = ''
	if args[1] == '-view':
		content = '\n'.join(split)
		divider = '=================================' + '\n'
		sections = temp.split(divider)
		print(sections[-1])
	elif args[1] == '-clear':
		split[1] = '0.0'
		content = '\n'.join(split)
		content = content + '\n' + 'Week\'s Total - ' + str(count) + '\n' + '=================================' + '\n'
		count = 0
	elif len(args) == 3 and args[1] == '-a':
		isTrue = False
		indecies = range(len(split))
		indecies.reverse()
		for i in indecies:
			if ': ' in split[i]:
				element = split[i].split(': ')
				if element[0] == stringdate:
					isTrue = True
					split[i] = stringdate + ': ' + str((float(element[1]) + float(args[2]))) + ' : ' + element[2]
					break
		count = count + float(args[2])
		split[1] = str(count)
		content = '\n'.join(split)
		if not isTrue: 
			content = content + '\n' + stringdate + ': ' + str(args[2]) + ' : ' + 'Unknown Purchase'
	else:
		count = count + float(args[1])
		split[1] = str(count)
		content = '\n'.join(split)
		content = content + '\n' + stringdate + ': ' + str(args[1]) + ' : ' + args[2]
		
	file = open(money_txt_path, 'w')
	file.write(content)
	file.close()
	print('Your total accumulated payments is: ' + str(count))

main()