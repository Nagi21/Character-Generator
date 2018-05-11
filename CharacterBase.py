

class CharacterBase:
	def __init__(self, level, race, cClass, alignment):
		self.name = ""
		self.level = level
		self.race = race
		self.cClass = cClass
		self.alignment = alignment
		
		self.proBonus = 0
		
		self.strength = 0
		self.dexterity = 0
		self.constituation = 0
		self.intelligence = 0
		self.wisdom = 0
		self.charisma = 0
		
		self.hp = 0
		self.ac = 0
		
		self.acrobatics = 0 
		self.animalHanding = 0 
		self.arcana = 0
		self.athletics = 0
		self.deception = 0 
		self.history = 0
		self.insight = 0
		self.intimidation = 0
		self.investigation = 0
		self.medicine = 0
		self.nature = 0 
		self.perception = 0
		self.performance = 0
		self.persuasion = 0
		self.religion = 0
		self.sleight = 
		self.stealth = 0
		self.survival = 0
		
		self.traits = []
		self.feats = []
		self.weapons = []