# Premise: Ayesha's father was 38 years of age when she was born while her mother was 36 years old when her brother four years younger to her was born.
# Hypothesis: Ayesha's father was 18 years of age when she was born while her mother was 36 years old when her brother four years younger to her was born.
# Golden Label: contradiction

father_age_birth_ayesha_premise = 38
father_age_birth_ayesha_hypothesis = 18
mother_age_birth_brother_premise = 36
mother_age_birth_brother_hypothesis = 36

# the hypothesis refers to the age of Ayesha's parents when she and her brother were born, information also available in the premise
if father_age_birth_ayesha_premise != father_age_birth_ayesha_hypothesis:
    # check if the father's age at Ayesha's birth in the hypothesis contradicts the age given in the premise
    label = "contradiction"
elif mother_age_birth_brother_premise != mother_age_birth_brother_hypothesis:
    # check if the mother's age at the brother's birth in the hypothesis contradicts the age given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

