travelled_premise = 10
travelled_hypothesis = 10

# the hypothesis talks about the number of hours travelled, referenced also in the premise
if travelled_hypothesis <= travelled_premise:
    # check if the hypothesis value contradicts the estimate of more than 'travelled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours travelled
    # any number of hours travelled greater than 'travelled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
