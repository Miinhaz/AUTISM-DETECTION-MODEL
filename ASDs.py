from pydantic import BaseModel

class ASD(BaseModel):
    Does_your_child_look_at_you_when_you_call_his_name: int
    How_easy_is_it_for_you_to_get_eye_contact_with_your_child: int
    Does_your_child_point_to_indicate_that_he_wants_something: int
    Does_your_child_point_to_indicate_what_he_want: int
    Does_your_child_point_to_share_interest_with_you: int
    Does_your_child_follow_where_you_are_looking: int
    if_you_or_somweone_in_the_family_is_visibly_upset_does_your_child_show_sign_to_comfort_them: int
    Would_you_describe_your_childs_first_word_as_typical_or_unusual: int
    Does_your_child_use_simple_gestures_like_waving_goodbye: int
    Does_your_child_stare_at_nothing_with_no_apparent_purpose: int
    Age_Mons: int
    Sex: int
    Ethnicity: int  
    Jaundice: int
    Family_mem_with_ASD: int
    Who_completed_the_test: int
   
 