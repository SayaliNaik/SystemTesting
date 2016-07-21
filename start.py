import sys
import webbrowser
from time import sleep

def start():
	files = ["learn-future","bbtst1.txt","bbtst2.txt","bbstg1.txt","bbstg2.txt"]
	i = int(sys.argv[1])
	with open(files[i],"r") as f:
		while True:
			line = f.readline()
			if line:
				webbrowser.open(line,new=0,autoraise=True)
				sleep(8)
			else:
				if i == 1:
					print("Done with BBTST1")
				elif i == 2:
					print("Done with BBTST2")
				elif i == 3:
					print("Done with BBSTG1")
				elif i == 4:
					print("Done with BBSTG2")
				else:
					print("Done with learn-future")
				break;
start()
            