#!/usr/bin/python
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
    sys.exit(main())
    try:
        sys.exit(main())
    except Exception, e:
        print "%s: %s" %(e.__class__.__name__, e)
        sys.exit(1)
if __name__ == "__main__":
    main()
    
