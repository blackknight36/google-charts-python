#!/usr/bin/env python

def average(list):
   total = 0; count = 0
   for each in list:
      count += 1
      total += float(each)
   return total/count

def simpleEncode(values, maxValue):
   simpleEncoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
   chartdata = "s:"
   for x in values:
      currentValue = x
      if isinstance(currentValue, (int, long, float, complex)):
         idx = (61 * currentValue / maxValue)
         chartdata = chartdata + simpleEncoding[idx]
      else:
         chartdata = chartdata + "_"
   return chartdata

def mklabels(data, mod):
   xlabels = []
   n = 0
   for x in data:
      if n % 12 == 0:
         xlabels.append(x[0])
      n = n +1
   return xlabels

def cleandata(data):
   dpoints = []
   for x in data:
      p = int( round(x[1]) )
      dpoints.append(p)
   dpoints.remove(max(dpoints))
   return dpoints

def buildUrl(data, xlabels, ymax, avg, size):
   xstr = ""
   dstring = simpleEncode(data, ymax)
   for label in xlabels:
      xstr = xstr + "%s|" %label
   url = "//charts.googleapis.com/chart?chs=%s" %size
   url += "&cht=lc&chxt=x,y&chxl=0:|%s" %xstr
   url += "1:||%s|%s" %(int(avg), ymax)
   url += "&chd=%s" %dstring
   return url

def mkgraph(title, data, mod, size):
   ydata = cleandata(data)
   ymax = max(ydata)
   xlabels = mklabels(data, mod)
   avg = average(ydata)
   graphurl = buildUrl(ydata, xlabels, ymax, avg, size)
   print "<p>%s</p>\n" %title
   print "<img src='%s' alt='%s'>" %(graphurl, title)
   print "<br><br>\n"
