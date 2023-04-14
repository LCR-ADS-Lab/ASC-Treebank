# Argument Structure Construction (ASC) tag annotation manual

This document provides an initial guideline of the ASC tags used.

If you have questions when tagging, please follow this procedure:
- Check the tagging scheme below.
- Check this [documentation](https://asc-treebank.readthedocs.io/en/latest/).
- Check these [slides](https://web.stanford.edu/~jurafsky/slp3/slides/22_SRL.pdf), if you need a brief introduction about the semantic roles (e.g., agent, path) used in <b>semantic frames</b>.
- <b>Bring up the issue in our weekly meeting</b>, if the annotations are ambigurous.

## ASC tagging Scheme
Here, each `tag` is described and examples of each are also given.

| **ASC tag**    | **Syntactic frame (example)**                      | **Semantic frame (example)**                                                |
|----------------|----------------------------------------------------|-----------------------------------------------------------------------------|
| **`ATTR`**       | Subj-V<sub>copular</sub>-NP                        | X<sub>theme</sub> is Y<sub>attribute</sub>                                  |
| **`INTRAN_S`**   | Subj-V                                             | X<sub>agent</sub> acts                                                      |
| **`INTRAN_MOT`** | Subj-V-Adverbial Particle/PP                       | X<sub>theme</sub> moves Y<sub>path</sub>                                    |
| **`INTRAN_RES`** | Subj-V-NP/AdjP                                     | X<sub>patient</sub> becomes Y<sub>result</sub>                              |
| **`TRAN_S`**     | Subj-V-Obj                                         | X<sub>agent</sub> acts on Y<sub>patient</sub>                               |
| **`DITRAN`**     | Subj-V-Obj<sub>indirect</sub>-Obj<sub>direct</sub> | X<sub>agent</sub> causes Y<sub>recipient</sub> to receive Z<sub>theme</sub> |
| **`CAUS_MOT`**   | Subj-V-Obj-PP                                      | X<sub>agent</sub> causes Y<sub>theme</sub> to move Z<sub>path/goal</sub>    |
| **`TRAN_RES`**   | Subj-V-Obj-NP                                      | X<sub>agent</sub> causes Y<sub>theme</sub> to become Z<sub>state</sub>      |
| **`PASSIVE`**    | Subj-auxV<sub>past participle</sub>(-*by*-PP)      | X<sub>theme</sub> undergo V (*by* Y<sub>agent</sug>)                        |


## ASC tagging steps

1. The provided data is structured in the [CoNLL-U format](https://universaldependencies.org/format.html), which presents each sentence in a vertical arragement. In this format, the columns are presented in the following order:

    1. ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
    
    2. FORM: Word form or punctuation symbol.
    
    3. LEMMA: Lemma or stem of word form (currently empty).
    
    4. UPOS: Universal part-of-speech tag.
    
    5. XPOS: Language-specific part-of-speech tag; underscore if not available.

    6. FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available (currently empty).

    7. HEAD: Head of the current word, which is either a value of ID or zero (0).

    8. DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.

    9. DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.

    10. MISC: Any other annotation.


2. Of the columns, `4`,`8` and `10` is important, because we will tag ASC on the `10`th column for either every `VERB` that appears in the `4`th column and every `root` that appears in the `8`th column (often they overlap). 

3. Practice with examples

- Example 1

    - Identify the VERB (located in column 4) and the root (located in column 8).
    - Determine the appropriate ASC tag by taking into account both syntactic and semantic frames.
    - Once you have decided on the ASC tag, enter it into the 10th column.

- Example 2

    - Occasionally, a sentence may be challenging to analyze due to its brevity (or many other reasons) when determining the appropriate ASC tag. 
    - Nevertherless, it is crucial to assign an ASC tag to every root that appears in the corpus.
    - For this example, I would rely on the syntactic frame to guide my decision.

- Example 3

    - In this case, you need to assign two ASC tags, as both `root` and `VERB` can be identified.
    - Keep in mind that the `TRAN_S` tag may include several subcategories (as well as a various semantic arguments) such as mental activities, explanations of a subject’s state, and communication activities such as speaking or writing.
