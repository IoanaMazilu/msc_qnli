jane_age_start_babysitting_premise = 20
jane_age_start_babysitting_hypothesis = 40

# the hypothesis talks about the age of Jane when she started baby-sitting, referenced also in the premise
if jane_age_start_babysitting_hypothesis <= jane_age_start_babysitting_premise:
    # check if the hypothesis value contradicts the age of Jane when she started baby-sitting in the premise
    label = "contradiction"
else:
    # the premise gives the exact age of Jane when she started baby-sitting
    # any age less than 'jane_age_start_babysitting_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)