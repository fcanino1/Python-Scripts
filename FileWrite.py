from sys import argv

script, filename = argv

target = open(filename, 'w')

i = 0

answer = raw_input("Do you want to erase the file? ")
if answer == 'Yes' or answer == 'yes':
	print "Erasing the file now..."
	target.truncate()
else:
	print 'Moving on to file writing phase...'
	
while i < 1:		
	line = raw_input("Please enter a line of text to write into the file: ")
	print "Writing the file now..."
	target.write(line)
	target.write('\n')
	answer = raw_input("Write another line into the file? ")
	
	if answer == 'Yes':
		i = 0
	else:
		i = 1

print "File being closed now..."
target.close()
