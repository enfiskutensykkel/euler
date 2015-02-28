#!/usr/bin/env python
#
# This script retrieves problem descriptions from the Project Euler website
# and stores them as README files with Markdown syntax.
#
# It assumes that directories containing source code files are problems
# attempted solved, and that the directory name is the problem number.
#
#  ./path/to/problem/18/whatever.cpp
#
# The above will translate as a solution for problem 18, and a README.med file
# will be placed in ./path/to/problem/18/
#
# The file INDEX.md is auto-generated with a list of all solved and attempted
# problems.
#
import os
from urllib import urlencode
import urllib2 as url
import cookielib as cookie
import re
import sys
import getopt
from datetime import datetime as dt

known_extensions = ['.py', '.c', '.cc', '.cpp', '.java', '.php', '.pl', '.js', '.sh']


def walk(abspath, relpath, directory, force):
    solutions = []

    has_readme = False
    has_source = False

    for filename in os.listdir(abspath):
        path = os.path.join(abspath, filename)

        if os.path.isdir(path):
            solutions += walk(path, os.path.join(relpath, filename), filename, force)
        elif os.path.splitext(filename)[1] in known_extensions:
            has_source = True
        elif filename == "README.md":
            has_readme = True

    if has_source and (force or not has_readme):
        solutions.append((relpath, directory))

    return solutions


def create_connection(password):
    jar = cookie.CookieJar()
    opener = url.build_opener(url.HTTPRedirectHandler(), url.HTTPHandler(), url.HTTPSHandler(), url.HTTPCookieProcessor(jar))

    params = urlencode({'username': "enfiskutensykkel", 'password': password, 'sign_in': "Sign In"})
    headers = {'User-Agent': "Browser", 'Content-Type': "application/x-www-form-urlencoded", 'Host': "projecteuler.net"}
    request = url.Request("https://projecteuler.net/sign_in", params, headers)
    data = opener.open(request).read()

    if "sign_in" in re.findall(r'<a href="([^"]*)"', data):
        return None

    return opener


def retrieve_problem(connection, problem):
    # FIXME: Use something more efficient than re.findall
    data = connection.open("https://projecteuler.net/problem=%s" % str(problem)).read()
    title = re.findall(r'<h2>(.*?)</h2>', data)[0].strip()
    raw_content = re.findall(r'<div\s+class="problem_content"[^>]*>(.*)</div>(<br />\s*)+(<br />|<div style="([^"]*)" class="noprint">)', data, re.DOTALL | re.MULTILINE)[0]
    content = raw_content[0].replace("\r", "")
    solved = len(re.findall(r'<input', data)) == 0
    return title, content, solved


def create_readme(path, problem, title, content, solved):
    link = "\n\n[Go to the problem description](https://projecteuler.net/problem=%s)\n" % str(problem)

    with open(os.path.join(path, "README.md"), "w") as f:
        headline = "=" * (len(title))
        f.write(title)
        if not solved:
            f.write(" (not solved yet)")
            headline += "=" * len(" (not solved yet)")
        f.write("\n")
        f.write(headline)
        f.write("\n")

        f.write(content)
        f.write(link)


def build_index(path, index):
    filename = os.path.join(path, "INDEX.md")
    solved = ((path, number, title) for path, number, title, content, solved in index if solved is True)
    unsolved = ((path, number, title) for path, number, title, content, solved in index if solved is False)

    with open(filename, "w") as f:
        f.write("Solutions\n")
        f.write("=========\n")
        f.write("Here is a list of [Project Euler](https://projecteuler.net/) problems I've attempted to solve.\n")
        f.write("This file was generated on %s by the `update.py` script.\n\n" % str(dt.utcnow()))

        f.write("Solved\n")
        f.write("------\n")
        count = 0
        for path, number, title in solved:
            f.write("* [PE%s %s](https://github.com/enfiskutensykkel/euler/tree/master/%s)\n" % (number, title, path))
            count += 1
        f.write("\n")

        if count < len(index):
            f.write("Work in progress\n")
            f.write("----------------\n")
            for path, number, title in unsolved:
                f.write("* [PE%s %s](https://github.com/enfiskutensykkel/euler/tree/master/%s)\n" % (number, title, path))
            f.write("\n")


def usage(command, handle):
    handle.write("Usage: %s -p <password> [-v] [-f] [-h]\n\n" % command)
    handle.write("  -p\tpassword for user enfiskutensykkel at Project Euler\n")
    handle.write("  -f\trebuild index file and update all project descriptions\n")
    handle.write("  -v\tbe verbose, print out problem names\n")
    handle.write("  -h\tshow this help\n")
    handle.write("\nThis scripts searches subdirectories for source code files.\n")
    handle.write("Parent directory MUST be named using the Project Euler problem number.\n")


if __name__ == '__main__':
    force = False
    quiet = True
    password = None

    optlist, args = getopt.gnu_getopt(sys.argv, "fp:hv")
    for opt, arg in optlist:
        if opt == '-h':
            usage(sys.argv[0], sys.stdout)
            sys.exit(0)
        elif opt == '-v':
            quiet = False
        elif opt == '-f':
            force = True
        elif opt == '-p':
            password = arg

    if password == None:
        sys.stderr.write("Missing password\n")
        usage(sys.argv[0], sys.stderr)
        sys.exit(1)

    status = sys.stdout if quiet else sys.stderr

    status.write("Locating source code files... ")
    status.flush()
    solutions = walk(os.getcwd(), "", os.path.basename(os.getcwd()), force)
    solutions = filter(lambda item: re.match(r'\d+', item[1]), solutions)
    solutions.sort(cmp=lambda a, b: -1 if int(a[1]) < int(b[1]) else 1)
    status.write(" DONE\n")

    if len(solutions) == 0:
        sys.stderr.write("No new solutions found\n")
        sys.stderr.write("Use -f to update already downloaded descriptions\n")
        sys.exit(0)

    status.write("Connecting to PE website... ")
    status.flush()
    conn = create_connection(password)
    if conn is None:
        status.write("FAIL\n")
        sys.stderr.write("Failed to sign in\n")
        sys.exit(2)
    status.write("DONE\n")

    index = []

    status.write("Downloading problem descriptions... ")
    if not quiet:
        status.write("\n")
    status.flush()
    for path, number in solutions:
        title, content, solved = retrieve_problem(conn, number)
        if not quiet:
            sys.stdout.write("%4s %s %s\n" % (number, title, "[solved]" if solved else "[unsolved]"))
        index.append((path, number, title, content, solved))
    if quiet:
        status.write("DONE\n")

    status.write("Writing description files... ")
    status.flush()
    for path, number, title, content, solved in index:
        create_readme(os.path.join(os.getcwd(), path), number, title, content, solved)
    status.write("DONE\n")

    if force:
        status.write("Updating index... ")
        build_index(os.getcwd(), index)
        status.write("DONE\n")
