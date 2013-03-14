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

class ScribusHTMLImportRead(object):

    def __init__(self):
        print "Setting ScribusTypoGrid"
        self.ui = ui
        (page, margins, leading, grid) = ui.getParamValues()
        self.setValues(page, margins, leading, grid)


    def setValues(self, page, margins, leading, grid):
        """Set values from arrays 'page', 'margins', 'leading' and 'grid'"""
        self.page = page
        self.margins = margins
        self.leading = leading
        self.grid = grid


    def calculateGrid(self):
        self.grid["left"] = self.margins["left"]
        self.grid["right"] = self.page["width"] - self.margins["right"]
        self.grid["top"] = self.margins["top"]
        self.grid["bottom"] = self.page["height"] - self.margins["bottom"]

        # Compute grid height & width
        self.grid["height"] = abs(self.grid["bottom"] - self.grid["top"])
        self.grid["width"] = abs(self.grid["right"] - self.grid["left"])

        # Compute nb of lines based on initial interval
        self.computeBaselineNbAndInterval()


    def computeBaselineNbAndInterval(self):
        """Compute nb of lines based on initial interval."""
        self.grid["nb_baselines"] \
            = int(self.grid["height"] / self.leading["target"])

        # Then compute resulting leading space resulting in integer nb_baselines
        self.leading["computed_lower"] \
            = self.grid["height"] / (self.grid["nb_baselines"] + 1)

        self.leading["computed_upper"] \
            = self.grid["height"] / self.grid["nb_baselines"]

        # Keep closest resulting computed leading interval
        if (abs(self.leading["computed_upper"] - self.leading["target"])
            < abs(self.leading["computed_lower"] - self.leading["target"])):
            self.leading["computed"] = self.leading["computed_upper"]
        else:
            self.leading["computed"] = self.leading["computed_lower"]
        

    def createGrid(self):
        print "createGrid: not implemented yet !"
        return


