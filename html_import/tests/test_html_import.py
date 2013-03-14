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
mod_htmlImport = imp.load_source("html_import",
                                 "../html_import.spy")
mod_htmlImportRead = imp.load_source("html_import",
                                     "../html_import_read.py")
mod_htmlImportWrite = imp.load_source("html_import",
                                      "../html_import_write.py")

class Test_ScribusHTMLImportWrite(mod_htmlImportWrite.ScribusHTMLImportWrite):

    def __init__(self, HTMLImportRead_ParsedTree):
        super(Test_ScribusHTMLImportWrite, self)\
            .__init__(HTMLImportRead_ParsedTree)
        return


def run_tests():
    mod_htmlImport.run()

if __name__ == '__main__':
    run_tests()

