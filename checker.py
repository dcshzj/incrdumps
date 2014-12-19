#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012-2014 Hydriz Scholz
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime, timedelta
import os
import settings
import sys
import time

class IncrChecker:
	def __init__( self ):
		workingdate = datetime.today() - timedelta(3)
		deletedate = datetime.today() - timedelta(5)
		self.date = workingdate.strftime( '%Y%m%d' )
		self.deletedate = deletedate.strftime( '%Y%m%d' )
		self.filetouse = "status.txt"
		self.scriptdir = settings.scriptdir

	def dldtestfile( self, wiki ):
		os.system( "wget -cq http://archive.org/download/incr-%s-%s/%s" % ( wiki, self.date, self.filetouse ) )

	def reupload( self, wiki ):
		os.system( "python %s/runner.py %s %s" % ( self.scriptdir, wiki, self.date ) )

	def test( self, wiki ):
		self.dldtestfile( wiki )
		if ( os.path.exists( self.filetouse ) ):
			os.system( "rm %s" % ( self.filetouse ) )
		else:
			self.reupload( wiki )

	def main( self ):
		wikilist = "%s-wikis.txt.1" % ( self.date )
		wikis = open( wikilist, 'r' ).read().splitlines()
		for wiki in wikis:
			time.sleep( 1 ) # Ctrl+C
			print "Checking %s..." % ( wiki )
			self.test( wiki )

		wikilist2 = "%s-wikis.txt.2" % ( self.date )
		wikis2 = open( wikilist2, 'r' ).read().splitlines()
		for wiki2 in wikis2:
			print "Checking %s..." % ( wiki2 )
			self.test( wiki2 )

		os.remove( "%s-wikis.txt.1" % ( self.deletedate ) )
		os.remove( "%s-wikis.txt.2" % ( self.deletedate ) )

if __name__ == "__main__":
	IncrChecker = IncrChecker()
	IncrChecker.main()
