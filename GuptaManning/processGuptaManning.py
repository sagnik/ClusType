import re
from itertools import combinations

#if the match is (" example ",(5,14)), we return
#( "example",(6,13))  
def stripMatch(match):
    if match[0][0]==" " and match[0][-1] == " ":
        return (match[0].strip(),(match[1][0]-1,match[1][1]-1)) 
    elif match[0][0]==" " and match[0][-1] != " ":
        return (match[0].strip(),(match[1][0]-1,match[1][1]))
    elif match[0][0]!=" " and match[0][-1] == " ":
        return (match[0].strip(),(match[1][0],match[1][1]-1))
    else:
        return match  

def matchString(match):
    return "{0}|{1},{2}".format(match[0],match[1][0],match[1][1]) 
  
def getBetween(pattern,content,tags):
   matches= [(m.group(1),m.span(1)) for m in re.finditer(pattern,content,re.DOTALL)]
   return [matchString(stripMatch(match))+"|"+",".join(tags) for match in matches if "<tag name=" not in matchString(stripMatch(match))]
 
def processAbstract(abstract):
    tags=["DOMAIN","FOCUS","TECHNIQUE"]
    tagStart = "<tag name=\"{0}\" value=\"start\"/>"
    tagEnd = "<tag name=\"{0}\" value=\"end\"/>"
    results = []
    for (tag1,tag2,tag3) in list(combinations(tags,3)):
        pattern=tagStart.format(tag1)+tagStart.format(tag2)+tagStart.format(tag3)\
        +"(.*?)"+\
        tagEnd.format(tag3)+tagEnd.format(tag2)+tagEnd.format(tag1)
        results+=getBetween(pattern,abstract,[tag1,tag2,tag3]) 
    
    for (tag1,tag2) in list(combinations(tags,2)):
        pattern=tagStart.format(tag1)+tagStart.format(tag2)\
        +"(.*?)"+\
        tagEnd.format(tag2)+tagEnd.format(tag1)
        results+=getBetween(pattern,abstract,[tag1,tag2]) 
   
    for tag in tags:
        pattern=tagStart.format(tag)+"(.*?)"+tagEnd.format(tag)
        results+=getBetween(pattern,abstract,[tag])
    
    return results   
   
    
    

def main():
    cons=[(x.split("\n")[0],"\n".join(x.split("\n")[1:]).strip()) for x in open("../data/FTDDataset_v1.txt").read().split("\n##")[1:]]
    taggedCons=[(con[0],processAbstract(con[1]),con[1]) for con in cons]
    for (fname,taggedCon,content) in taggedCons:
        with open("../data/guptamanning/{0}.txt".format(fname),"w") as f,\
        open("../data/guptamanning/{0}.ann".format(fname),"w") as g:
            f.write(content)
            g.write("\n".join("T"+str(index+1)+"|"+con for (index,con) in enumerate(taggedCon)))
    #for r in rs: print r;   

if __name__ == "__main__":
    main()
