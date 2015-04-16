from optparse import OptionParser
import urllib2
import urllib
from time import sleep

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
baseUrl = "http://www.google.com/search?q="
headers={'User-Agent':user_agent,}

# just store whole html for now
def extract(content):
    return content.encode('string_escape') + '\n'

def scrape(queries):
    print "scraping " + str(len(queries)) + " queries, please wait..."
    with open(options.outputFile, 'a') as output:
        for query in queries:
            # sleep(1)
            url = baseUrl + urllib.quote(query)
            request = urllib2.Request(url, None, headers)
            connection = urllib2.urlopen(request)
            output.write(query + '\n' + extract(connection.read()))

if __name__ == '__main__':
    parser = OptionParser("")
    parser.add_option("--input", "-i", dest="inputFile", action="store", default="queries.txt")
    parser.add_option("--output", "-o", dest="outputFile", action="store", default="pages.txt")

    (options, args) = parser.parse_args()
    queries = []
    with open(options.inputFile, 'r') as qf:
        for line in qf:
            queries.append(line.strip().split('\t')[1])
    scrape(queries)