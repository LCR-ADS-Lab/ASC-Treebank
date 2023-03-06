# ASC-Treebank


## Basic information
This is the repository for the Argument Structure Construction (ASC) Treebank.
The ASC Treebank was used to train a Spacy transformer model that annotates ASCs with a high degree of accuracy (F1 = .918). 

### ASC tags overview
Learned correspondences between form and function vary in terms of complexity and abstractionm, and so do the examples of the ASCs. There is currently no definitive set of ASCs that should be included in an ASC tagset. The current study drew on a range of previous literature and selected nine ASC types as a tagset. 

| **ASC tag**    | **Syntactic frame (example)**                      | **Semantic frame (example)**                                                |
|----------------|----------------------------------------------------|-----------------------------------------------------------------------------|
| **ATTR**       | Subj-V<sub>copular</sub>-NP                        | X<sub>theme</sub> is Y<sub>attribute</sub>                                 |
| **INTRAN_S**   | Subj-V                                             | X<sub>agent</sub> acts                                                      |
| **INTRAN_MOT** | Subj-V-Adverbial Particle/PP                                    | X<sub>theme</sub> moves Y<sub>path</sub>                                    |
| **INTRAN_RES** | Subj-V-NP/AdjP                                     | X<sub>patient</sub> becomes Y<sub>result</sub>                              |
| **TRAN_S**     | Subj-V-Obj                                         | X<sub>agent</sub> acts on Y<sub>patient</sub>                               |
| **DITRAN**     | Subj-V-Obj<sub>indirect</sub>-Obj<sub>direct</sub> | X<sub>agent</sub> causes Y<sub>recipient</sub> to receive Z<sub>theme</sub> |
| **CAUS_MOT**   | Subj-V-Obj-PP                                      | X<sub>agent</sub> causes Y<sub>theme</sub> to move Z<sub>path/goal</sub>    |
| **TRAN_RES**   | Subj-V-Obj-NP                                      | X<sub>agent</sub> causes Y<sub>theme</sub> to become Z<sub>state</sub>      |
| **PASSIVE**    | Subj-auxV<sub>past participle</sub>(-*by*-PP)      | X<sub>theme</sub> undergo V (*by* Y<sub>agent</sug>)                        |


## Documentation

The documenation for the ASC-Treebank is available [here](https://asc-treebank.readthedocs.io/en/latest/).

## Demo
The annotation model (including a demo) is available [here](https://huggingface.co/kriskyle/en_pipeline).

## Citation
If you use the model or the treebank, please cite [this paper](https://aclanthology.org/2023.cxgsnlp-1.7/):

Kyle, K. & Sung, H. (2023). An argument structure construction treebank, CxG+NLP, GURT (Georgetown University Round Table) 2023.


## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.







