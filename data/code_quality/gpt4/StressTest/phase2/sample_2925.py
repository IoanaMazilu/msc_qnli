father_age_sobha_birth_premise = 38
father_age_sobha_birth_hypothesis = 28
mother_age_brother_birth_premise = 36
mother_age_brother_birth_hypothesis = 36

# the hypothesis refers to the ages of Sobha's parents at their children's birth, mentioned in the premise
if father_age_sobha_birth_premise <= father_age_sobha_birth_hypothesis:
    # check if the estimate of 'father_age_sobha_birth_hypothesis' contradicts the age of father at Sobha's birth in the premise
    label = "contradiction"
elif mother_age_brother_birth_hypothesis != mother_age_brother_birth_premise:
    # check if the age of mother at brother's birth in the hypothesis contradicts the age of mother at brother's birth reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
