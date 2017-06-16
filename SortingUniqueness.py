import sys, getopt

def main(argv):
	if not argv:
		print 'Please provide data as arguments.'
                sys.exit()
    	else:
		arg_str = ' '.join(argv)
		print 'argument = ', arg_str	
		if len(arg_str) > 10:
			print 'too big'
        		return False

    		char_set = [False for _ in range(128)]
    		for char in arg_str:
        		val = ord(char)
        		if char_set[val]:
            			# Char already found in string
            			print 'Found Duplicate'
				return False
			print 'Did not find dupicate'
        		char_set[val] = True

    		return True

if __name__ == "__main__":
   main(sys.argv[1:])

