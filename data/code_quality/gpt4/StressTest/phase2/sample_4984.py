father_age_premise = 48
father_age_hypothesis = 58
mother_age_premise = 42
mother_age_hypothesis = 42

# the hypothesis talks about the age of Ayesha's parents when she and her brother were born
if father_age_hypothesis <= father_age_premise:
    # check if the father's age in the hypothesis contradicts the estimate of more than 'father_age_premise'
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the mother's age at the time of her brother's birth in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the father's age
    # a father's age greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
