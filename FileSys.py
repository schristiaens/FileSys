import os, sys

content = {'drive': [], 'folder': [], 'text': [], 'zip': [] }
##### Begin Entity Class #####
 
class Entity(object):
    def __init__(self, Type=None, Name=None, Parent=None, Size=0):
        self.type = Type
        self.name = Name
        self.parent = Parent
        self.children = []
    	return

    def size():
    	if self.type is 'drive':
    		print 'drive size'
    	elif self.type is 'folder':
    		print 'folder size'
    	elif self.type is 'text':
    		print 'text size'
    	elif self.type is 'zip':
    		print 'zip 1/2 size'
    	return 

##### End Entity Class #####

def create(Type, Name, PathOfParent = None):
	if Type not in content:
		print 'Invalid entity type \"%s\".\n' % Type
		return
	
	for value in content[Type]:
		if Name in value['name']:
			print '%s already exists.' % Name
			return

	Name = {'type': Type, 'name': Name, 'parent': PathOfParent}
	if Type == 'text':
		Name['content'] = ''

	content[Type].append(Name)
	return Name

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

