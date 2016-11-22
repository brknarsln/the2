#the2

def stnd():
	count=0
	while (count==0):
		#print ('Ogrenci numarasi giriniz! (orn: 123456-7)')
		#print ('Cikmak icin "q" yaziniz!')
		stud = raw_input()
		
		if stud=='q':
			count=1
			pass
		else:
			x = [str(b) for b in stud]			
			if len(x)==8:
				a = x.index('?')
				if a!=6:
					del x[6];
					if x[a]==1:

						
						
						pass

					pass
				pass
			pass

		pass