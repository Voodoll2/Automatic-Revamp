from urllib2 import urlopen, URLError, HTTPError
import re
import os
from os.path import join

pathToInputs = '/Users/voodoll2/Desktop/Automatic/Models'

def dlfile(url, saveFileName):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(join(pathToInputs, saveFileName), "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url

def download():
    urls = []
    urls.append("https://neuinfo.org/mynif/search.php?q=*&t=indexable&cf=Models&nif=nlx_154697-12&ff=Database:ModelDB&s=Output%20files&sa=true&b=%0")
    for url in urls:
        print url
        nifpage = urlopen(url)
        nifPattern = "http:\S+model=\d+"
        # print pattern

        nifString = nifpage.read()
        modeldbLinks = re.findall(nifPattern, nifString)
        count = 1
        for link in modeldbLinks:
            # if count > 9:
            #     break
            print "model db link: ", link
            modeldbPattern = "o=\d+\S+zip"
            modeldbPage = urlopen(link)
            modeldbString = modeldbPage.read()
            downloadMatch = re.search(modeldbPattern, modeldbString)
            accessPattern = "o=\d+\&"
            accessNumber = re.search(accessPattern, str(downloadMatch.group()))
            accessNumber = str(accessNumber.group())[2:-1]
            downloadLink = 'http://senselab.med.yale.edu/modeldb/eavBinDown.asp?' + downloadMatch.group()
            if not accessNumber == '144570':
                dlfile(downloadLink, accessNumber)
            count += 1
