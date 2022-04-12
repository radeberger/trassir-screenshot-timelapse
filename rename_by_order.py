import os

os.chdir('f:\\Trassir\\screenshots')
print(os.getcwd())
COUNT = 0


# Function to increment count
# to make the files sorted.
def increment():
    global COUNT
    COUNT = COUNT + 1


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = "image" + str(COUNT).zfill(6)
    increment()

    new_name = '{}{}'.format(f_name, f_ext)
    print(new_name)
    os.rename(f, new_name)