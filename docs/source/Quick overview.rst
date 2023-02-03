Quick overview
=====

***** 
ASC Tagset
*****

Learned correspondences between form and function vary in terms of complexity and abstraction (e.g., Fillmore, Kay, & O'Connor, 1998; Goldberg, 2013), and so do the examples of the ASCs. There is currently no definitive set of ASCs that should be included in an ASC tagset. The current study drew on a range of previous literature (e.g., Biber et al., 1999; Goldberg, 1995; 2006; Hwang & Kim, 2022) and selected **nine ASC types** as a tagset. These are briefly summarized below with frequently occuring syntactic(Kyle, 2016; Kyle & Crossley, 2017; Kyle et al., 2021) and semantic (Fillmore, 1968; Palmer et al., 2005; Palmer, Gildea, & Xue, 2010) frames. 

+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| ASC tag           | Syntactic frame (example)                        | Semantic frame (example)                                               |
+===================+==================================================+========================================================================+
| :ref:`ATTR`       | Subj-V\ :sub:`copular`-NP/AdjP/PP                | X\ :sub:`theme`  is Y\ :sub:`attribute`                                |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`INTRAN_S`   | Subj-V                                           | X\ :sub:`agent` acts                                                   |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`INTRAN_MOT` | Subj-V-AdvPr/PP                                  | X\ :sub:`theme` moves Y\ :sub:`path`                                   |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`INTRAN_RES` | Subj-V-NP/AdjP                                   | X\ :sub:`patient` becomes Y\ :sub:`result`                             |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`TRAN_S`     | Subj-V-Obj                                       | X\ :sub:`agent` acts on Y\ :sub:`patient`                              |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`DITRAN`     | Subj-V-Obj\ :sub:`indirect`-Obj\ :sub:`direct`   | X\ :sub:`agent` causes Y\ :sub:`recipient` to receive Z\ :sub:`theme`  |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`CAUS_MOT`   | Subj-V-Obj-PP                                    | X\ :sub:`agent` causes Y\ :sub:`theme` to move Z\ :sub:`path/goal`     |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`TRAN_RES`   | Subj-V-Obj-NP/AdjP                               | X\ :sub:`agent` causes Y\ :sub:`theme` to become Z\ :sub:`state`       |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+
| :ref:`PASSIVE`    | Subj-auxV\ :sub:`past participle` (-*by*-PP)     | X\ :sub:`theme` undergo V  (*by* Y\ :sub:`agent`)                      |
+-------------------+--------------------------------------------------+------------------------------------------------------------------------+



***** 
Dataset
*****
We developed an ASC treebank by building on the English portion of the Universal Propositions (UP) project (Akbik et al., 2015). The project represents a merge of the Universal Dependencies version of the English Web Treebank (EWT; Bies et al., 2012; Silveira et al., 2014) and PropBank (Palmer et al., 2005). The EWT corpus includes sentences from five web registers including blogs, newsgroups, emails, reviews, and Yahoo! Answers. 


***** 
Creating an ASC treebank
*****
#. For each sentence in the training section of EWT, we extracted the large-grained argument structures using the default PropBank semantic role labels (e.g., *ARG0*-Verbsense-*ARG1*).
#. We converted the large-grained arguments to fine-grained semantic role frames (e.g., *agent*-V-*theme*), using relation mappings from PropBank frame files (Palmer et al., 2005), which also draws on information in FrameNet (Fillmore et al., 2003) and VerbNet (Schuler, 2005).
#. Based on a discussion of ASC categorization between the authors that included co-annotation of 100 sentences, we manually assigned an ASC to each semantic role frame that occured at least times in the corpus (*n* = 355). For example, the semantic role frame *theme-Verb-attribute* was annotated as an attributive construction and *agent-Verb-theme* was annotated as a transitive simple construction.
#. In some cases, the corpus analysis indicated that particular semantic role frames could represent multiple ASCs. This most often occurred in cases where a fine-grained semantic role for a particular argument of a particular verb was unavailable in PropBank, leading to an underspecified semantic role frame. In these cases, the use of each 'semantic role frame + verb' combination that occurred at least twice in the treebank was checked and each was assigned an ASC.
#. Particularly ambiguous cases were resolved through discussions between the authors.
#. As a final step, we conducted spot checks which led to a small number of corrections. This approach resulted in the categorization of 94.1% of the ASCs in the treebank. Any sentences that included uncategorized ASCs were omitted from further analysis.
#. We also evaluated the quality of the semi-automated annotation process (for more information, see Kyle & Sung (2023)).

***** 
ASC representation in Treebank
*****

+-------------+----------------------+-------------+--------+--------+-------+
| ASC         | Most frequent verbs  | Total Freq  | Train  | Dev    | Test  |
+=============+======================+=============+========+========+=======+
| TRAN_S      | *have, do, say*      | 12,431      | 9,965  | 1,213  | 1,253 |
+-------------+----------------------+-------------+--------+--------+-------+
| ATTR        | *be, seem, look*     | 6,004       | 4,723  | 648    | 633   |
+-------------+----------------------+-------------+--------+--------+-------+
| INTRAN_S    | *go, work, come*     | 2,754       | 2,200  | 289    | 265   |
+-------------+----------------------+-------------+--------+--------+-------+
| PASSIVE     | *attach, do, call*   | 1,818       | 1,481  | 167    | 170   |
+-------------+----------------------+-------------+--------+--------+-------+
| INTRAN_MOT  | *go, come, get*      | 1,098       | 915    | 88     | 95    |
+-------------+----------------------+-------------+--------+--------+-------+
| TRAN_RES    | *let, make, get*     | 977         | 795    | 90     | 92    |
+-------------+----------------------+-------------+--------+--------+-------+
| CAUS_MOT    | *take, put, send*    | 675         | 546    | 64     | 65    |
+-------------+----------------------+-------------+--------+--------+-------+
| DITRAN      | *give, tell, ask*    | 534         | 448    | 40     | 46    |
+-------------+----------------------+-------------+--------+--------+-------+
| INTRAN_RES  | *become, go, come*   | 146         | 121    | 9      | 16    |
+-------------+----------------------+-------------+--------+--------+-------+
| Total       |                      | 26,437      | 21,194 | 2,608  | 2,635 |
+-------------+----------------------+-------------+--------+--------+-------+


