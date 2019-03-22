from pathlib import Path

# list all files in the current directory
path = Path()
for file in path.glob('*'):
    print(file)


# Creates a new directory, if directory does not exist
path = Path("python-workspace/MoshTutorial/emails")
print(path.exists())
if path.exists() == False:
    print("Folder doesn't exist")
    print("creating a new folder")
    path.mkdir()
    print("folder created..")


# remove directory
remove = True
if remove:
    path.rmdir()
    print("directory '" + str(path) + "' is removed")
