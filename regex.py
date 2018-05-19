import re

#create a regex from a raw string
d3 = re.compile(r"[0-9]{3,4}")

m = re.search(d3,"abc123xyz45")

print("{0} {1}".format(type(m), m))

#condition on match found
if re.search(d3,"123"):
    print ("Matched")
else:
    print ("No matchee")

#substitution and groups
groups = re.compile(r"(\d\d)-(\d\d)-(\d{4})")
us_dates = "01-03-2017 12-30-2016 03-31-2017"
# reference groups by number - groups defned by () in the regex
uk_dates = re.sub(groups, r"\2-\1-\3", us_dates)
print("US {0} converted to UK {1}".format(us_dates, uk_dates))

#limit to 2 substitutons
uk_dates = re.sub(groups, r"\2-\1-\3", us_dates, 2)
print("US {0} converted to UK {1}".format(us_dates, uk_dates))

#findall matches in a string
print (re.findall(groups, us_dates))

#multiline string - ready for a url match and sub
urls = \
'''http://foo.bar.com/test/test.html
http://grew.bar.com/myapp/
https://barneymcgrew.bar.com/index.asp'''

changeurl = re.compile(r"(https?)://(\w+)\.bar\.com/(\S+)")
#g1=http(s) g2=domain prefix g3=folders/file
newurls = re.sub(changeurl, r"\1://\2.foobar.com/\3", urls)
print (newurls)


