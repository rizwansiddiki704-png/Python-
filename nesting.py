aliens = [ ]

for alien_number in range(30):
	new_alien ={'color':'blue','point':21,'speed':'fast'}
	aliens.append(new_alien)
	
for alien in aliens [:5]:
	if alien['color'] =='blue':
		alien['color'] ='black'
		alien['speed'] ='medium'
		alien['point'] = 15
		
for alien in aliens[:10]:
	print (alien)
print ("...")