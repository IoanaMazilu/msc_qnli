gangs_mala_premise = 2
gangs_mala_hypothesis = 5

# the hypothesis talks about the number of gangs Mala has, referenced also in the premise
if gangs_mala_hypothesis <= gangs_mala_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gangs_mala_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs Mala has
    # any number of gangs greater than 'gangs_mala_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
