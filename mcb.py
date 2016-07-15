
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
	print "Text copied to clipboard" , sys.argv[2]


elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	if sys.argv[2].lower() == 'all':
		mcbShelf.clear()
		print "Deleted all saved clipboards!"
		
	elif sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
		print "\"%s\" clipboard deleted." % (sys.argv[2])


elif len(sys.argv) == 2:

	if sys.argv[1].lower() == 'list':
	#	pyperclip.copy(str(list(mcbShelf.keys())))		-- uncomment to make list copy to real clipboard
		print list(mcbShelf.keys())

	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		print "\"%s\" clipboard has copied to your original clipboard, press Ctrl+v to paste!" % (sys.argv[1])




mcbShelf.close()

