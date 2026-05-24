users ={
    'khabib.ufc':{
    'first' : 'khabib',
    'last' : 'norgamadov',
    'location':'dagestan',
    },
    
    'islam.ufc':{
    'first': 'islam',
    'last': 'makachev',
    'location': 'dagestan',
    },
    'magomad.ufc':{
    'first': 'magomad',
    'last' : 'ankalayev',
    'location': 'dagestan',
    },
}
for username,user_info in users.items():
	print(f"\nUsername : {username}")
	full_name = f"{user_info['first']} {user_info['last']}" 
	location= user_info['location']
	
	print(f"\tFull name:{full_name.title()}")
	print(f"\tLocation:{location.title()}")
	