import os

ext1 = ""
ext2 = "txt"
i = 1
# dir = 'C:\\Users\\nUser\\Pictures\\123'
dir = 'C:\\Users\\nUser\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu20.04LTS_79rhkp1fndgsc\\LocalState\\rootfs\\home\\BreachCompilation_Last\\data'
for file in os.listdir(dir):
    if file.endswith(ext1):
        os.rename(f'{dir}/{file}', f'{dir}/{i}.{ext2}')
        i = i + 1
