# the hypothesis talks about the number of gangs in a friendship gang, referenced also in the premise
if gangs_premise <= gangs_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'gangs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs
    # any number of gangs greater than 'gangs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
