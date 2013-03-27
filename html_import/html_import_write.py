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

class ScribusHTMLImportWrite(object):

    def __init__(self):
        # Bind class to active Scribus document
#        self.document = None
        self.document = Scripter.activeDocument
        self.HTMLTree = None
        self.HTMLText = ""


    def importHTML(self, parsedHTMLTree):
        # Bind class to HTML Tree parsed by lxml.etree and handled by
        # ScribusHTMLImportRead class
        self.HTMLTree = parsedHTMLTree
        self.HTMLTree.html_read()
        self.setTextDestination()
        self.createStyles()
        self.addTextAndStyles()
        self.setHTMLTextInFrame()


    def setTextDestination(self):
        """Use selected text frame as destination -- only one frame allowed"""
        items = self.document.activePage.selection
        print "items='" + str(items) +"'"
        if len(items) != 1:
            print "One and only one item must be selected"
            return

        # Check if frame is a text frame
        try:
            print "TextLength = " + str(items[0].textLength)
            self.textDestination = items[0]
        except AttributeError:
             print "Item selected must be a text frame"
             return
        
        # Use this portion of code when path to TextAPI is found
        #   -- it is not declared within Scripter
        # if isinstance(items[0], Scripter.TextAPI):
        #     self.textDestination = items[0]
        # else:
        #     print "Item selected must be a text frame"
        #     return

        return


    def createStyles(self):
        print "Creating styles -- not implemented yet"
        return


    def addTextAndStyles(self):
#        for paragraph in self.HTMLTree.getText().getParagraphs():
        text = self.HTMLTree.getText()
        print "text = " + str(text)
        for paragraph in text.getParagraphs():
            self.HTMLText = self.HTMLText + "[:ParaStyle = " \
                + paragraph.getStyle().getName() + ": "
            for (text, carStyle) in paragraph.get_text_chunks():
                self.HTMLText = self.HTMLText + "{:CarStyle = " \
                    + carStyle.getName() + ": " + text \
                    + " :" + carStyle.getName() + ":}"
            self.HTMLText = self.HTMLText + " :" \
                + paragraph.getStyle().getName() + ":]"
        return


    def setHTMLTextInFrame(self):
        try:
            self.textDestination.insertText(self.HTMLText, 0)
        except AttributeError:
            print "A text frame must be selected for HTML import"


### Routines for tests and debug ###
    def describeParams(self, paramsList, categoryPathList = []):
        """Return a list of strings describing key/value pairs for parameters 
within a parameters list."""
        indentSize = 2

        paramsDescription = []
        indentLevel = len(categoryPathList)
        indent = ' ' * indentLevel * indentSize
#        print "paramsList = " + str(paramsList)
#        print "categoryPathList = " + str(categoryPathList)
#        print "indentLevel = " + str(indentLevel)
        for elem in paramsList:
#            print "elem = "+ str(elem)
            if isinstance(elem, basestring):
                # If elem is a string, we are ready for param evaluation
                categoryAccess = None
                for category in categoryPathList:
                    try:
                        if category == "":
                            if indentLevel == 1:
                                # There is no category, 
                                # the element is at top level
                                elemValue = getattr(self, elem)
                            else:
                                # categoryAccess is already well set 
                                elemValue = categoryAccess[elem]
                        elif categoryAccess == None:
                            categoryAccess = getattr(self, category)
                            elemValue = categoryAccess[elem]
                        else:
                            categoryAccess = categoryAccess[category]
                            elemValue = categoryAccess[elem]
                        Description = indent + elem + " = " + str(elemValue)
                        paramsDescription.append(Description)
                    except AttributeError:
                        pass
            else:
                # There are more nesting levels in the categories
                (CategoryName, categoryId, categoryParamsList) = elem
                paramsDescription.append(indent + CategoryName + ":")
                pathList = list(categoryPathList)
                pathList.append(categoryId)
                paramsDescription.extend(self.describeParams(categoryParamsList,
                                                             pathList))
                # Group top-level categories by sets
                if indentLevel == 0:
                    paramsDescription.append("")

        return paramsDescription


    def displayInfos(self):
        """Generate a summary string of grid specifications"""
        paramsList \
            = [("Init",
                "", 
                ["document", "HTMLTree"])]


        infos = [ ]
        infos.extend(self.describeParams(paramsList))
                    
        # Remove the last blank record added after each top-level category
        if len(infos) > 0:
            infos.pop()
                                                         
        return "\n".join(infos)


