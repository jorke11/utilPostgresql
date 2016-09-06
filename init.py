import os,string,commands,configparser,os.path

class UtilPostgres:

	def __init__(self):
		a = open("config.ini","a")
		os.system("chmod 0777 config.ini");
		a.close();
		

	def getMenu(self):

		while True:
		
			content ="Proccess PostgreSQL\n"
			content += "1. Backup\n"
			content += "2. Restore\n"
			content += "3. Config pg_dump\n"
			content += "4. Config pg_restore\n"
			content += "5. Exit\n"
			content += "Selection ->"

			menu=raw_input(content)
		
			if menu=="1":
				os.system('clear')
				print "Data Backup\n"
				content = "Database:"
				db=raw_input(content)
				content = "Path destination: "
				path=raw_input(content)
				self.backUp(db,path)
				print db + " " + path
			elif menu=="2":
				os.system('clear')
				print "Data Restore\n"
				content = "Database:"
				db=raw_input(content)
				content = "Path file: "
				path=raw_input(content)
				self.restore(db,path)
			elif menu=="3":
				self.pg_dump()

			elif menu == "4":

				self.pg_restore()

			elif menu == "5":
				print "End!"
				break;
	
	def pg_dump(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		print "Looking bin wait ...."
		paths = commands.getstatusoutput('find / -name pg_dump')
		os.system('clear')
		paths = paths[1].split("\n")

		for ind in range(len(paths)):
			print str(ind + 1) + " " + paths[ind]


		if 'pg_dump' in config:
			content = "Selection Bin("+config.get("pg_dump","path")+"): "
		else:
			content = "Selection Bin: "
		
		sel = raw_input(content)

		for ind in range(len(paths)):
			if str(sel) == str(ind + 1):
				binario = paths[ind]
		
		if 'pg_dump' not in config:
			config.add_section('pg_dump')
			
			
		config.set("pg_dump","path",binario)


		with open('config.ini', 'w') as archivoconfig:
			config.write(archivoconfig)

		os.system('clear')
		print "Path update: "+config.get("pg_dump","path")+"\n"

	def pg_restore(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		print "Lookin bin Wait ...."
		paths = commands.getstatusoutput('find / -name pg_restore')
		os.system('clear')
		paths = paths[1].split("\n")

		for ind in range(len(paths)):
			print str(ind + 1) + " " + paths[ind]

		if 'pg_restore' in config:
			content = "Selection Bin:("+config.get("pg_restore","path")+") "
		else:
			content = "Selection Bin: "
			
		sel = raw_input(content)

		for ind in range(len(paths)):
			if str(sel) == str(ind + 1):
				binario = paths[ind]
		
		if 'pg_restore' not in config:
			config.add_section('pg_restore')
			
			
		config.set("pg_restore","path",binario)


		with open('config.ini', 'w') as archivoconfig:
			config.write(archivoconfig)

		os.system('clear')
		print "Path update: "+config.get("pg_restore","path")+"\n"


	def backUp(self,db,path):

		config = configparser.ConfigParser()
		config.read('config.ini')

		if path.find(".backup")==-1:
			name= db +'.backup '
			path+=name
			print "Try create file in: " + path

		if 'pg_dump' in config:
			bk=config.get("pg_dump","path")+' -i -h localhost -p 5432 -U postgres -F c -b -v -f ' + path + ' ' + db;
		else:
			bk =  "****** Pendiente configurar BIN pg_dump ******\n"
		os.system("clear")
		print bk



	def restore(self,db,path):
		config = configparser.ConfigParser()
		config.read('config.ini')
		

		if 'pg_restore' in config:
			bk = config.get("pg_restore","path")+" -i -h localhost -p 5432 -U postgres -d " + db +" -v "+ path
		else:
			bk =  "****** Pendiente configurar BIN pg_restore ******\n"
		os.system("clear")
		print bk

obj=UtilPostgres()
obj.getMenu()
