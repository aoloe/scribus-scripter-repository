#! /usr/bin/env python
# -*- coding: utf-8-unix;  -*-
# Above line defines encoding : http://www.python.org/dev/peps/pep-0263/

'''
Copyright (C) 2013 A. Rimoldi <a.l.e@ideale.ch>
                   C. Gémy <cedric@cgemy.com>
                   C. Schockaert <R3vLibre@citadels.be>

##Tests for "TypographicGrid extension"

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

# Load class and functions to be tested
import imp
mod_typoGrid = imp.load_source("typographic_grid", "../typographic_grid.spy")


class Test_ScribusTypoGridUI(object):
    """Class to handle definition of UI parameters in tests without running a real UI"""

    def __init__(self, gridSpec):
        """Define grid specification as array describing 'page', 'margins', 'leading' and 'grid'"""
        self.gridSpec = gridSpec
        return

    def getParamValues(self):
        """Get values from test UI definition"""
        # Get page specification from Scribus Document

        return (self.gridSpec["page"], 
                self.gridSpec["margins"],
                self.gridSpec["leading"],
                self.gridSpec["grid"])


class Test_ScribusTypoGrid(mod_typoGrid.ScribusTypoGrid):
    """Class completed with test functionalities for validation of parent"""

    # Space width for each indentation level
    indentSize = 2

    # Param Description : tuple(CategoryName, CategoryPath, CategoryContent)
    #   - CategoryContent can itself be a full parameter description
    #   - CategoryContent as a constant string refers to a actual param value
    paramsList \
        = [("Page",
            "page", 
            ["width", "height"]),
           ("Margins",
            "margins",
            ["left", "right", "top", "bottom"]),
           ("Leading interval",
            "leading",
            ["target", "computed", "computed_lower", "computed_upper"]),
           ("Grid",
            "grid", 
            [("Limits", 
              "", 
              ["left", "right", "top", "bottom",
               "height", "width",
               "nb_baselines"]),
             ("Vertical", 
              "vertical", 
              ["nb_div", "gutter"]),
             ("Horizontal", 
              "horizontal", 
              ["nb_div", "gutter"]),
             ]
            )
           ]


    def __init__(self, ui):
        super(Test_ScribusTypoGrid, self).__init__(ui)
        return


    def describeParams(self, paramsList, categoryPathList = []):
        """Return a list of strings describing key/value pairs for parameters 
within a parameters list."""
        
        paramsDescription = []
        indentLevel = len(categoryPathList)
        indent = ' ' * indentLevel * Test_ScribusTypoGrid.indentSize
        for elem in paramsList:
            if isinstance(elem, basestring):
                # If elem is a string, we are ready for param evaluation
                categoryAccess = None
                for category in categoryPathList:
                    if categoryAccess == None:
                        categoryAccess = getattr(self, category)
                    elif category == "":
                        # Do nothing : categoryAccess is already well set 
                        # (condition is kept here for clarity)
                        pass
                    else:
                        categoryAccess = categoryAccess[category]

                Description = indent + elem + " = " \
                    + str(categoryAccess[elem])
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


    def describeGridSpec(self):
        """Generate a summary string of grid specifications"""
        gridSpecs = [ ]
        gridSpecs.extend(self.describeParams(Test_ScribusTypoGrid.paramsList))
                    
        # Remove the last blank record added after each top-level category
        gridSpecs.pop()
                                                         
        return "\n".join(gridSpecs)


    def createGrid(self):
        print "createGrid: test routine -- no creation performed !"
        return


def run_tests():
    ui_Test_001 = Test_ScribusTypoGridUI(
        # Define test values for Test_001 (units = cm)
        {
            # Page dimensions
            "page":
                {"width": 21.0, "height": 29.7},
             # Margin definitions
            "margins":
                {"left": 1.25, "right": 1.25, 
                 "top": 1.25, "bottom": 1.25},
            # Leading interval (cm)
            "leading":
                {"target": 0.77},
            # Grid specifications
            "grid":
                {"vertical": {"nb_div": 6,
                              "gutter": 0.8},
                 "horizontal": {"nb_div": 6,
                                "gutter": 0.8}}
            }
        )
    testGrid = mod_typoGrid.run(ui_Test_001)
    GridSpec = testGrid.describeGridSpec()
    print "Grid Specification:\n" + GridSpec


if __name__ == '__main__':
    run_tests()
