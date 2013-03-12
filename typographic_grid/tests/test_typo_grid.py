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

import imp
typo_grid = imp.load_source("typographic_grid", "../typographic_grid.spy")
print "Initialisation of module 'TypoGrid' =" + str(typo_grid)

if __name__ == '__main__':
    typo_grid.run(
        # Define test values (units = cm)
        testValues = {
            # Page dimensions
            "page":
                {"width": 21.0, "height": 29.7},
             # Margin definitions
            "margins":
                {"left": 1.25, "right": 1.25, 
                 "top": 1.25, "bottom": 1.25},
            # Leading interval (cm)
            "leading":
                {"initial": 0.77},
            # Grid specifications
            "grid":
                {"vertical": {"nb_div": 6,
                              "spacing": 0.8},
                 "horizontal": {"nb_div": 6,
                                "spacing": 0.8}}
        }
        )
