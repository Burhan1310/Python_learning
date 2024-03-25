from pathlib import Path

# path = Path('burhan')
# print(path.exists())
#
# path = Path('burhan')
# print(path.mkdir())

# print(path.rmdir())

path = Path()
# print(path.glob('*.py'))
for files in path.glob("*.py"):
    print(files)