import os
n = 5000
urllist = [
'http://localhost:8080/servletcoroutine-0.0.1-SNAPSHOT/sync.html',
'http://localhost:8080/servletcoroutine-0.0.1-SNAPSHOT/kilim.html'
]
timelist = [100, 200, 500, 1000, 2000, 3000]
for i in range(1, 11):
    for time in timelist:
        for url in urllist:
            cmd = 'ab -c %d -n %d %s?sleeptime=%d' % ((i * 100), n, url, time)
            print cmd
            os.system(cmd)
