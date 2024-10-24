# Calculate Descriptive Statistics for ASCs
import json

def freq_update(item,freq_dict):
	if item not in freq_dict:
		freq_dict[item] = 1
	else:
		freq_dict[item] += 1

def freq_update2(asc,verb,freq_dict):
	if asc not in freq_dict:
		freq_dict[asc] = {"_totalFreq" : 1}
	else:
		freq_dict[asc]["_totalFreq"] += 1
		freq_update(verb,freq_dict[asc])

def simpleFrequency(sents):
	freqDict = {}

	for sent in sents:
		tokens  = sent.split("\n")
		for token in tokens:
			if token[0] == "#":
				continue
			items = token.split("\t")
			asc = items[9].strip()
			freq_update(asc,freqDict)
	return(freqDict)

def verbFrequency(sents):
	freqDict = {}

	for sent in sents:
		tokens  = sent.split("\n")
		for token in tokens:
			if token[0] == "#":
				continue
			items = token.split("\t")
			asc = items[9].strip()
			verb = items[1].lower().strip()
			freq_update2(asc,verb,freqDict)
	return(freqDict)

def byDatasetFrequency(sents):
	sentDict = {}
	freqDict = {}
	for sent in sents:
		tokens  = sent.split("\n")
		dataset = tokens[1].split(" ")[-1]#get dataset
		if dataset not in sentDict: 
			sentDict[dataset] = []
		sentDict[dataset].append(sent)
	for x in sentDict:
		freqDict[x] = simpleFrequency(sentDict[x])
	
	return(freqDict)

def byDatasetAndSectionFrequency(sents):
	sentDict = {}
	freqDict = {}
	for sent in sents:
		tokens  = sent.split("\n")
		dataset = tokens[1].split(" ")[-1]#get dataset
		section = tokens[2].split(" ")[-1]#get section
		datasetSection = "-".join([dataset,section])
		if datasetSection not in sentDict: 
			sentDict[datasetSection] = []
		sentDict[datasetSection].append(sent)
	for x in sentDict:
		freqDict[x] = simpleFrequency(sentDict[x])
	
	return(freqDict)

def bySectionFrequency(sents):
	sentDict = {}
	freqDict = {}
	for sent in sents:
		tokens  = sent.split("\n")
		section = tokens[2].split(" ")[-1]#get section
		if section not in sentDict: 
			sentDict[section] = []
		sentDict[section].append(sent)
	for x in sentDict:
		freqDict[x] = simpleFrequency(sentDict[x])
	
	return(freqDict)

def createCorpusTable(corpDict,loRows,loCols):
	outl = []
	#create header:
	header = ["dataset"]
	for col in loCols:
		header.append(col)
	outl.append(header)
	#add data:
	for row in loRows:
		rowList = [row]
		for col in loCols:
			if col in corpDict[row]:
				rowList.append(corpDict[row][col])
			else:
				rowList.append(0)
		outl.append(rowList)
	for r in outl:
		print("\t".join([str(x) for x in r]))
	return(outl)

def createCorpusTable2(corpDict,loRows,loCols): #need to finish this with ASCs as rows and dataset as columns
	outl = []
	#create header:
	header = ["ASC"]
	for col in loCols:
		header.append(col)
	outl.append(header)
	#add data:
	for row in loRows:
		rowList = [row]
		for col in loCols:
			if row in corpDict[col]:
				rowList.append(corpDict[col][row])
			else:
				rowList.append(0)
		outl.append(rowList)
	for r in outl:
		print("\t".join([str(x) for x in r]))
	return(outl)


def writeTable(outname,loRows):
	outf = open(outname,"w")
	outl = []
	for row in loRows:
		outl.append("\t".join([str(x) for x in row]))
	outf.write("\n".join(outl))
	outf.flush()
	outf.close()

def readSpacyEval(loJsonPaths):
	outd = {}
	for jsonPath in loJsonPaths:
		simpleName = jsonPath.split("/")[-1]
		outd[simpleName] = json.load(open(jsonPath))
	return(outd)

def spacyEvalTableMaker(evalDict,colList,rowList,key = "f"):
	header = ["Entity"]
	for col in colList:
		header.append(col)
	entTableList = [header]
	for row in rowList:
		line = [row] #add ent type
		for col in colList:
			line.append(evalDict[col]['ents_per_type'][row][key])
		entTableList.append(line)
	totalLine = ["macroAv"]
	for col in colList:
		totalLine.append(evalDict[col]['ents_'+key])
	entTableList.append(totalLine)
	return(entTableList)

targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'

goldSents = open(targetPath + "datasets/goldSentences_database20231128_redistributed.txt").read().strip().split("\n\n")
silverSents = open(targetPath + "datasets/silverSentences_database20231128.txt").read().strip().split("\n\n")

goldFreq = simpleFrequency(goldSents) #{'_': 140938, 'ATTR': 4588, 'TRAN_S': 9967, 'DITRAN': 482, 'INTRAN_MOT': 1097, 'INTRAN_S': 2582, 'TRAN_RES': 855, 'PASSIVE': 1312, 'INTRAN_RES': 280, 'CAUS_MOT': 906}
silverFreq = simpleFrequency(silverSents) #{'_': 115374, 'TRAN_S': 8025, 'DITRAN': 347, 'INTRAN_S': 1792, 'PASSIVE': 1196, 'ATTR': 3995, 'INTRAN_MOT': 710, 'TRAN_RES': 141, 'CAUS_MOT': 97, 'INTRAN_RES': 15}

goldFreqByDataset = byDatasetFrequency(goldSents)
silverFreqByDataset = byDatasetFrequency(silverSents)

goldFreqByDatasetSection = byDatasetAndSectionFrequency(goldSents)
silverFreqDatasetSection = byDatasetAndSectionFrequency(silverSents)

goldRows = ['EWT-train',  'EWT-dev','EWT-test', 'en_eslwrit-train','en_eslwrit-dev','en_eslwrit-test', 'en_eslspok-train', 'en_eslspok-dev', 'en_eslspok-test']
goldCols = ['ATTR', 'CAUS_MOT', 'DITRAN', 'INTRAN_MOT', 'INTRAN_RES', 'INTRAN_S', 'PASSIVE', 'TRAN_RES', 'TRAN_S']

goldTable = createCorpusTable(goldFreqByDatasetSection,goldRows,goldCols)

writeTable(targetPath + "goldTable_20240111.txt",goldTable)

###20240112

targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'

goldSents = open(targetPath + "datasets/goldSentences_database20231128_redistributed_502525.txt").read().strip().split("\n\n")
goldFreqByDatasetSection = byDatasetAndSectionFrequency(goldSents)

goldRows = ['EWT-train',  'EWT-dev','EWT-test', 'en_eslwrit-train','en_eslwrit-dev','en_eslwrit-test', 'en_eslspok-train', 'en_eslspok-dev', 'en_eslspok-test']
goldCols = ['ATTR', 'CAUS_MOT', 'DITRAN', 'INTRAN_MOT', 'INTRAN_RES', 'INTRAN_S', 'PASSIVE', 'TRAN_RES', 'TRAN_S']
goldTable = createCorpusTable(goldFreqByDatasetSection,goldRows,goldCols)
writeTable(targetPath + "goldTable_20240112_502525.txt",goldTable)

###20240113 Make eval tables
evalpath1 = "/Users/kristopherkyle/Library/CloudStorage/GoogleDrive-kristopherkyle1@gmail.com/My Drive/Programming/ASC Analysis/Analyses/datasets/goldSentences_database20231128_redistributed_343333_lemma/eval/"
evalList1 = [evalpath1+"V1-eslspok-343333-test_metrics.json",evalpath1+"V1-eslspok-502525-test_metrics.json",evalpath1+"V2-343333-eslspok-343333-test_metrics.json"]
evalDict = readSpacyEval(evalList1)
evalColList1 = ["V1-eslspok-343333-test_metrics.json","V1-eslspok-502525-test_metrics.json","V2-343333-eslspok-343333-test_metrics.json"]

sampleEvalTable = spacyEvalTableMaker(evalDict,evalColList1,goldCols)

for x in sampleEvalTable:
	print("\t".join([str(y) for y in x]))

###20240114 Run Tables
datasetCols = ['EWT-train',  'EWT-dev','EWT-test', 'en_eslwrit-train','en_eslwrit-dev','en_eslwrit-test', 'en_eslspok-train', 'en_eslspok-dev', 'en_eslspok-test']
datasetRows = ['ATTR', 'CAUS_MOT', 'DITRAN', 'INTRAN_MOT', 'INTRAN_RES', 'INTRAN_S', 'PASSIVE', 'TRAN_RES', 'TRAN_S']

#original
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldSents = open(targetPath + "datasets/goldSentences_database20231128.txt").read().strip().split("\n\n")
goldSentsFreqByDatasetSection = byDatasetAndSectionFrequency(goldSents)

goldSentsTable = createCorpusTable2(goldFreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_freqTable.txt",goldSentsTable)

#801010
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldSents801010 = open(targetPath + "datasets/goldSentences_database20231128_redistributed.txt").read().strip().split("\n\n")
goldSents801010FreqByDatasetSection = byDatasetAndSectionFrequency(goldSents801010)

goldSents801010Table = createCorpusTable2(goldSents801010FreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_redistributed_freqTable.txt",goldSents801010Table)

#343333
goldSents343333 = open(targetPath + "datasets/goldSentences_database20231128_redistributed_343333.txt").read().strip().split("\n\n")
goldSents343333FreqByDatasetSection = byDatasetAndSectionFrequency(goldSents343333)

goldSents343333Table = createCorpusTable2(goldSents343333FreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_redistributed_343333_freqTable.txt",goldSents343333Table)

#502525
goldSents502525 = open(targetPath + "datasets/goldSentences_database20231128_redistributed_502525.txt").read().strip().split("\n\n")
goldSents502525FreqByDatasetSection = byDatasetAndSectionFrequency(goldSents502525)

goldSents502525Table = createCorpusTable2(goldSents502525FreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_redistributed_502525_freqTable.txt",goldSents502525Table)

### 20240118 Compile eval tables
evalpath1 = "/Users/kristopherkyle/Library/CloudStorage/GoogleDrive-kristopherkyle1@gmail.com/My Drive/Programming/ASC Analysis/Analyses/datasets/evals/"
evalList1 = [evalpath1+"343333-eslspok-343333-test_metrics.json",evalpath1+"343333-eslwrit-343333-test_metrics.json",evalpath1+"343333-EWT-343333-test_metrics.json",evalpath1+"502525-eslspok-502525-test_metrics.json",evalpath1+"502525-eslwrit-502525-test_metrics.json",evalpath1+"EWTonly-eslspok-343333-test_metrics.json",evalpath1+"EWTonly-eslspok-502525-test_metrics.json",evalpath1+"EWTonly-eslwrit-343333-test_metrics.json",evalpath1+"EWTonly-eslwrit-502525-test_metrics.json",evalpath1+"EWTonly-EWT-test_metrics.json",evalpath1+"V1-eslspok-343333-test_metrics.json",evalpath1+"V1-eslspok-502525-test_metrics.json",evalpath1+"V1-eslspok-801010-test_metrics.json",evalpath1+"V1-eslwrit-343333-test_metrics.json",evalpath1+"V1-eslwrit-502525-test_metrics.json",evalpath1+"V1-eslwrit-801010-test_metrics.json",evalpath1+"V1-EWT-343333-test_metrics.json"]
evalDict = readSpacyEval(evalList1)
evalColList1 = ["343333-eslspok-343333-test_metrics.json","343333-eslwrit-343333-test_metrics.json","343333-EWT-343333-test_metrics.json","502525-eslspok-502525-test_metrics.json","502525-eslwrit-502525-test_metrics.json","EWTonly-eslspok-343333-test_metrics.json","EWTonly-eslspok-502525-test_metrics.json","EWTonly-eslwrit-343333-test_metrics.json","EWTonly-eslwrit-502525-test_metrics.json","EWTonly-EWT-test_metrics.json","V1-eslspok-343333-test_metrics.json","V1-eslspok-502525-test_metrics.json","V1-eslspok-801010-test_metrics.json","V1-eslwrit-343333-test_metrics.json","V1-eslwrit-502525-test_metrics.json","V1-eslwrit-801010-test_metrics.json","V1-EWT-343333-test_metrics.json"]

sampleEvalTable = spacyEvalTableMaker(evalDict,evalColList1,datasetRows,key = "f")

for x in sampleEvalTable:
	print("\t".join([str(y) for y in x]))
writeTable(evalpath1 + "combinedF1scores-2024-01-18.txt",sampleEvalTable)

#compile sections
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'

#original
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldSents = open(targetPath + "datasets/goldSentences_database20231128.txt").read().strip().split("\n\n")
goldSentsFreqByDatasetSection = byDatasetAndSectionFrequency(goldSents)

goldSentsTable = createCorpusTable2(goldFreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_freqTable.txt",goldSentsTable)

#801010
targetPath = '/Users/kristopherkyle/Desktop/Programming/GitHub/LCR-ADS-Lab/ASC-Treebank/ASC-Treebank-V2/'
goldSents801010 = open(targetPath + "datasets/goldSentences_database20231128_redistributed.txt").read().strip().split("\n\n")
goldSents801010FreqByDatasetSection = byDatasetAndSectionFrequency(goldSents801010)

goldSents801010Table = createCorpusTable2(goldSents801010FreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_redistributed_freqTable.txt",goldSents801010Table)

#343333
goldSents343333 = open(targetPath + "datasets/goldSentences_database20231128_redistributed_343333.txt").read().strip().split("\n\n")
goldSents343333FreqByDatasetSection = byDatasetAndSectionFrequency(goldSents343333)

goldSents343333Table = createCorpusTable2(goldSents343333FreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_redistributed_343333_freqTable.txt",goldSents343333Table)

#502525
goldSents502525 = open(targetPath + "datasets/goldSentences_database20231128_redistributed_502525.txt").read().strip().split("\n\n")
goldSents502525FreqByDatasetSection = byDatasetAndSectionFrequency(goldSents502525)

goldSents502525Table = createCorpusTable2(goldSents502525FreqByDatasetSection,datasetRows,datasetCols)
writeTable(targetPath + "datasets/goldSentences_database20231128_redistributed_502525_freqTable.txt",goldSents502525Table)
