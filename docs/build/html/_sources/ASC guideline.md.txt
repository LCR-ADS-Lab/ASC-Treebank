ASC guideline
=====

In this section, we will provide more detailed descriptions and examples of the ASC types that we included for the current study. Note that all examples in the following subsections come from the training section of the treebank.

<a name="attr"></a>
#### `ATTR`
  - **Attributive** ASC
  - **Form**: Subj V<sub>copular</sub> NP/AdjP/PP
  - **Meaning**: X<sub>theme</sub> is Y<sub>attribute</sub>
  - **Examples**
    - [_it_]<sub>theme</sub> _was_ [_an evolution_]<sup>NP</sup><sub>attribute</sub>
    - [_I_]<sub>theme</sub> _am_ [_sure_]<sup>AdjP</sup><sub>attribute</sub>
    - [_your dog_]<sub>theme</sub> ... _is_ [_in the same room_]<sup>PP</sup><sub>attribute</sub>


<a name="intrns"></a>
#### `INTRAN_S`
  - **Intransitive simple** ASC
  - **Form**: Subj V
  - **Meaning**: X<sub>agent</sub> acts; X<sub>theme</sub> happens
  - **Examples**
    - [_I_]<sub>agent</sub> _am working from our Hong Kong office_
    - [_Martin's box_]<sub>theme</sub> _is working wonderfully_ 


<a name="intranm"></a>
#### `INTRAN_MOT`
  - **Intransitive motion** ASC 
  - **Form**: Subj V Obl
  - **Meaning**: X<sub>mover/theme</sub>  moves Y<sub>path</sub>
  - **Examples**
    - [_the morbidity rate_]<sub>theme</sub> _is going_ [_up_]<sup>AdvPR</sup><sub>ARGM-DIR</sub>
    - [_I_]<sub>theme</sub> _went_ [_across the bay_]<sup>PP</sup><sub>goal</sub>


<a name="intranr"></a>
#### `INTRAN_RES`
  - **Intransitive resultative** ASC
  - **Form**: Subj V RP
  - **Meaning**: X<sub>patient</sub> becomes Y<sub>state</sub>
  - **Example**
    - [_the spine_]<sub>patient</sub> _will become_ [_flexible_]<sub>result</sub>
    

<a name="trns"></a>
#### `TRAN_S`
  - **Transitive simple** ASC
  - **Form**: Subj V Obj
  - **Meaning**: X<sub>agent</sub> acts on Y<sub>patient/theme</sub> 
  - **Examples** (may include subcategories)
    - [_they_]<sub>agent</sub> _are targeting_ [_ambulances_]<sub>theme</sub>
    - mental activities: [_I_]<sub>agent</sub> _thought_ [_the US government was looking for me_]<sub>theme</sub> 
    - state: [_I_]<sub>experiencer</sub> _love_ [_my gym_]<sub>stimulus</sub>
    - communication: [_he_]<sub>agent</sub> _claimed_ [_that they have the means to stage_]<sub>topic</sub> 


<a name="dtrs"></a>
#### `DITRAN`
  - **Ditransitive** ASC
  - **Form**: Subj V Obj<sub>1</sub> Obj<sub>2</sub>
  - **Meaning**: X<sub>agent</sub> causes Y<sub>recipient</sub> to receive Z<sub>theme</sub>
  - **Examples** (may include subcategories)
    - [_you_]<sub>agent</sub> _feed_ [_your rabbits_]<sub>recipient</sub> [_non-veg items_]<sub>theme</sub>
    - communication: [_I_]<sub>agent</sub> _told_ [_the little girl_]<sub>recipient</sub> [_that she would have to accompany me to school_]<sub>topic</sub>


<a name="caumot"></a>
#### `CAUS_MOT`
  - **Caused-motion** ASC
  - **Form**: Subj V Obj Obl
  - **Meaning**: X<sub>agent</sub> causes Y<sub>theme</sub> to move Z<sub>path</sub>
  - **Examples**
    - [_I_]<sub>agent</sub> _took_ [_it_]<sub>theme</sug> [_there_]<sub>destination</sub>
    - [_the body_]<sub>agent</sub> _brings_ [_stability_]<sub>theme</sub> [_to the region_]<sub>goal</sub>

<a name="tranr"></a>
#### `TRAN_RES`
  - **Transitive resultative** ASC
  - **Form**: Subj V Obj RP
  - **Meaning**: X<sub>agent</sub>> causes Y<sub>patient/theme</sub> to become Z<sub>result</sub>
  - **Examples**
    - [_the vessel_]<sub>agent</sub> _changed_ [_its name_]<sub>patient</sub> _at sea to_ [_Horizon_]<sub>result</sub>
    - [_No preacher_]<sub>agent</sub> _has ever blow_ [_himself_]<sub>theme</sub> [_up_]<sub>C-V</sub>


<a name="pass"></a>
#### `PASSIVE`
  - **Passive** ASC
  - **Form**: Subj aux V <sup>past participle</sup> (_by_-PP)
  - **Meaning**: X<sub>theme</sub> undergo V (_by_ Y<sub>agent</sub>)
  - **Examples** (may include subcategories)
    - [_you_]<sub>theme</sub> _are invited_<sup>Vpassive</sup> _to join with members of the forum_
    - _coined_<sup>Vpassive</sup> [_by Bill Gates_]<sub>agent</sub>
    - past participle pre-modifiers: _overlooked_<sup>Vpassive</sup> [problem]<sub>theme</sub> 
    - past participle post-modifiers: _she guided me through a very difficult period dealing with a family member's suicide_, _coupled_<sup>Vpassive</sup> with elder abuse

---------

#### Notes
- Each ASC type is tagged next to the main verb head of argument structure construction (e.g., _He **sneezed**<sub>CAUS_MOT</sub> the foam off the table_).
- Multiple, overlaping ASCs may be present in a particular utterance. For example, a clausal argument of an ASC will represent an additional ASC (e.g., [_But the best way **is**_<sub>ATTR</sub> [_to **use**<sub>TRAN_S</sub> coupons_]]).


#### Abbreviations
