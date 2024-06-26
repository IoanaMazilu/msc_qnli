gangs_premise = 5
gangs_hypothesis = 2

# the hypothesis refers to the number of gangs in a friendship gang, which is also mentioned in the premise
if gangs_hypothesis <= gangs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gangs_premise' gangs
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs
    # any number of gangs greater than 'gangs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
