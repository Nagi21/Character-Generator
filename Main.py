import string

RACE_LIST = []
CLASS_LIST = []
ALIGNMENTS = ['chaotic good', 'neutral good', 'lawful good', 'lawful neutral', 'true neutral', 'chaotic neutral', 'lawful evil', 'neutral evil', 'chaotic evil']

def main():
	mainMenu = -1
	while mainMenu != 0:
		print("1. Generate Characters \n0. Quit")
		userSelection = int(input("Enter Selection: "))
		if userSelection == 0:
			mainMenu = 0
		elif userSelection == 1:
			numCharGenerated = int(input("How many characters are needed?"))
			for x in numCharGenerated:
				levelSelection = int(input("What level for character %s?".format(x)))
				raceSelection = input("What race for character %s?".format(x)).lower()
				classSelection = input("What class for character %s?".format(x)).lower()
				alignmentSelection = input("What alignment for character %s?".format(x)).lower()
				if raceSelection not in RACE_LIST:
					#randomly select race
				if classSelection not in CLASS_LIST:
					#randomly select class
				if alignmentSelection not in ALIGNMENTS:
					#randomly select alignment
				#make list to store character objects after creation
			