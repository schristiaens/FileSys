import os, sys

content = {'drive': [], 'folder': [], 'text': [], 'zip': [] }
##### Begin Entity Class #####
 
class Entity(object):
	def __init__(self, Type=None, Name=None, Parent=None, Size=0):
		if Type not in content:
			print 'Invalid type \"%s\"' % Type
			return False
		self.type = Type

		if Type is 'drive' and Parent is not None:
			print 'Illegal File System Operation'
			return False
		if Type is not 'drive' and Parent is None:
			print 'Illegal File System Operation'
			return False

		self.parent = find_parent(Parent)

		#self.parent.children.append(self)

		if Parent is not None:
			if Name in Parent.children:
				print 'Path \"%s\\%s\" already exists' % Parent, Name
				return False
		self.name = Name
		
		self.children = []
		return 

	def find_parent(self, parentName):
			for d in content['drive']:
				if parentName == d.name:
					return d
			for f in content['folder']:
				if parentName == f.name:
					return f
			for z in content['zip']:
				if parentName == z.name:
					return z
			return False

	def __get_size(self):
		if self.type is 'drive':
			print 'drive size'
		elif self.type is 'folder':
			print 'folder size'
		elif self.type is 'text':
			print 'text size'
		elif self.type is 'zip':
			print 'zip 1/2 size'
		return 0

	def write(self, writing):
		if self.type is not 'text':
			return False
		self.content = str(writing)
		return True

	def path(self, fullPath=''):
		if self.parent is None:
			fullPath = self.name
		else:
			self.parent.path(fullPath)
			fullPath += '\\' + self.name
		return fullPath


##### End Entity Class #####

def create(Type, Name, PathOfParent = None):
	created = Entity(Type=Type, Name=Name, Parent=PathOfParent)
	if created:
		content[Type].append(created)
		return True
	else: 
		return False

def delete(Path):

	return

def move(SrcPath, DstPath):

	return

def write_to_file(Path, Content):

	return

def size(Path):

	return

def main():

	try:
		create('drive', 'drive1')
		create('folder', 'folder1', 'drive1')
		create('text', 'file1', 'folder1')
		create('zip', 'zip1', 'folder1')
		create('zip', 'zip1', 'folder1')
		return 0
	except Exception, e:
		sys.stderr.write('ERROR: %s\n' % str(e))
		pass
	finally:
		print content

	

# Template to start the program
if __name__ =='__main__':
	main()
	sys.exit(0)

