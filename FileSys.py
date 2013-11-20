# By: Steve Christiaens
# November 20, 2013
# Written for Proofpoint interview

import os, sys

content = {'drive': [], 'folder': [], 'text': [], 'zip': [] }
##### Begin Entity Class #####
 
class Entity(object):
	def __init__(self, Type=None, Name=None, Parent=None, Size=0):
		if Type not in content:
			raise Exception('Illegal File System Operation')
			return False
		self.type = Type
		
		if self.type is 'text':
			self.content = '1234567890'

		if not self.__parent_checks(Type, Parent):
			raise Exception('Illegal File System Operation')
			return False

		if Parent is not None:
			self.parent = self.__find_parent(Parent)
		
		if Parent is not None:
			if Name in str(self.parent.children):
				raise Exception('Path \"\\%s\\%s" already exists.' % (Parent,Name))
				 
		
		if Type is not 'drive':
			self.parent.children.append(self)
		self.children = []
		self.name = Name

		
		return 

	def __repr__(self):
		return self.name

	def __parent_checks(self, Type, Parent):
		if Type is 'drive' and Parent is not None:
			return False
		if Type is not 'drive' and Parent is None:
			return False
		return True

	def __find_parent(self, parentName):
			for d in content['drive']:
				if parentName == d.name:
					return d
			for f in content['folder']:
				if parentName == f.name:
					return f
			for z in content['zip']:
				if parentName == z.name:
					return z
			raise Exception('Path not found \"%s\\".' % parentName)

	def write(self, writing):
		if self.type is not 'text':
			raise Exception('Not a text file')
		self.content = str(writing)
		print "Wrote successfully"
		return

	def path(self, fullPath=''):
		if self.type is 'drive':
			fullPath = self.name
		else:
			fullPath += self.parent.path(fullPath) + '\\' + self.name
		return fullPath

	def size(self, total=0, mult=1):
		# Need to implement checks for drives/folders w/no children
		if self.type is 'drive':
			for child in self.children:
				total = child.size(total) * mult 
		if self.type is 'folder':
			for child in self.children:
				total = child.size(total) * mult
		elif self.type is 'text':
			total += len(self.content) * mult
		elif self.type is 'zip':
			for child in self.children:
				total = child.size(total, .5)
		return total

##### End Entity Class #####

def create(Type, Name, PathOfParent = None):
	created = Entity(Type=Type, Name=Name, Parent=PathOfParent)
	if created:
		content[Type].append(created)
		return True
	else: 
		return False

def delete(Path):
	# Get object reference using Path
	# Path.parent.children.remove(Path) # remove parent ref to child
	#
	# for child in Path.children: # remove all children
	#	delete(child.path)
	#
	# delete object # remove self
	return

def move(SrcPath, DstPath):
	# Get object references using SrcPath, DstPath
	# srcPath.parent.children.remove(srcPath) # remove reference from original parent
	# srcPath.parent = DstPath # change parent
	# srcPath.parent.children.append(srcPath) # let parent know it has a new child

	return

def write_to_file(Path, Content):
	# Get object reference using Path
	# Path.write(Content)
	return

def size(Path):
	totalSize = Path.size()
	return totalSize

def main():

	try:
		# Create a basic collection of files and show the size() function.
		create('drive', 'drive1')
		create('folder', 'folder1', 'drive1')
		create('zip', 'zip1', 'folder1')
		create('text', 'file1', 'zip1')
		create('text', 'file2', 'zip1')
		create('text', 'file3', 'zip1')
		create('text', 'file1', 'folder1')
		
		#create('drive', 'drive2', 'folder1') # Create drive w/a parent directory
		#create('zip', 'zip1', 'folder8') # Create zip w/non-existent parent
		#create('zip', 'zip1', 'folder1') # File already exists
		
		print 'Drives created:'
		for d in content['drive']: print d.path()
		print '\nFolders created:'
		for f in content['folder']: print f.path()
		print '\nText Files created:'
		for t in content['text']: print t.path()
		print '\nZip Files created:'
		for z in content['zip']: print z.path()

		for drive in content['drive']:
			print '\nSize of drive \'%s\' is %d' %(drive, size(drive))
		return 0
	except Exception, e:
		sys.stderr.write('ERROR: %s\n' % str(e))
		pass

# Template to start the program
if __name__ =='__main__':
	main()
	sys.exit(0)

