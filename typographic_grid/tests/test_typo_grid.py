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
    def __init__(self, ui):
        super(Test_ScribusTypoGrid, self).__init__(ui)
        return


    def describeGridSpec(self):
        """Generate a summary string of grid specifications"""
        gridSpecs = [ ]
        gridSpecs.append("Page:")
        gridSpecs.append("  width = " + str(self.page["width"]))
        gridSpecs.append("  height = " + str(self.page["height"]))
        gridSpecs.append("")
        gridSpecs.append("Margins:")
        gridSpecs.append("  left = " + str(self.margins["left"]))
        gridSpecs.append("  right = " + str(self.margins["right"]))
        gridSpecs.append("  top = " + str(self.margins["top"]))
        gridSpecs.append("  bottom = " + str(self.margins["bottom"]))
        gridSpecs.append("")
        gridSpecs.append("Leading interval:")
        gridSpecs.append("  target = " + str(self.leading["target"]))
        gridSpecs.append("  computed = " + str(self.leading["computed"]))
        gridSpecs.append("  computed_lower = " + str(self.leading["computed_lower"]))
        gridSpecs.append("  computed_upper = " + str(self.leading["computed_upper"]))
        gridSpecs.append("")
        gridSpecs.append("Grid:")
        gridSpecs.append("  Limits:")
        gridSpecs.append("    left = " + str(self.grid["left"]))
        gridSpecs.append("    right = " + str(self.grid["right"]))
        gridSpecs.append("    top = " + str(self.grid["top"]))
        gridSpecs.append("    bottom = " + str(self.grid["bottom"]))
        gridSpecs.append("    height = " + str(self.grid["height"]))
        gridSpecs.append("    width = " + str(self.grid["width"]))
        gridSpecs.append("    baseline_nb = " + str(self.grid["nb_baselines"]))
        gridSpecs.append("  Vertical:")
        gridSpecs.append("    nb_div = " + str(self.grid["vertical"]["nb_div"]))
        gridSpecs.append("    gutter = " + str(self.grid["vertical"]["gutter"]))
        gridSpecs.append("  Horizontal:")
        gridSpecs.append("    nb_div = " + str(self.grid["horizontal"]["nb_div"]))
        gridSpecs.append("    gutter = " + str(self.grid["horizontal"]["gutter"]))
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
