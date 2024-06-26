baby_sitting_age_premise = 18
baby_sitting_age_hypothesis = 88

# the hypothesis refers to the age Jane started baby-sitting, which is also mentioned in the premise
if baby_sitting_age_hypothesis < baby_sitting_age_premise:
    # check if the hypothesis age is less than the premise age, which would be a contradiction
    label = "contradiction"
elif baby_sitting_age_hypothesis == baby_sitting_age_premise:
    # if the hypothesis age is equal to the premise age, we can infer entailment
    label = "entailment"
else:
    # any age greater than 'baby_sitting_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
