import os
class UtilPostgres:

	def getMenu(self):

		content ="Proccess PostgreSQL\n"
		content += "1. Backup\n"
		content += "2. Restore\n"
		content += "Selection ->"

		menu=raw_input(content)
		print menu



obj=UtilPostgres()
obj.getMenu()
