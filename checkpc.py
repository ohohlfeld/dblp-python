import datetime
import dblp
import operator
import pickle
from collections import defaultdict

verbose = True
#verbose = False

pc = {}
pc["2014"] = defaultdict(list)
pc["2015"] = defaultdict(list)
pc["2016"] = defaultdict(list)
pc["2017"] = defaultdict(list)
pc["2018"] = defaultdict(list)

## This is the part where we read the PC information from text files
## and populate the dictionary. pc[year][conf] is a list of PC members
## for that conference.

for x in open("sosp17-pc.txt", 'r'):
    xx = x.split(",")
    pc["2017"]["sosp"].append(xx[0])

for x in open("sosp15-pc.txt", 'r'):
    xx = x.split(",")
    pc["2015"]["sosp"].append(xx[0])
    
for x in open("eurosys17-pc.txt", "r"):
    xx = x.split(",")
    pc["2017"]["eurosys"].append(xx[0])

for x in open("fast18-pc.txt", "r"):
    xx = x.split(",")
    pc["2018"]["fast"].append(xx[0])

for x in open("osdi16-pc.txt", "r"):
    xx = x.split(",")
    pc["2016"]["osdi"].append(xx[0])

for x in open("nsdi15-pc.txt", "r"):
    xx = x.split(",")
    pc["2015"]["nsdi"].append(xx[0])

for x in open("nsdi16-pc.txt", "r"):
    xx = x.split(",")
    pc["2016"]["nsdi"].append(xx[0])

for x in open("nsdi17-pc.txt", "r"):
    xx = x.split(",")
    pc["2017"]["nsdi"].append(xx[0])

for x in open("atc17-pc.txt", "r"):
    xx = x.split(",")
    pc["2017"]["usenix"].append(xx[0])

for x in open("popl18-pc.txt", "r"):
    xx = x.split(",")
    pc["2018"]["popl"].append(xx[0])

# - for isca    
for x in open("isca17-pc.txt", "r"):
    xx = x.split("-")
    pc["2017"]["isca"].append(xx[0].strip())
    
# special for popl 17, just use names as is
for x in open("popl17-pc.txt", "r"):
    pc["2017"]["popl"].append(x.strip())

for x in open("pldi17-pc.txt", "r"):
    pc["2017"]["pldi"].append(x.strip())

for x in open("mobicom17-pc.txt", "r"):
    pc["2017"]["mobicom"].append(x.strip())

for x in open("mobicom16-pc.txt", "r"):
    pc["2016"]["mobicom"].append(x.strip())

for x in open("mobicom15-pc.txt", "r"):
    pc["2015"]["mobicom"].append(x.strip())

for x in open("mobicom14-pc.txt", "r"):
    pc["2014"]["mobicom"].append(x.strip())

for x in open("sigcomm17-pc.txt", "r"):
    pc["2017"]["sigcomm"].append(x.strip())

for x in open("sigcomm16-pc.txt", "r"):
    pc["2016"]["sigcomm"].append(x.strip())

for x in open("sigcomm14-pc.txt", "r"):
    pc["2014"]["sigcomm"].append(x.strip())
    
for x in open("sigcomm15-pc.txt", "r"):
    pc["2015"]["sigcomm"].append(x.strip())
    
for x in open("sigmod17-pc.txt", "r"):
    pc["2017"]["sigmod"].append(x.strip())

for x in open("vldb17-pc.txt", "r"):
    pc["2017"]["vldb"].append(x.strip())

for x in open("asplos17-pc.txt", "r"):
    xx = x.split(",")
    pc["2017"]["asplos"].append(xx[0])
    
# The main heart of the logic. 'conf', 'conf_short' both need to be
# the values that DBLP sees for this conference. See the many examples
# to identify the values for the conference you are interested in.
#
# pc[year][conf] needs to be setup before check_pc is invoked.

def check_pc(conf, year, conf_short):
    pc_papers = {}
    pc_papers_titles = set()
    total_count = 0
    pc_count = 0
    conf = conf.lower()
    a = dblp.getvenueauthorsbypaper("/conf/" + conf.lower() + "/" + str(year), conf_short)
    for x in a:
        #print x
        total_count += 1
        for xx in x[1]:
            # Need to put in more hacks like this unfortunately
            if xx == "Yuanyuan Zhou 0001":
                if "Yuanyuan Zhou" in pc[year][conf]:
                    pc_count += 1
                    break
            if xx in pc[year][conf]:
                pc_count += 1
                # Uncomment if you want to see which papers are PC-authored
                if verbose:
                    print pc_count, xx, ":", x[0][0]
                pc_papers[xx] = pc_papers.get(xx, 0) + 1
                pc_papers_titles.add(x[0][0])
                break

    print
    print conf, year
    print "Total Papers:", total_count
    print "PC-Paper Count:", pc_count
    print "Percentage of PC-authored papers: ", format((100.0 * pc_count/total_count if total_count != 0 else 0), '.2f')
    if verbose:
        print len(pc_papers_titles)
        for pp in sorted(pc_papers.items(), key=operator.itemgetter(1), reverse=True):
            print pp[0], pp[1]

# check_pc("sosp", "2017", "SOSP")
# check_pc("eurosys", "2017", "EuroSys")
# check_pc("fast", "2018", "FAST")
# check_pc("osdi", "2016", "OSDI")
# check_pc("usenix", "2017", "USENIX Annual Technical Conference")
# check_pc("nsdi", "2015", "NSDI")
# check_pc("nsdi", "2016", "NSDI")
# check_pc("nsdi", "2017", "NSDI")
# check_pc("popl", "2017", "POPL")
# check_pc("pldi", "2017", "PLDI")
# check_pc("sigmod", "2017", "SIGMOD Conference")
# check_pc("asplos", "2017", "ASPLOS")
# check_pc("isca", "2017", "ISCA")
# check_pc("sosp", "2015", "SOSP")
# check_pc("sigcomm", "2017", "SIGCOMM")
# check_pc("sigcomm", "2016", "SIGCOMM")
# check_pc("sigcomm", "2014", "SIGCOMM")
# check_pc("sigcomm", "2015", "SIGCOMM")
# check_pc("mobicom", "2017", "MobiCom")
# check_pc("mobicom", "2016", "MobiCom")
# check_pc("mobicom", "2015", "MobiCom")
# check_pc("mobicom", "2014", "MobiCom")
