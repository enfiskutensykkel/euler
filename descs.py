#!/usr/bin/env python

# This script retrieves all the problem descriptions, and formats them to
# mark down. Run this in the root directory.

import urllib2 as url, os, re

dirs = [ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) and name.isdigit() ]

override = False
for d in dirs:
	if not override and os.path.isfile(os.path.join(os.path.join(".",d), 'README.md')):
		continue

	print "Retrieving problem description #%s" % d

	r = url.urlopen("http://projecteuler.net/problem=%s" % d).read()
	title = re.findall(r'<h2>(.*?)</h2>', r)[0].replace("\r", "")
	content = re.findall(r'<div\s+class="problem_content".*?>(.*)</div><br />\s*<br /></div>', r, re.DOTALL | re.MULTILINE)[0].replace("\r", "")
	#content = url.urlopen("http://projecteuler.net/minimal=%s" % d).read().replace("\r","")

	if not title[-1] == "\n":
		title += "\n"
	line = "".join(['='] * (len(title)-1)) + '\n'

	link = "\n\n[Go to the problem description](http://projecteuler.net/problem=%s)\n" % d

	print "Writing description #%s to file" % d
	open(os.path.join(os.path.join(".",d), 'README.md'), 'w').write(title + line + content + link)
