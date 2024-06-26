female_workforce_premise = 50
female_workforce_hypothesis = 60

# the hypothesis refers to the percentage of female workforce in Samsung, also mentioned in the premise
if female_workforce_hypothesis <= female_workforce_premise:
    # check if the hypothesis value contradicts the estimate of more than 'female_workforce_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of female workforce
    # any percentage greater than 'female_workforce_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
