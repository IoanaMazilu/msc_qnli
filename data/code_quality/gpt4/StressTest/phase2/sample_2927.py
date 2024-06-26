age_father_sobha_birth_premise = 38
age_father_sobha_birth_hypothesis = 38
age_mother_brother_birth_premise = 36
age_mother_brother_birth_hypothesis = 36

# the hypothesis refers to the ages of Sobha's parents at the time of her and her brother's birth
if age_father_sobha_birth_premise != age_father_sobha_birth_hypothesis:
    # check if the age of Sobha's father at her birth in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif age_mother_brother_birth_premise != age_mother_brother_birth_hypothesis:
    # check if the age of Sobha's mother at the time of her brother's birth contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
