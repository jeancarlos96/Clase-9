import time 

for x in range (1, 61):
	print (x)

t= time.localtime()
s=t[4]
print ("imprimir un numero cada segundo")
for s in range (1,61):
	print(s)
	time.sleep(1)