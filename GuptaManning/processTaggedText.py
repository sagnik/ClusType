import sys
import re
import os

def removeTags(taggedAbstract):
    pattern="<(.*?)/>"
    matches=[m.span(0) for m in re.finditer(pattern,taggedAbstract,re.DOTALL)]
    abstract=""
    startIndex=0
    for match in matches:
        con=taggedAbstract[startIndex:match[0]]
        if not con.startswith(" "):
            con=" "+con
        abstract+=con
        startIndex=match[1]
    abstract+=taggedAbstract[startIndex:]
    return " ".join([x for x in re.split("\\s+",abstract) if x])
    
def main():
    fName=sys.argv[1]
    toWrite=os.path.join(os.path.split(fName)[0][:-14],"abstxts",os.path.split(fName)[1])
    print toWrite
    with open(toWrite,"w") as f:
        f.write(removeTags(open(sys.argv[1]).read()))

if __name__ == "__main__":
   main()
