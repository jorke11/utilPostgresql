import os
class UtilPostgres:

	def getMenu(self):

		content ="Proccess PostgreSQL\n"
		content += "1. Backup\n"
		content += "2. Restore\n"
		content += "3. Salir\n"
		content += "Selection ->"

		menu=raw_input(content)

		if(menu==3){
			break;
		}


obj=UtilPostgres()
obj.getMenu()
