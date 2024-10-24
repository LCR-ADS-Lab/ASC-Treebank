
import random

def multiReplace(targetList,loStr,original, target):
	for x in loStr:
		targetList.append(x.replace(original,target))

def multiReplace2(loStr,original, target):
	newL = []
	for x in loStr:
		newL.append(x.replace(original,target))
	return(newL)

def sortData(loSents,loPercs = [.2208,.3896,.3896]): 
	toSortList = []
	completedList = []
	for sent in loSents:
		lines = sent.split("\n")
		if lines[1] == "# dataset = en_eslwrit" and lines[2] == "# section = test":
			toSortList.append(sent)
		else:
			completedList.append(sent)
	print(len(toSortList))
	random.seed(1)
	random.shuffle(toSortList)
	to_train = toSortList[:int(len(toSortList)*loPercs[0])]
	print(len(to_train))
	to_dev = toSortList[int(len(toSortList)*loPercs[0]):int(len(toSortList)*(loPercs[0]+loPercs[1]))]
	print(len(to_dev))
	to_test = toSortList[int(len(toSortList)*(loPercs[0]+loPercs[1])):]
	print(len(to_test))

	to_train = multiReplace2(to_train,"# section = test","# section = train")
	for sent in to_train:
		completedList.append(sent)

	to_dev = multiReplace2(to_dev,"# section = test","# section = dev")
	for sent in to_dev:
		completedList.append(sent)

	return(completedList+to_test)

def sortDataSimple(loSents,dataset,loPercs): #added 20240112
	toSortList = []
	completedList = []
	for sent in loSents:
		lines = sent.split("\n")
		if lines[1] == dataset:
			toSortList.append(sent)
		else:
			completedList.append(sent)
	print("to sort:",len(toSortList))
	print("completed:",len(completedList))
	print("total",len(toSortList)+len(completedList))
	random.seed(23)
	random.shuffle(toSortList)
	index1 = int(len(toSortList)*loPercs[0])
	print("index1",index1)
	index2 = int(len(toSortList)*(loPercs[0]+loPercs[1]))
	print("index2",index2)
	to_train = toSortList[:index1]
	print(dataset,"n training:",len(to_train))
	to_dev = toSortList[index1:index2]
	print(dataset,"n dev:",len(to_dev))
	to_test = toSortList[index2:]
	print(dataset,"n test:",len(to_test))

	to_train = multiReplace2(to_train,"# section = test","# section = train")
	to_train = multiReplace2(to_train,"# section = dev","# section = train")
	for sent in to_train:
		completedList.append(sent)

	to_dev = multiReplace2(to_dev,"# section = train","# section = dev")
	to_dev = multiReplace2(to_dev,"# section = test","# section = dev")
	for sent in to_dev:
		completedList.append(sent)

	to_test = multiReplace2(to_test,"# section = train","# section = test")
	to_test = multiReplace2(to_test,"# section = dev","# section = test")
	for sent in to_test:
		completedList.append(sent)

	print("After Processing", len(completedList))
	return(completedList)

def writeFile(outname,loSents):
	outf = open(outname,"w")
	outf.write("\n\n".join(loSents) + "\n")
	outf.flush()
	outf.close()


### 20240111

### 20240114
#update eslwrit to make approx 801010
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldsents = open(targetPath + "datasets/goldSentences_database20231128.txt").read().strip().split("\n\n")

goldSentsReconf = sortData(goldsents)

writeFile(targetPath+ "datasets/goldSentences_database20231128_redistributed.txt",goldSentsReconf)


#50/25/25
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldsents = open(targetPath + "datasets/goldSentences_database20231128.txt").read().strip().split("\n\n")

#update spok
goldSents_502525 = sortDataSimple(goldsents,"# dataset = en_eslwrit",[.5,.25,.25])
#update writ
goldSents_502525 = sortDataSimple(goldSents_502525,"# dataset = en_eslspok",[.5,.25,.25])

writeFile(targetPath+ "datasets/goldSentences_database20231128_redistributed_502525.txt",goldSents_502525)

#34/33/33
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldsents = open(targetPath + "datasets/goldSentences_database20231128.txt").read().strip().split("\n\n")

#update spok
goldSents_343333 = sortDataSimple(goldsents,"# dataset = en_eslwrit",[.34,.33,.33])
#update writ
goldSents_343333 = sortDataSimple(goldSents_343333,"# dataset = en_eslspok",[.34,.33,.33])

writeFile(targetPath+ "datasets/goldSentences_database20231128_redistributed_343333.txt",goldSents_343333)

#from ASC_Frequencies.py
# goldRows = ['EWT-train',  'EWT-dev','EWT-test', 'en_eslwrit-train','en_eslwrit-dev','en_eslwrit-test', 'en_eslspok-train', 'en_eslspok-dev', 'en_eslspok-test']
# goldCols = ['ATTR', 'CAUS_MOT', 'DITRAN', 'INTRAN_MOT', 'INTRAN_RES', 'INTRAN_S', 'PASSIVE', 'TRAN_RES', 'TRAN_S']
# goldFreqByDatasetSection = byDatasetAndSectionFrequency(goldSentsReconf)
# goldTable = createCorpusTable(goldFreqByDatasetSection,goldRows,goldCols)