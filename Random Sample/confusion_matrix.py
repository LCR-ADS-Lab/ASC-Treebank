from sklearn.metrics import confusion_matrix, cohen_kappa_score

eval_file = open("Annotated/Eval2_simple.csv").read().split("\n")
#len(eval_file)

def make_anno_list(evals,col,sep = ","):
	outl = []
	for row in evals:
		#print(row[0])
		if row[0] in ["#","",'',"0"]: #skip first row and blank rows
			continue
		if len(row.split(sep)[col]) > 1:
			outl.append(row.split(sep)[col])
	return(outl)

anno1L = make_anno_list(eval_file,0)
#len(anno1L)
anno2L = make_anno_list(eval_file,1)
#len(anno2L)
cfsMtrx1 = confusion_matrix(anno1L,anno2L)
interannotator_Kappa = cohen_kappa_score(anno1L,anno2L)

adjudicated = make_anno_list(eval_file,2)
algo = make_anno_list(eval_file,3)
cfsMtrx2 = confusion_matrix(adjudicated,algo)
algo_Kappa = cohen_kappa_score(adjudicated,algo)
