# Argument Structure Construction (ASC) tag annotation manual

This document provides an initial guideline of the ASC tags used.

If you have questions when tagging, please follow this procedure:
- Check the tagging scheme below.
- Check the detalied <a href="https://asc-treebank.readthedocs.io/en/latest/ASC%20guideline.html" target="_blank">guidelines</a> for each tag.
- Check these <a href="https://web.stanford.edu/~jurafsky/slp3/slides/22_SRL.pdf" target="_blank">slides</a>, if you need a brief introduction about the semantic roles (e.g., agent, path) used in <b>semantic frames</b>.
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

```
    1. ID: Word index.
    2. FORM: Word form or punctuation symbol.
    3. LEMMA: Lemma or stem of word form (currently empty).
    4. UPOS: Universal part-of-speech tag.
    5. XPOS: Language-specific part-of-speech tag; underscore if not available.
    6. FEATS: List of morphological features from the universal feature inventory (currently empty).
    7. HEAD: Head of the current word, which is either a value of ID or zero (0).
    8. DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0).
    9. DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
    10. MISC: Any other annotation.
```

2. Among the columns, `4`, `8`, and `10` are crucial, as we will tag the ASC in the 10th column for every `VERB` that appears in the `4th` column. In most cases, this overlaps with the `root` found in the `8th` column. 

### Practice with examples

##### Example 1
<img src="https://user-images.githubusercontent.com/84297888/232111316-5ab514ed-bfeb-4774-a3c5-cabf97cab336.png" width="550" alt="example image1-1">
  
  - Identify the VERB (located in column 4) and the root (located in column 8).
  - Determine the appropriate ASC tag by taking into account both syntactic and semantic frames.
  - Once you have decided on the ASC tag, enter it into the 10th column.
<img src="https://user-images.githubusercontent.com/84297888/232111999-e5c869ad-5388-41b7-a5db-96dfe2414268.png" width="550" alt="example image1-2">


##### Example 2
<img src="https://user-images.githubusercontent.com/84297888/232112756-d7b80fc2-61d7-4ca8-b315-13e49875d2f3.png" width="550" alt="example image2">

 - Occasionally, a sentence may have a root but no verb, particularly when the data originates from spoken discourse.
 - In such examples, we will not assign any ASC tag to the sentence, as it lacks the necessary components for accurate analysis and processing.

##### Example 3
<img src="https://user-images.githubusercontent.com/84297888/232115934-1209d37e-027c-48c2-b064-539c28903c2a.png" width="550" alt="example image3-1">

 - In this case, you need to assign three ASC tags, as the `VERB` can be identified three times in a given snetence.
 - Keep in mind that the `TRAN_S` tag may include several subcategories (as well as a various semantic arguments) such as mental activities, explanations of a subject’s state, and communication activities such as speaking or writing.
 - For the last verb `eat`, even though we cannot directly identify the object of the verb in the syntactic frame, it is essential to consider its meaning (as we can infer the object of the verb while reading the sentence, i.e., `what`).
    
<img src="https://user-images.githubusercontent.com/84297888/232117260-8eb7616b-5ae7-48e2-8df1-ecd688516549.png" width="550" alt="example image3-2">

    
