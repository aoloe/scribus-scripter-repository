# -*- coding: utf-8-unix;  -*-
# Above line defines encoding : http://www.python.org/dev/peps/pep-0263/

'''
Copyright (C) 2013 A. Rimoldi <a.l.e@ideale.ch>
                   C. Gémy <cedric@cgemy.com>
                   C. Schockaert <R3vLibre@citadels.be>

##This extension draws a typographic grid for use within Scribus documents.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from lxml import etree
from lxml import html
'''
>>> tree = etree.parse('file.html')
>>> tree.getroot()

Clean HTML Code
>>>from lxml.html.clean import Cleaner
>>> cleaner = Cleaner(page_structure=False, links=False)
>>> print cleaner.clean_html(html)

root.xpath("//article[@type='news']")
root.getchildren()
'''

class Styles():
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name
	def getName(self):
		return self.name

class CarStyles(Styles):
	def __init__(self, name):
		self.name = name
		#super(CarStyles,self).__init__(name)
	'''def __unicode__(self):
		return self.name
		#return super(CarStyles,self).__unicode__(name)
	def get_name():
		return self.name'''

class ParaStyles(Styles):
	def __init__(self,name):
		self.name = name
		#super(ParaStyles,self).__init__(name)
	'''def __unicode__(self):
		return self.name
		#return super(ParaStyles,self).__unicode__(name)
	def get_name():
		return self.name'''

class Text():
	def __init__(self):
		self.paragraphs=[]
	def add_para(self,para):
		self.paragraphs.append(para)

        def getParagraphs(self):
                return self.paragraphs

class Paragraph():
	def __init__(self,style):
		self.style = style
		self.text_chunks = []
	def add_text_chunk(self,text,carstyle):
		text_chunk = (text,carstyle)
		self.text_chunks.append(text_chunk)
	def getStyle(self):
		return self.style

        def get_text_chunks(self):
                return self.text_chunks

class ScribusHTMLImportRead():
	car = ['b','i','span','a','u','cite']
	para = ['h1','h2','p','ul','li','ol','pre','address','blockquote']
	
	def __init__(self):
		file='/home/r3vlibre/dev/Scribus/scripter.git/html_import/examples/ch008_le-principe-du-montage.txt'
		self.htmlfile=etree.parse(file)
		# attention aux entites html avec le parsing xml
		self.root = self.htmlfile.getroot()
#		self.text = ()
		self.tags = ()
		self.paragraphs_and_tags = []
		self.text_content=""

	def top_elements(self):
		''' Get top level elements : generally might be html, in Fmfr is h1 '''
		for elem in self.root:
			print unicode(elem.tag) +" : "+ unicode(elem.text)+" : TAIL : " +unicode(elem.tail)
	
	def get_styles(self):
		#self.classes = self.root.xpath('//@class')
		car_expr = '(//b/@class|//i/@class|//span/@class|//a/@class|//u/@class|//cite/@class)'
		para_expr = '(//h1/@class|//h2/@class|//p/@class|//li/@class|//pre/@class|//address/@class)'
		car_styles=list(set(self.root.xpath(car_expr)))
		para_styles= ScribusHTMLImportRead.para+list(set(self.root.xpath(para_expr)))
		self.styles = {'car':[],'par':[]}
		for style_name in car_styles:
			self.styles['car'].append(CarStyles(style_name)) 
		for style_name in para_styles:
			self.styles['par'].append(ParaStyles(style_name))
		#'car':car_styles, 'para':para_styles}
		return self.styles
	
	def parse_childs(self,elem, paragraph):
		print "parse_childs('" + str(elem) + "', '" + str(paragraph) +"')"
		if elem.tag in ScribusHTMLImportRead.para : 
			print "Creating para for '" + str(elem.tag) +"'" 
                        paragraph = Paragraph(ParaStyles("Para_StyleToDefine"))
		
		for field in elem.iterchildren(): 
			if field.tail == None :
				field.tail = ""
			if field.text == None:
				field.text = ""
			print '<%s>: [%s] {%s}' % (field.tag.strip(), field.text.strip(), field.tail.strip())
			if field.tag not in ScribusHTMLImportRead.para:
				print "Adding text_chunk for '" + str(field.tag) +"'" 				
				paragraph.add_text_chunk(field.text,CarStyles("carstyle"))
			self.parse_childs(field, paragraph)
		if elem.tag in ScribusHTMLImportRead.para : 
			print "Adding the para for '" + str(elem.tag) +"'" 
			self.text.add_para(paragraph)
		return
				
	def html_read(self):
		self.text = Text()
		self.parse_childs(self.root, None)
		return

        def getText(self):
                return self.text



htmlimport = ScribusHTMLImportRead()
for style in htmlimport.get_styles()["car"]:
	print str(style)
for style in htmlimport.get_styles()["par"]:
	print str(style)

#htmlimport.html_read()
#print htmlimport.text_content


##htmlimport.top_elements()
