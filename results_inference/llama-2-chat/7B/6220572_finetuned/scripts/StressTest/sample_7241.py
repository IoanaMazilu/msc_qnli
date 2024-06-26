father_age_premise = 1/6
father_age_hypothesis = 1/6

# the hypothesis talks about the father's age, referenced also in the premise
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'father_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the father's age
    # any father's age greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
