#!/bin/sh
DataPath='/media/sagnik/OS_Install/data/nlp-table-data/txtsfromparsredxmls/'
RawTextFiles='/media/sagnik/OS_Install/data/nlp-table-data/txtsfromparsedxmls/'
#TypeFile='/media/sagnik/OS_Install/data/nlp-table-data/pdfs'
StopwordFile='data/stopwords.txt'
#FreebaseMap='data/freebase_links.nt'
#FreebaseKey='AIzaSyBvkZaBXc1GzVs3d0QN2HjTjDZwlgxboW4' # set your own freebase key
SegmentOutFile='result/segmentNLP.txt'
#SeedFile='result/seed_yelp.txt'
significance="1"
capitalize="1"
maxLength='4' # maximal phrase length
minSup='10' # minimal support for phrases in candidate generation
#DataStatsFile='result/data_model_stats.txt' # data statistics on graph construction
#NumRelationPhraseClusters='50' # number of relation phrase clusters
#ResultFile='result/results.txt' # typed entity mentions
#ResultFileInText='result/resultsInText.txt' # typed mentions annotated in segmented text

###
rm -rf tmp
mkdir tmp

#rm -rf result
#mkdir result

### Candidate Generation
sentences_path="IntermediateNLP/sentences.txt"
full_sentence_path="IntermediateNLP/full_sentences.txt"
pos_path="IntermediateNLP/pos.txt"
full_pos_path="IntermediateNLP/full_pos.txt"
frequent_patterns_path="IntermediateNLP/frequentPatterns.pickle"
segmentInput='IntermediateNLP/phrase_segments.txt'
cd candidate_generation
rm -rf IntermediateNLP
mkdir IntermediateNLP
python DataPreprocessing/Clean.py $RawTextFiles 
python FrequentPhraseMining/FrequentPatternMining.py $segmentInput $maxLength $minSup 
python EntityExtraction/EntityRelation.py $sentences_path $full_sentence_path $pos_path $full_pos_path $frequent_patterns_path $significance $SegmentOutFile $capitalize
cd ..

### Entity Linking (DBpeidaSpotlight)

#cd entity_linking
#mkdir tmp
#python EntityLinking.py $RawText $TypeFile $FreebaseMap $SeedFile $FreebaseKey
#rm -rf tmp
#cd ..

### ClusType
#python src/step0-graph_construction.py $SegmentOutFile $StopwordFile $DataStatsFile
#python src/step1-entity_recognition.py $SegmentOutFile $SeedFile $TypeFile $NumRelationPhraseClusters $ResultFile $ResultFileInText
