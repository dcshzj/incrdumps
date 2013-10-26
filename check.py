#!/usr/bin/python
from datetime import datetime, timedelta
import os
import sys

class IncrChecker:
	def __init__(self):
		workingdate = datetime.today() - timedelta(2)
		self.date = workingdate.strftime('%Y%m%d')
		self.filetouse = "status.txt"

	def dldtestfile(self, wiki):
		os.system("wget -cq http://archive.org/download/incr-%s-%s/%s" % (wiki, self.date, self.filetouse))

	def reupload(self, wiki):
		os.system("python incrdumps.py %s %s" % (self.date, wiki))

	def test(self, wiki):
		self.dldtestfile(wiki)
		if (os.path.exists(self.filetouse)):
			os.system("rm %s" % (self.filetouse))
		else:
			self.reupload(wiki)

	def main(self):
		wikilist = "%s-wikis.txt" % (self.date)
		wikis = open(wikilist, 'r').read().splitlines()
		for wiki in wikis:
			print "Checking %s..." % (wiki)
			self.test(wiki)

def main():
	x = IncrChecker()
	x.main()
	print "Done!"

if __name__ == "__main__":
	main()
