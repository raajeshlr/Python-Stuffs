import re

#line = "abbbbb are smarter are than dog animals"
line = " are smarter are than dog?? animals dog"


matchingobject  = re.match(r'(\d) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(\D) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(123) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(ab) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(.?) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(\d) are (.*?) (.*)',line)
#matchingobject  = re.match(r'([ab]) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(ab*) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(a{5}) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'(a{3,5}) are (.*?) .*',line,re.M|re.I)
#matchingobject  = re.match(r'dog(!+|\?)',line,re.M|re.I)
matchingobject  = re.match(r'dog$',line,re.M|re.I)



if matchingobject:
    print("mathchign object is ",matchingobject.group())
    #print("mathchign object is ", matchingobject.group(1))
    #print("mathchign object is ", matchingobject.group(2))
    #print("mathchign object is ", matchingobject.group(3))
else:
    print("no match")
