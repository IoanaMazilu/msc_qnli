age_premise = 20
age_hypothesis = 40

# the hypothesis refers to the age of Jane when she started baby-sitting
if age_hypothesis >= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the age in the premise
    label = "contradiction"
else:
    # the premise gives an exact age for Jane when she started baby-sitting
    # any age less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
