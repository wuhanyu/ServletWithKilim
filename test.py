import os
import re

dict = {}
def setValue(name, concurrentnum, sleeptime, qps, rt):
    if (not dict.has_key(name)): dict[name] = {}
    dict[name]["%d:%d:qps" % (concurrentnum, sleeptime)] = qps
    dict[name]["%d:%d:rt" % (concurrentnum, sleeptime)] = rt

#init
n = 5000
urllist = [
'http://localhost:8080/servletcoroutine-0.0.1-SNAPSHOT/sync.html',
'http://localhost:8080/servletcoroutine-0.0.1-SNAPSHOT/kilim.html'
]
timelist = [100, 200, 500, 1000, 2000, 3000]
pattern_name = re.compile(r'(\w*).html')
pattern_qps = re.compile(r'(\d+.\d+) \[#/sec\]')
pattern_rt = re.compile(r'(\d+.\d+) \[ms\]')

file_object = open('log.txt', 'w')

#begin

for i in range(1, 11):
    for time in timelist:
        for url in urllist:
            concurrent = i * 100
            cmd = 'ab -c %d -n %d %s?sleeptime=%d' % (concurrent, n, url, time)
            print cmd
            tmp = "".join(os.popen(cmd).readlines())
            if (len(tmp) < 100): continue
            print tmp
            file_object.write(tmp)
            name = pattern_name.search(tmp).group(1)
            qps = pattern_qps.search(tmp).group(1)
            rt = pattern_rt.search(tmp).group(1)
            print qps, rt
            setValue(name, concurrent, time, qps, rt)
file_object.close()
            
for key in dict:
    print "============%s============" % key
    print "------------qps------------"
    for i in range(1, 11):
        str = ""
        for time in timelist:
            concurrent = i * 100
            str += "%s\t" % dict[key]["%d:%d:qps" % (concurrent, time)]
        print str
    print "------------rt------------"
    for i in range(1, 11):
        str = ""
        for time in timelist:
            concurrent = i * 100
            str += "%s\t" % dict[key]["%d:%d:rt" % (concurrent, time)]
        print str