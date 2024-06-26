father_age_premise = 1/6
father_age_hypothesis = 3/6

# the hypothesis refers to the ratio of Ayisha's age to her father's age mentioned in the premise
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'father_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of Ayisha's age to her father's age
    # any ratio less than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
