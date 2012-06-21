#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Hydriz
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import datetime
import time

# Configuration goes here
path = "" # No trailing slash

# Nothing to change below...
date = ""

def getdate():
        global date
        now = datetime.datetime.now()
        now -= datetime.timedelta(days=1)
        date = now.strftime("%Y%m%d")

def checkifdone():
        global date
        os.chdir(path + "/")
        if (os.path.exists(date + '-done.txt')):
                time.sleep(1800) # Check every half-hour
                process()
        else:
                execmd()
                os.system('touch ' + date + '-done.txt')
                purge()
                process()

def purge():
        os.chdir(path + "/")
        now = datetime.datetime.now()
        now -= datetime.timedelta(days=7)
        olddate = now.strftime("%Y%m%d")
        oldfile = olddate + '-done.txt'
        if (os.path.exists(oldfile)):
                os.system("rm " + oldfile)
        else:
                print ""

def execmd():
        global path
        os.system('python ' + path + '/incrdumps.py ' + date)

def process():
        getdate()
        checkifdone()

process()
