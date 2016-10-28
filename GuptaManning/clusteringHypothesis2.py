import json
import random
import numpy as np

def getRPtoRight(base,sens):
    rpsToRight=[]
    for sen in sens:
        phrases=sen.split(",")
        if phrases.count(base+":EP")!=1:
            print "improbable results: EP: {0} :in sentence: {1} :".format(base+":EP",sen)
        else:
            index=phrases.index(base+":EP")
            if index==len(phrases)-1:
                print "EP: {0} : at the end of the sentence: {1} :".format(base+":EP",sen)
            else:    
                for phrase in phrases[index+1:]:
                    if ":RP" in phrase:
                        rpsToRight.append(phrase.split(":R")[0])
                        break
    if rpsToRight: 
        return rpsToRight
    else:
        return None    

def getRPtoLeft(base,sens):
    rpsToLeft=[]
    for sen in sens:
        phrases=sen.split(",")
        if phrases.count(base+":EP")!=1:
            print "improbable results: EP: {0} :in sentence: {1} :".format(base+":EP",sen)
        else:
            index=phrases.index(base+":EP")
            if index==0:
                print "EP: {0} : at the beginning of the sentence: {1} :".format(base+":EP",sen)
            else:    
                for i in range(index-1,0,-1):
                    if ":RP" in phrases[i]:
                        rpsToLeft.append(phrases[i].split(":R")[0])
                        break
    if rpsToLeft: 
        return rpsToLeft
    else:
        return None    
               
def getRPtoJustRight(base,sens):
    rpsToRight=[]
    for sen in sens:
        phrases=sen.split(",")
        if phrases.count(base+":EP")!=1:
            print "improbable results: EP: {0} :in sentence: {1} :".format(base+":EP",sen)
        else:
            index=phrases.index(base+":EP")
            if index==len(phrases)-1:
                print "EP: {0} : at the end of the sentence: {1} :".format(base+":EP",sen)
            else:    
                if ":RP" in phrases[index+1]:
                    rpsToRight.append(phrases[index+1].split(":R")[0])
                        
    if rpsToRight: 
        return rpsToRight
    else:
        return None    

def getRPtoJustLeft(base,sens):
    rpsToLeft=[]
    for sen in sens:
        phrases=sen.split(",")
        if phrases.count(base+":EP")!=1:
            print "improbable results: EP: {0} :in sentence: {1} :".format(base+":EP",sen)
        else:
            index=phrases.index(base+":EP")
            if index==0:
                print "EP: {0} : at the beginning of the sentence: {1} :".format(base+":EP",sen)
            else:    
                if ":RP" in phrases[index-1]:
                     rpsToLeft.append(phrases[index-1].split(":R")[0])
                        
    if rpsToLeft: 
        return rpsToLeft
    else:
        return None    

def listToFreqDict(l):
    dict={}
    for item in l:
        if item in dict:
            dict[item]=dict[item]+1
        else:
            dict[item]=1
    return [(k,dict[k]) for k in dict.keys()]

dinEPsDict=json.load(open("/home/sagnik/codes/ClusType/result/sample-domain-eps.json"))
tinEPsDict=json.load(open("/home/sagnik/codes/ClusType/result/sample-technique-eps.json"))

random.shuffle(dinEPsDict)
random.shuffle(tinEPsDict)


a=[y for y in [getRPtoJustRight(x['ep'],x["sentence"]) for x in dinEPsDict[:80]] if y is not None]
b=[y for y in [getRPtoJustRight(x['ep'],x["sentence"]) for x in tinEPsDict[:80]] if y is not None]

domainRPstoRight=listToFreqDict([x for y in a for x in y])
techniqueRPstoRight=listToFreqDict([x for y in b for x in y])
         
a=[y for y in [getRPtoJustLeft(x['ep'],x["sentence"]) for x in dinEPsDict[:80]] if y is not None]
b=[y for y in [getRPtoJustLeft(x['ep'],x["sentence"]) for x in tinEPsDict[:80]] if y is not None]

domainRPstoLeft=listToFreqDict([x for y in a for x in y])
techniqueRPstoLeft=listToFreqDict([x for y in b for x in y])

domainRPstoLeft.sort(key = lambda x:-x[1])
domainRPstoRight.sort(key = lambda x:-x[1])
techniqueRPstoLeft.sort(key = lambda x:-x[1])
techniqueRPstoRight.sort(key = lambda x:-x[1])

domainRPsentences=np.sum([len(x["sentence"]) for x in dinEPsDict[:80]])
techniqueRPsentences=np.sum([len(x["sentence"]) for x in tinEPsDict[:80]])

print "\n------------------------------------------\n"
print domainRPsentences,techniqueRPsentences

print "\n-------Domain EPs: Left----------------\n"
print domainRPstoLeft[:20]

print "\n-------Technique EPs: Left----------------\n"
print techniqueRPstoLeft[:20]

print "\n-------Domain EPs: Right----------------\n"
print domainRPstoRight[:20]

print "\n-------Technique RPs: Right----------------\n"
print techniqueRPstoRight[:20]

