#!/usr/bin/env python
# File: exportPDF.py - PDF export profile for scribus document
# 2011.06.13 Cedric Gemy
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

'''
USAGE
- prepare the book file containing the list of files
- launch the script to choose your action

RELEASE :
v1.0 : 	- updated page numbers
		- export for print and web all the files in a single

TODO
- see method list :
	- define a master doc
- add a window to define the quality of exported PDF
- add a window to define the PDF output directory
- add a setting to define PDF output name and suffix (for multiple export)
- # pdftk option "background stamp.pdf" adds the background to every page
- Change ui to qt asap API allows it
- add an option to add blank page if needed between files

'''

from lxml import etree
import scribus
import re
import os
import subprocess
#import exportPDF

class book:
	def __init__(self):
		#scribus.messageBox("Debut",'Init',icon=0,button1=1)
		# loads the file
		try: 
			#scribus.messageBox("Debut","try OK : fichier charge dans Books",icon=0,button1=1)
			self.outputfile = scribus.fileDialog('Choose book file', filter='Book Files (*.sla.bk);;All Files (*)')
			#self.books = etree.parse("/home/cedric/.scribus/plugins/bookfiles/guideapi.sla.bk")
			self.books = etree.parse(self.outputfile)
		except Exception, e:
			scribus.messageBox("Debut",e,icon=0,button1=1)
		# etree.tostring(book) # display the whole file
		self.root = self.books.getroot() # gets the root element that can be displayed with root.tag
		self.thing=""
		self.pdffiles=""
		self.action=scribus.valueDialog("Book handling","0=SyncPageNumber, 1=Export All","1")
		result = {
			"0": self.syncPageNumbers(),
			"1": self.exportAll2PDF()
		}
		#result.get(int(self.action))
		#self.syncPageNumbers()
		#self.exportAll2PDF()
	
	def parse():
		for element in self.root.iter("file"):
			files = element.text
			self.thing = etree.parse(files)

		
	def makeMaster():
		print ""
		# root = etree.Element("root", interesting="totally")  // insert an interesting attributes with totally value: to be used for isMaster
	
	def isMaster():
		print ""
		# root.get("interesting") // gets the value of the attributes
		# root.set("interesting", "somewhat") // set a new value to the attributes
	
	def syncStyles():
		print ""
		# scribus.getAllStyles()comparer les styles et laisser choisir ou faire automatic pour les styles aux noms identiques
		# remplace auto les styles au nom identique
		# display les styles uniques pour remplacement
		# scribus.loadStylesFromFile("filename")
	
	def syncMasterPage():
		# list of master page should be displayed in the window in L (for Left) and R (for Right) with scribus.masterPageNames(...)
		print ""
			
	def getPages():
		print ""
		# scribus.pageCount(...)
		
	def addFile():
		print ""
		# root.insert(0, etree.Element("child0")) // insert child0 at the beginning
		# root.append( etree.Element("child1") ) // adds a child element tagged child1
		
	def delFile():
		print ""

	def createBook():
		print ""
#		texte = """<html>
#<title>informations personnelles</title>
#<head>
#<body>
#vous etes monsieur :"%s" "%s"
#</body>
#</head>
#</html>""" % (a,b)#
#
#x=open('site.html','w')
#x.write(texte)
#x.close()
	
	def export2PDF(self):
#		PDF=exportPDF()
		self.pdfExport = scribus.PDFfile()
		self.pdfExport.info = "Scribus PDF export engine"
		self.pdfExport.version = 14 #PDF 1.4
		self.pdfExport.pages = self.pageList()
		#self.exportWeb()
		#self.exportPrint()
		
	def exportAll2PDF(self):
		self.textfile=""
		self.filenames=""
		#outputfile = scribus.fileDialog('Enter name of file to save to', filter='PDF Files (*.pdf);;All Files (*)')
		for element in self.root.iter("file"):
			scribus.openDoc(str(element.text))
			filename = os.path.splitext(os.path.basename(element.text))
			#self.filenames=self.filenames+" "+filename[0]
			#scribus.messageBox("Export PDF",self.filenames,icon=0,button1=1)
			self.textfile = "/tmp/"+filename[0]+".pdf"
			#files+= self.textfile+" "
			self.export2PDF()
			self.exportWeb()
			scribus.closeDoc()
		#try:
			######### POUR INSTANT PROBLEME AVEC REALISATION DU MERGE ###########
			#pdftkargs = self.pdffiles +" cat output "+ outputfile #"output /home/cedric/Bureau/perso/clients/adapro/Vtest/"+outputfile+".pdf"
			#pdftkargs = self.filenames+" cat output /tmp/output.pdf" #"output /home/cedric/Bureau/perso/clients/adapro/Vtest/"+outputfile+".pdf"
			#subprocess.call(["pdftk", pdftkargs])
		#	scribus.messageBox("Export PDF OK",pdftkargs,icon=0,button1=1)
		#except Exception,e :
		#	scribus.messageBox("Export PDF Error",e,icon=0,button1=1)
			
		
	
	def pageList(self):
		listOfPages = []
		i = 0
		while (i < scribus.pageCount()):
			i = i + 1
			listOfPages.append(i)
		return listOfPages
	
	def exportWeb(self):
		self.pdfExport.compressmtd = 1
		self.pdfExport.downsample = 72
		self.pdfExport.quality = 1 #0 = max -> 4=min
		self.pdfExport.outdst = 0 #screen | 1 = printer
		self.pdfExport.file = str(self.textfile)
		self.pdffiles+=self.textfile+" "
		self.pdfExport.save()

	def exportPrint(self):
		self.pdfExport.compressmtd = 2
		self.pdfExport.bleedl = 14
		self.pdfExport.bleedr = 14
		self.pdfExport.bleedt = 14
		self.pdfExport.bleedb = 14
		self.pdfExport.downsample = 300
		self.pdfExport.quality = 0 #0 = max -> 4=min
		self.pdfExport.outdst = 1 #screen | 1 = printer
		#pdfExport.pages = self.pageList()
		self.pdfExport.file = str(self.textfile+"Print.pdf")
		self.pdfExport.save()



	def syncPageNumbers(self):
		scribus.messageBox("Debut",'Apply page numbers',icon=0,button1=1)
		i=0
		totalpages=1
			# parses the book file; for each book document
		for element in self.root.iter("file"):
			files = element.text
			thing = etree.parse(files)
			#scribus.messageBox("Debut",str(files),icon=0,button1=1)

			rawstr = r"""Start=".+" R"""
			matchstr=etree.tostring(thing)
			compile_obj=re.compile(rawstr)
			textpage = 'Start="'+str(totalpages)+'" R'
			newstr=compile_obj.subn(str(textpage),etree.tostring(thing))

			# Open file in Scribus to get the page quantity for each file through scribus own method
			doc = scribus.openDoc(files)
			pageqty = scribus.pageCount()
			totalpages += pageqty #sets the amount of page from the beginning of the first file
			scribus.closeDoc()
			#scribus.messageBox("Debut","begins at "+str(newstr[0]),icon=0,button1=1)
			
			FILE = open(files,"w")
			FILE.write(newstr[0])
			FILE.close()

if __name__ == '__main__':
	#scribus.messageBox("Debut",'Debut',icon=0,button1=1)
	app = book()
	#PDF = exportPDF()

#if scribus.haveDoc():
#	try:
#		app = book()
#	except Exception, e:
#		print e

#else:
#	scribus.messageBox('Export Error', 'You need a Document open, and a frame selected.', \
#					icon=0, button1=1)
