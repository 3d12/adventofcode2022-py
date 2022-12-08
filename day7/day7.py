from ..file_reader import read_file_into_list

def parse(line):
    line_stripped = line.replace('\n','')
    return line_stripped

class FileSystem_File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name

    def __str__(self):
        return f"{str(self.size)} {self.name}\n"

class FileSystem_Folder:
    def __init__(self, name, parent):
        self.name = name
        self.contents = []
        self.parent = parent

    def __repr__(self):
        return self.name

    def __str__(self, indent=0):
        strToReturn = (' ' * indent) + '- ' + self.name + '\n'
        for elem in self.contents:
            if type(elem) == FileSystem_Folder:
                 strToReturn += elem.__str__(indent+4)
            else:
                strToReturn += (' ' * (indent+4)) + '- ' + elem.__str__()
        return strToReturn

    def getTotalSize(self):
        total = 0
        for elem in self.contents:
            if type(elem) == FileSystem_Folder:
                total += elem.getTotalSize()
            else:
                total += elem.size
        return total

class FileSystem:
    def __init__(self):
        self.fs = FileSystem_Folder('/', None)
        self.current_working_directory = self.fs

    def __str__(self):
        return self.fs.__str__()

    def goToRoot(self):
        self.current_working_directory = self.fs

    def changeDirectory(self, newDir):
        if newDir == '..':
            self.current_working_directory = self.current_working_directory.parent # pyright: ignore
            return
        self.createDirectory(newDir)
        self.current_working_directory = next(elem for elem in self.current_working_directory.contents if elem.name == newDir) # pyright: ignore

    def createDirectory(self, newDir):
        if newDir not in [elem.name for elem in self.current_working_directory.contents]: # pyright: ignore
            self.current_working_directory.contents.append(FileSystem_Folder(newDir, self.current_working_directory)) # pyright: ignore

    def createFile(self, fileSize, fileName):
        self.current_working_directory.contents.append(FileSystem_File(fileSize, fileName)) # pyright: ignore

    def getChildDirectories(self, startDir):
        childDirs = [elem for elem in startDir.contents if type(elem) == FileSystem_Folder] # pyright: ignore
        if len(childDirs) == 0:
            return childDirs
        for elem in childDirs:
            elemChildDirs = self.getChildDirectories(elem)
            for childDir in elemChildDirs:
                if childDir not in childDirs:
                    childDirs.append(childDir)
        return childDirs

    def getAllDirectories(self):
        return self.getChildDirectories(self.fs)

    def getAllDirectorySizes(self):
        dirs = self.getAllDirectories()
        sizes = []
        for elem in dirs:
            sizes.append({ 'folderName': elem.name, 'folderSize': elem.getTotalSize() })
        return sizes




input_list = read_file_into_list('day7/input.txt', parse)

input_list = input_list[1:] # pyright: ignore

test = FileSystem()

for instruction in input_list:
    instruction_split = instruction.split()
    # we only care about the cd command
    if instruction_split[0] == '$':
        if instruction_split[1] == 'cd':
            test.changeDirectory(instruction_split[2])
    elif instruction_split[0] == 'dir':
        test.createDirectory(instruction_split[1])
    else:
        test.createFile(instruction_split[0], instruction_split[1])

# total
test.goToRoot()
print(test)

print(test.getAllDirectorySizes())

answer = sum([int(elem['folderSize']) for elem in test.getAllDirectorySizes() if int(elem['folderSize']) < 100000])

print(f"The answer is: {answer}")
