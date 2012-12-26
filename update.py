#!/usr/bin/env python

# This script retrieves problem descriptions from the project Euler website
# and stores them as README files with Markdown syntex.
#
# It assumes that solved problems are organized in directories corresponding
# to their ID number. For example, the solution to problem 18 should be stored
# as:
#    ./1-25/18/whatever
#
# This script will then recognize 18 and download the problem description and
# put it in ./1-25/18

### parameters ###
root = "."
name = "README.md"
### end parameters ###


import urllib2 as url, os, re

handle = open(os.path.join(root, name), "a")
override = False

for subdir in map(lambda name: os.path.join(root, name), filter(lambda name: re.match(r'[0-9]+\-[0-9]+', name) != None, [ name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name)) ])):
	for directory, problem in [ (os.path.join(subdir, d), d) for d in os.listdir(subdir) if os.path.isdir(os.path.join(subdir, d)) and d.isdigit() ]:

		# Don't overwrite existing file
		if not override and os.path.isfile(os.path.join(directory, name)):
			continue


		# Retrieve problem description
		print "#%s downloading..." % problem
		result = url.urlopen("http://projecteuler.net/problem=%s" % problem).read()


		# Process data
		title = re.findall(r'<h2>(.*?)</h2>', result)[0].replace("\r", "")
		contents = re.findall(r'<div\s+class="problem_content".*?>(.*)</div><br />\s*<br /></div>', result, re.DOTALL | re.MULTILINE)[0].replace("\r", "")
		#contents = url.urlopen("http://projecteuler.net/minimal=%s" % d).read().replace("\r","")
		if not title[-1] == "\n":
			title += "\n"
		line = "".join(['='] * (len(title)-1)) + '\n'
		link = "\n\n[Go to the problem description](http://projecteuler.net/problem=%s)\n" % problem


		# Write to file
		print "#%s writing..." % problem
		open(os.path.join(directory, name), 'w').write(title + line + contents + link)

		handle.write("[#%s %s](%s)\n" % (problem, title.strip(), directory))

handle.close()
