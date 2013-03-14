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

    def __init__(self, HTMLImportRead_ParsedTree):
        # Bind class to active Scribus document
        self.document = None
#        self.document = Scripter.activeDocument
        # Bind class to HTML Tree parsed by lxml.etree and handled by
        # ScribusHTMLImportRead class
        self.HTMLTree = HTMLImportRead_ParsedTree


    def importHTML(self, parsedHTMLTree):
        self.setTextDestination()
        

    def setTextDestination(self):
        # Use first selected text frame as destination
#        for item in self.document.activePage.selection:
#            if isinstance(item, Scripter.TextAPI):
#                self.textDestination = item
#                break
        return


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
            if isinstance(elem, basestring):
                # If elem is a string, we are ready for param evaluation
                categoryAccess = None
                for category in categoryPathList:
                    if category == "":
                        if indentLevel == 1:
                            # There is no category, the element is at top level
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
        infos.pop()
                                                         
        return "\n".join(infos)


