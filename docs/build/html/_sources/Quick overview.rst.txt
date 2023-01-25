Quick overview
=====

***** 
ASC Tagset
*****

Learned correspondences between form and function vary in terms of complexity and abstraction (e.g., Fillmore, Kay, & O'Connor, 1998; Goldberg, 2013), and so do the examples of the ASCs. There is currently no definitive set of ASCs that should be included in an ASC tagset. The current study drew on a range of previous literature (e.g., Biber et al., 1999; Goldberg, 1995; 2006; Hwang & Kim, 2022) and selected nine ASC types as a tagset. 


+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| ASC tag     | Description               | Form (example)                                   | meaning                                   |
+=============+===========================+==================================================+===========================================+
| ATTR        | attributive               | Subj V :sup:`copular` NP                         | X is Y :sub:`attribute`                   |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| INTRAN_S    | intransitive simple       | Subj V                                           | X acts                                    |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| INTRAN_MOT  | intransitive motion       | Subj V Obl                                       | X moves Y :sub:`path`                     |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| INTRAN_RES  | intransitive resultative  | Subj V RP                                        | X becomes Y :sub:`result`                 |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| TRAN_S      | transitive simple         | Subj V Obj                                       | X acts on Y                               |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| DITRAN      | ditransitive              | Subj V Obj :sub:`1` Obj :sub:`2`                 | X causes Y to receive Z                   |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| CAUS_MOT    | caused-motion             | Subj V Obj Obl                                   | X causes Y to move Z :sub:`path/goal`     |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| TRAN_RES    | transitive resultative    | Subj V Obj RP                                    | X causes Y to become Z :sub:`state`       |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+
| PASSIVE     | passive                   | Subj aux V :sup:`past participle` (*by*-PP)      | X undergo V  (*by* Y)                     |
+-------------+---------------------------+--------------------------------------------------+-------------------------------------------+

***** 
Dataset
*****
We developed ASC treebank by building on the English portion of the Universal Propositions (UP) project (Akbik et al., 2015). The project represents a merge of the Universal Dependencies version of the English Web Treebank (EWT; Bies et al., 2012; Silveira et al., 2014) and PropBank (Palmer et al., 2005). The EWT corpus includes sentences from five web registers including blogs, newsgroups, emails, reviews, and Yahoo! Answers. For more information about how we created an ASC treebank using this dataset, please refer to Kyle & Sung (2023).
