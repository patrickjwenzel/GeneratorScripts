import string
import random

lc = string.ascii_lowercase
uc = string.ascii_uppercase
nums = [0,1,2,3,4,5,6,7,8,9]
sc = ['!','@','#','$','%','^','&','*']

p = ''

for i in range(0,15):
	n = random.randint(1, 100)
	if n <= 65:
		x = random.randint(1, 100)
		ri = random.randint(0, 25)
		p += lc[ri] if x <= 65 else uc[ri]
	elif n <= 85:
		ri = random.randint(0, 9)
		p += str(nums[ri])
	else:
		ri = random.randint(0, len(sc) - 1)
		p += sc[ri]

print(p)