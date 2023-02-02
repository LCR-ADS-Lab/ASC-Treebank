ASC guideline
=====

In this section, we will provide more detailed descriptions and examples of the ASC types that we included in the current study. Note that all examples in the following subsections come from the training section of the treebank.

.. _ATTR:

******
ATTR
******
* The **attributive** (ATTR) ASC includes two arguments, namely a *theme* and an *attribute*. The *attribute* is prototypically represented by a noun phrase, an adjective phrase, or a prepositional phrase. Most commonly, the copular verb *be* is used. The verbs *seem* and *look* alsoappear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-V\ :sub:`copular`-NP/AdjP/PP

  * **Semantic frame (example)**: X\ :sub:`theme`  is Y\ :sub:`attribute`
  
  * **Examples sentences**
  
    * *it*\ :sub:`theme` *was* *an evoluation*\ :sub:`attribute`
    
    * *I*\ :sub:`theme` *am* *sure*\ :sub:`attribute`
    
    * *your dog*\ :sub:`theme` ... *is* *in the same room*\ :sub:`attribute`


.. _INTRAN_S:

******
INTRAN_S
******
* The **intransitive simple** (INTRAN_S) ASC includes a single argument and typically denotes either what *agent* does or what happens to a *theme*. In the training set, the verbs *go*, *work*, and *live* appear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-V 

  * **Semantic frame (example)**: X\ :sub:`agent` act; X\ :sub:`theme` happens
  
  * **Examples**
  
    * *I*\ :sub:`agent` *am working from our Hong Kong office*
    
    * *Martin's box*\ :sub:`theme` *is working wonderfully*


.. _INTRAN_MOT:

******
INTRAN_MOT
******
* The **intransitive motion** (INTRAN_MOT) ASC involves two arguments including a *mover/theme* and a *path* (Goldberg, 1995). The path is prototypically denoted via an adverbial particle or a prepositional phrase. The verbs *go*, *come*, and *get* appear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-V-AdvPr/PP 

  * **Semantic frame (example)**: X\ :sub:`theme` moves Y\ :sub:`path` 
  
  * **Examples**
  
    * *the morbidity rate*\ :sub:`theme` *is going* *up*\ :sub:`path`
    
    * *I*\ :sub:`theme` *went* *across the bay*\ :sub:`path`
    

.. _INTRAN_RES:

******
INTRAN_RES
******
* The **intransitive resultative** (INTRAN_RES) ASC involves two arguments including a *patient* and a *result*. The result denotes a patient's changed state. The verbs *become*, *come*, *go* appear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-V-NP/AdjP  

  * **Semantic frame (example)**: X\ :sub:`patient` becomes Y\ :sub:`result` 
  
  * **Examples**
  
    * *the spine*\ :sub:`patient` *will become* *flexible*\ :sub:`result`
    
    * *these weapons*\ :sub:`experiencer` *have* *gone*\ :sub:`result`
    
    
.. _TRAN_S:

******
TRAN_S
******
* The **transitive simple** (TRAN_S) ASC involves two arguments that describe an action done by a subject to an object, thus prototypically includes an *agent* and a *theme/patient* as arguments. This construction may include several subcategories (as well as a various semantic arguments) such as mental activities, explanations of a subject's state, and communication activities such as speaking or writing (Biber et al., 1999). The most frequent verbs within this construction in the EWT/ASCT are *have*, *do*, and *get*.

  * **Syntactic frame (example)**: Subj-V-Obj  

  * **Semantic frame (example)**: X\ :sub:`agent` acts on Y\ :sub:`patient` 
  
  * **Examples**
  
    * *they*\ :sub:`agent` *are targeting* *ambulances*\ :sub:`theme`
    
    * *I*\ :sub:`agent` *thought* *the US government was looking for me*\ :sub:`theme` (mental activity)
    
    * *I*\ :sub:`experiencer` *love* *my gym*\ :sub:`stimulus` (state)
   
    * *he*\ :sub:`agent` *claimed* *that they have the means to stage*\ :sub:`topic`
       
    
.. _DITRAN:

******
DITRAN
******
* The **ditransitive** (DITRAN) ASC prototypically includes three arguments of *agent*, *recipient*, and *theme*, evoking the notion of literal or metaphorical transfer. This construction is inclusive of the transfer of a topic during communication. The verbs *give* and *send* appear frequently, and the verbs *tell* and *ask* appear commonly when the construction is used in a communication situation.

  * **Syntactic frame (example)**: Subj-V-Obj\ :sub:`indirect`-Obj\ :sub:`direct`

  * **Semantic frame (example)**: X\ :sub:`agent` causes Y\ :sub:`recipient` to receive Z\ :sub:`theme`
  
  * **Examples**
  
    * *you*\ :sub:`agent` *feed* *your rabbits*\ :sub:`recipient` *non-veg items*\ :sub:`theme`
    
    * *I*\ :sub:`agent` *told* *the little girl*\ :sub:`recipient` *that she would have to accompany me to school*\ :sub:`topic` (communication)
   

.. _CAUS_MOT:

******
CAUS_MOT
******
* The **caused-motione** (CAUS_MOT) ASC is one of the complex transitive constructions, which include three arguments. The construction involves an *agent* that causes a *theme* to move along a path designated by a directional phrase (Goldberg, 1999). Semantically, this construction is inclusive of both direct and indirect causation. The verbs *put*, *take*, and *send* appear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-V-Obj-PP 

  * **Semantic frame (example)**: X\ :sub:`agent` causes Y\ :sub:`theme` to move Z\ :sub:`path/goal`
  
  * **Examples**
  
    * *I*\ :sub:`agent` *took* *it*\ :sub:`theme` *there*\ :sub:`destination` (direct causation)
    
    * *the body*\ :sub:`agent` *brings* *stability*\ :sub:`theme` *to the region*\ :sub:`goal` (indirect causation)


.. _TRAN_RES:

******
TRAN_RES
******
* The **transitive resultative** (TRAN_RES) ASC is the other type of the complex transitive constructions. The construction involves an *agent*, a *theme*, and a *result* wherein the *agent* causes the theme to become the *result*. We also include verb-particle constructions wherein the paired particle has a figurative meaning of the resultative state. The verbs *let*, *make* and *get* appear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-V-Obj-NP/AdjP 

  * **Semantic frame (example)**: X\ :sub:`agent` causes Y\ :sub:`theme` to become Z\ :sub:`state`
  
  * **Examples**
  
    * *the vessel*\ :sub:`agent` *changed* *its name*\ :sub:`patient` *at sea* *to Horizon*\ :sub:`result`
    
    * *no preacher*\ :sub:`agent` *has ever blow* *himself*\ :sub:`theme` *up*\ :sub:`C-V`
    

.. _PASSIVE:

******
PASSIVE
******
* The **passive** (PASSIVE) ASC contains short passive (a form without an expressed agent in *by*-phrase and long passive (with an expressed agent). We also include past particle pre-modifiers and post-modifiers in this ASC type. The verbs *do*, *attach*, and *make* appear frequently with this construction in the EWT/ASCT.

  * **Syntactic frame (example)**: Subj-auxV\ :sub:`past participle` (-*by*-PP) 

  * **Semantic frame (example)**: X\ :sub:`theme` undergo V  (*by* Y\ :sub:`agent`)
  
  * **Examples**
  
    * *you*\ :sub:`theme` *are* *invited*\ :sub:`Vpassive` *to join with members of the forum*
    
    * *...coined*\ :sub:`Vpassive` *by Bill Gates*\ :sub:`agent` 
    
    * *... overlooked*\ :sub:`Vpassive` *problem*\ :sub:`theme` (past participle pre-modifiers)
    
    * *she guided me through a very difficult period dealing with a family member's suicide* *coupled*\ :sub:`Vpassive` *with elder abuse*
    
   
******
* Notes
******
- Each ASC type is tagged next to the main verb head of argument structure construction (e.g., *He* **sneezed**\ :sub:`CAUS_MOT` *the foam off the table*).
- Multiple, overlaping ASCs may be present in a particular utterance. For example, a clausal argument of an ASC will represent an additional ASC (e.g., [*But the best way* **is**\ :sub:`ATTR` [*to* **use**\ :sub:`TRAN_S` *coupons*]]).
