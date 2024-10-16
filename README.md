# ASC-Treebank

## Basic information
This is the repository for the Argument Structure Construction (ASC) Treebank.
The ASC Treebank was used to train a Spacy transformer model that annotates ASCs with a high degree of accuracy (L1: F1 = .912; L2-written: F1 = .915; L2-spoken: F1 = .928). 

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

- The documenation for the ASC-Treebank is available [online](https://asc-treebank.readthedocs.io/en/latest/).
- The more detailed version of the documentation for the ASC-Treebank construction (based on manual annotations) is available in [PDF format](./docs/PDFmanuals/ASC_manual_240301.pdf).

## Demo
The annotation model (including a demo) is available [here](https://huggingface.co/kriskyle/en_pipeline) (*and will be upated with a new model soon*).

## Citation
If you use the model or the treebank, please refer to the following papers:

Kyle, K. & Sung, H. (2023). [An argument structure construction treebank](https://aclanthology.org/2023.cxgsnlp-1.7/), In *Proceedings of the First International Workshop on Construction Grammars and NLP (CxGs+NLP, GURT/SyntaxFest 2023)*, 51–62, Association for Computational Linguistics.

Sung, H., & Kyle, K. (2024). [Annotation Scheme for English Argument Structure Constructions Treebank](https://aclanthology.org/2024.law-1.2/). In *Proceedings of The 18th Linguistic Annotation Workshop (LAW-XVIII)*, 12-18, Association for Computational Linguistics.

Sung, H., & Kyle, K. (in press). [Leveraging pre-trained language models for linguistic analysis: A case of argument structure constructions](./24_ASC-EMNLP-dataset/Sung_Kyle_EMNLP24_camera_ready.pdf). In *the Association for Computational Linguistics: EMNLP 2024*.

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.







