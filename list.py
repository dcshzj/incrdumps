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
import re
import settings
import urllib

class IncrList:
	def __init__( self ):
		self.hosturl = settings.hosturl
		self.today = datetime.datetime.now().strftime( "%Y%m%d" )
		self.wikilist = []

	def grablistofwikis( self ):
		directory = urllib.urlopen( settings.hosturl )
		raw = directory.read()
		directory.close()
		wikis = re.compile( r'<strong>(?P<wiki>[^>]+)</strong>' ).finditer( raw )
		for wiki in wikis:
			self.wikilist.append( [ wiki.group( 'wiki' ) ] )
		count = 1
		for wiki in self.wikilist:
			thewiki = ''.join( wiki )
			if ( thewiki == "Here's the big fat disclaimer."):
				# The only non-wiki string that is in bold
				continue
			else:
				if ( count < 366 ):
					os.system( "echo %s >> %s/%s-wikis.txt.1" % ( thewiki, self.today ) )
					count += 1
				else:
					os.system( "echo %s >> %s/%s-wikis.txt.2" % ( thewiki, self.today ) )

if __name__ == "__main__":
	IncrList = IncrList()
	IncrList.grablistofwikis()
