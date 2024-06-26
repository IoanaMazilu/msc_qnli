jane_age_premise = 18
jane_age_hypothesis = 58

# the hypothesis refers to the age of Jane when she started baby-sitting, mentioned in the premise
if jane_age_hypothesis == jane_age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age greater than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
