# Refine Vertical Treebank
# Used to exclude sentences that include Uncategorized ASCs

wd = '~/ASC-Treebank/' #change this to the location of your files

train = open(wd + "ASC Treebank Vertical Full/train.conllu").read().split("\n\n")
dev = open(wd + "ASC Treebank Vertical Full/dev.conllu").read().split("\n\n")
test = open(wd + "ASC Treebank Vertical Full/test.conllu").read().split("\n\n")

def refine_sents(loSents):
	nexcluded = 0
	refined = []
	for sent in loSents:
		if "\tUncategorized\n" in sent:
			nexcluded += 1
			continue
		else:
			refined.append(sent)
	print("Excluded sentence count:",nexcluded)
	return(refined)

def write_new(loSents,outname):
	with open(outname,"w") as outf:
		outf.write("\n\n".join(loSents))

len(train)
len(dev)
len(test)
write_new(refine_sents(train),wd + "ASC Treebank Vertical Refined/train.conllu")
write_new(refine_sents(dev),wd + "ASC Treebank Vertical Refined/dev.conllu")
write_new(refine_sents(test),wd + "ASC Treebank Vertical Refined/test.conllu")