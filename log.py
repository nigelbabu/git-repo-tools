#!/usr/bin/python
#
#    Git graph prepares commit graphs of git repositories
#
#    Copyright (C) 2010  Nigel Babu
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import csv
import re
import subprocess
import sys

def getlog(path):
    log = "git log --shortstat -C --date=short"
    p = subprocess.Popen(log, shell=True, cwd=path, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    return output
    
def splitinto(log):
    expression = re.compile('^commit (.*)\sAuthor: (.*)\sDate:   (.*)\s*.*\s*(.*) files changed, (.*) insertions\(\+\), (.*) deletions', re.M)
    result = re.findall(expression, log)
    return result

def export(stats):
    statswriter = csv.writer(open('stats.csv', 'wb'))
    for row in stats:
        statswriter.writerow(row)

def main():
    log = getlog('/path/to/repo')
    stats = splitinto(log)
    export(stats)
    
if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception, e:
        print "%s: %s" %(e.__class__.__name__, e)
        sys.exit(1)    
