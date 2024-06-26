gangs_aravind_premise = 1
gangs_aravind_hypothesis = 2

# the hypothesis talks about the number of Aravind's gangs, referenced also in the premise
if gangs_aravind_hypothesis <= gangs_aravind_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gangs_aravind_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Aravind's gangs
    # any number of gangs greater than 'gangs_aravind_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
