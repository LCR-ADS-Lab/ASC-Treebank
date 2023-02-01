***** 
Related projects
*****

We build on previous related projects to create a publicly available treebank of ASCs. 

-----
PropBank
-----
* PropBank project identified and labeled the semantic arguments on the verb.
* Tagsets [for more information, see Guidelines_ (Bonial, Babko-Malaya, Choi, Hwang, & Palmer, 2010)]

.. _Guidelines: https://clear.colorado.edu/compsem/documents/propbank_guidelines.pdf
  
::

  Arg0: PROTO-AGENT
  Arg1: PROTO-PATIENT
  Arg2: benefactive, instrument, attribute
  Arg3: the starting point, benefactive, instrument, Attributive
  Arg4: end point
  ArgM-: (includes a number of modifiers such as TMP, LOC, GOL, etc.)

* A set of widely recognized semantic roles (from Palmer, Gildea, & Xue, N, 2011, p.4)

+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Role         | Description                                    | Examples                                                              |
+==============+================================================+=======================================================================+
| Agent        | Initiator of action, capable of volition       | **The batter** smashed the pitch into left field                      |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Patient      | Affected by action, undergoes change of state  | David trimmed **his beard**                                           |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Theme        | Entity moving, or being “located”              | Poala threw **the Frisbee**; **The picture** hangs above the fireplace|
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Experiencer  | Perceives action but not in control            | **He** tasted the delicate flavor of the baby lettuce                 |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Beneficiary  | For whose benefit action is performed          | He sliced **me** a large chunk of prime rib                           |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Instrument   | Intermediary/means used to perform an action   | He shot the wounded buffalo with **a rifle**                          |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Location     | Place of object or action                      | There are some real monsters hiding **in the anxiety closet**         |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Source       | Starting point                                 | The jet took off **from Nairobi**                                     |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+
| Goal         | Ending point                                   | The ball rolled **to the other end of the hall**                      |
+--------------+------------------------------------------------+-----------------------------------------------------------------------+



* References 

  * Palmer, M., Gildea, D., & Kingsbury, P. (2005). The proposition bank: An annotated corpus of semantic roles. *Computational linguistics, 31* (1), 71-106.

  * Palmer, M., Gildea, D., & Xue, N. (2011). *Semantic role labeling*. Morgan & Claypool Publishers.

-----
FrameNet
-----
* FrameNet project identified and labeled frame elements (similar to semantic roles) mostly based on a verb.
* Frame elements are less verb specific, but they defined in terms of overall semantic structures (i.e., frames) evoked by the verb; one or more verbs can be associated with a single semantic frame (Hwang, Nielsen, & Palmer, 2010)

* References 

  * Fillmore, C. J., Johnson, C. R., & Petruck, M. R. (2003). Background to framenet. *International journal of lexicography, 16* (3), 235-250.
  
  * See also https://framenet.icsi.berkeley.edu/fndrupal/ 

-----
VerbNet
-----
* VerbNet project demonstrated more specific semantic classes of verbs.
* Similar verbs that share similar syntactic realization (frames) based on Levin (1993) were grouped.

* References 

  * Schuler, Karin Kipper. 2005. *VerbNet: A Broad-Coverage, Comprehensive Verb Lexicon*. PhD Dissertation. University of Pennsylvania.

  * See also https://verbs.colorado.edu/verbnet/
  
-----
Universal Proposition (UP) Banks
-----
* UP project bannnotated text in different languages with universal semantic role labelling annotations.
* This project used the frame and role labels of the English PropBank.

* References

  * Akbik, A., Chiticariu, L., Danilevsky, M., Li, Y., Vaithyanathan, S., & Zhu, H. (2015, July). Generating high quality proposition banks for multilingual semantic role labeling. In *Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1)* (pp. 397-407).

  * See also https://universalpropositions.github.io/
