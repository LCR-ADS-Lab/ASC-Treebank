# This script is used to create a random sample of sentences to be manually evaluated
import random
random.seed(1234)

def filterUncategorized(loS): #takes list of conllu-like sentences as an argument, returns a list of conllu-like sentences that do not include uncategorized ASCs
	filteredList = [] #filtered list to output
	for sent in loS: #iterate through sentences
		keep = True #boolean to keep track of whether uncategorized ASCs are in the sentence
		for line in sent.split("\n"): #iterate through lines in sentence
			if line[0] == "#": #skip metadata
				continue
			cols = line.split("\t") #split each line into columns
			# if len(cols) > 13:
			# 	print(cols[13])
			if len(cols) > 13 and cols[13] == "Uncategorized": #check for uncategorized ASCs
				keep = False
		if keep == True:
			filteredList.append(sent) #if no uncategorized ASCs were found, then add the sentence to the filtered list
	return(filteredList)

def deleteASC(loS): #takes a list of conllu-like sentences (with ASC annotation) as an argument and returns a version without the ASC
	filteredList = [] #filtered list to output
	for sent in loS: #iterate through sentences
		new_sent = []
		for line in sent.split("\n"): #iterate through lines in sentence
			if line[0] == "#": #skip metadata
				new_sent.append(line)
				continue
			cols = line.split("\t") #split each line into columns
			if len(cols) > 13:
				cols[13] = "" # delete ASC text
				new_sent.append("\t".join(cols))
			else:
				new_sent.append("\t".join(cols))
		filteredList.append("\n".join(new_sent)) #add edited sentence to list
	return(filteredList)

#load data
ascTbTrain = open("ASC Treebank Vertical/train.conllu").read().split("\n\n")
# len(ascTbTrain)
# ascTbTrain[1]

#filter data
filteredTrain = filterUncategorized(ascTbTrain)
# len(filteredTrain)
# filteredTrain[1]

#get random sample
randomFilteredTrain = random.sample(filteredTrain,100)
len(randomFilteredTrain)

cleanedRandomFilteredTrain = deleteASC(randomFilteredTrain)

#algorithm-based annotations
algoOut = open("Random Sample/algo-derived.conllu","w")
algoOut.write("\n\n".join(randomFilteredTrain))
algoOut.flush()
algoOut.close()

anno1Out = open("Random Sample/anno1.conllu","w")
anno1Out.write("\n\n".join(cleanedRandomFilteredTrain))
anno1Out.flush()
anno1Out.close()

#copy for annotator 2
anno2Out = open("Random Sample/anno2.conllu","w")
anno2Out.write("\n\n".join(cleanedRandomFilteredTrain))
anno2Out.flush()
anno2Out.close()

### Data for getting reacquainted with annotation
#get random sample
randomFilteredTrainTiny = random.sample(filteredTrain,10)
len(randomFilteredTrainTiny)

#algorithm-based annotations
algoOut = open("Random Sample/algo-derived-tiny.conllu","w")
algoOut.write("\n\n".join(randomFilteredTrainTiny))
algoOut.flush()
algoOut.close()

anno1Out = open("Random Sample/anno1-tiny.conllu","w")
anno1Out.write("\n\n".join(deleteASC(randomFilteredTrainTiny)))
anno1Out.flush()
anno1Out.close()

#copy for annotator 2
anno2Out = open("Random Sample/anno2-tiny.conllu","w")
anno2Out.write("\n\n".join(deleteASC(randomFilteredTrainTiny)))
anno2Out.flush()
anno2Out.close()




