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

import datetime
import os
import settings
import sys

class IncrLauncher:
	def __init__( self ):
		self.dumpdate = self.getDumpDate()
		self.scriptdir = settings.scriptdir
		self.wikilist = ''

	def getDumpDate( self ):
		today = datetime.datetime.now()
		today -= datetime.timedelta( days=2 )
		return today.strftime( "%Y%m%d" )

	def processArgs( self ):
		if ( sys.argv[1] == 'one' ):
			self.wikilist = '%s/%s-wikis.txt.1' % ( self.scriptdir, self.dumpdate )
		elif ( sys.argv[1] == 'two' ):
			self.wikilist = '%s/%s-wikis.txt.2' % ( self.scriptdir, self.dumpdate )
		self.dispatch()

	def dispatch( self ):
		os.system( 'python %s/runner.py list %s %s' % ( self.scriptdir, self.wikilist, self.dumpdate ) )

if __name__ == "__main__":
	IncrLauncher = IncrLauncher()
	IncrLauncher.processArgs()
